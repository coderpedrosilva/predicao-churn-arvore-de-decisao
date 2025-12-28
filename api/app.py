from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import os
import numpy as np
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "api", "model.joblib")
DATA_PATH = os.path.join(BASE_DIR, "data", "churn_synthetic.csv")
STATIC_DIR = os.path.join(BASE_DIR, "api", "static")

model = joblib.load(MODEL_PATH)

app = FastAPI(title="Churn Decision API")

# =========================
# Servir Frontend
# =========================
app.mount("/app", StaticFiles(directory=STATIC_DIR, html=True), name="static")

# =========================
# Modelo de entrada
# =========================
class ClienteInput(BaseModel):
    tempo_contrato_meses: int
    valor_mensal: float
    uso_total_gb: float
    chamadas_suporte: int
    pagamentos_atrasados: int
    tipo_contrato: str
    renovacao_automatica: int
    desconto: int

# =========================
# Predição individual
# =========================
@app.post("/predict")
def predict(cliente: ClienteInput):

    tipo_mensal = 1 if cliente.tipo_contrato == "mensal" else 0

    X = np.array([[
        cliente.tempo_contrato_meses,
        cliente.valor_mensal,
        cliente.uso_total_gb,
        cliente.chamadas_suporte,
        cliente.pagamentos_atrasados,
        tipo_mensal,
        cliente.renovacao_automatica,
        cliente.desconto
    ]])

    prob = model.predict_proba(X)[0][1]

    riscos = []
    protecao = []

    if cliente.chamadas_suporte >= 3: riscos.append("Muitas chamadas ao suporte")
    else: protecao.append("Baixo número de chamadas ao suporte")

    if cliente.pagamentos_atrasados >= 2: riscos.append("Pagamentos atrasados frequentes")
    else: protecao.append("Pagamentos em dia")

    if cliente.tipo_contrato == "mensal": riscos.append("Contrato mensal")
    else: protecao.append("Contrato anual")

    if cliente.tempo_contrato_meses < 12: riscos.append("Pouco tempo de contrato")
    else: protecao.append("Alto tempo de contrato")

    if cliente.renovacao_automatica == 0: riscos.append("Sem renovação automática")
    else: protecao.append("Renovação automática ativa")

    if cliente.desconto == 1: protecao.append("Possui desconto")

    return {
        "probabilidade_churn": round(float(prob), 2),
        "classe": "Cliente em Evasão" if prob >= 0.5 else "Cliente Ativo",
        "riscos": riscos,
        "protecao": protecao
    }

# =========================
# Listagem e monitoramento
# =========================
@app.get("/clientes")
def listar_clientes(ordenar: str = "desc", somente_risco: bool = False):

    df = pd.read_csv(DATA_PATH)
    resultados = []

    for i, row in df.iterrows():

        tipo_mensal = 1 if row["tipo_contrato"] == "mensal" else 0

        X = np.array([[
            row["tempo_contrato_meses"],
            row["valor_mensal"],
            row["uso_total_gb"],
            row["chamadas_suporte"],
            row["pagamentos_atrasados"],
            tipo_mensal,
            row["renovacao_automatica"],
            row["desconto"]
        ]])

        prob = model.predict_proba(X)[0][1]

        riscos = []
        protecao = []

        if row["chamadas_suporte"] >= 3: riscos.append("Muitas chamadas ao suporte")
        else: protecao.append("Baixo número de chamadas ao suporte")

        if row["pagamentos_atrasados"] >= 2: riscos.append("Pagamentos atrasados frequentes")
        else: protecao.append("Pagamentos em dia")

        if row["tipo_contrato"] == "mensal": riscos.append("Contrato mensal")
        else: protecao.append("Contrato anual")

        if row["tempo_contrato_meses"] < 12: riscos.append("Pouco tempo de contrato")
        else: protecao.append("Alto tempo de contrato")

        if row["renovacao_automatica"] == 0: riscos.append("Sem renovação automática")
        else: protecao.append("Renovação automática ativa")

        if row["desconto"] == 1: protecao.append("Possui desconto")

        classe = "Cliente em Evasão" if prob >= 0.5 else "Cliente Ativo"

        if somente_risco and classe == "Cliente Ativo":
            continue

        resultados.append({
            "cliente": f"Cliente {i+1}",
            "probabilidade": round(float(prob), 2),
            "classe": classe,
            "riscos": riscos,
            "protecao": protecao
        })

    resultados = sorted(resultados, key=lambda x: x["probabilidade"], reverse=(ordenar == "desc"))
    return resultados
