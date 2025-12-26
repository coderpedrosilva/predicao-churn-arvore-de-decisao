# 📊 Previsão de Churn com Árvore de Decisão (Churn Prediction with Decision Tree)

Este projeto demonstra a construção de um modelo de Aprendizado de Máquina supervisionado utilizando Árvore de Decisão, com foco em previsão de churn de clientes.

O objetivo é apresentar todo o pipeline de ML, desde a geração de dados sintéticos, passando por treinamento, avaliação, visualização da árvore, até a automação completa via script principal (`main.py`).

> Projeto desenvolvido inteiramente em Python, com execução local (Visual Studio Code), sem dependência de notebooks.

---

## 🎯 Objetivo do Projeto

Construir um modelo capaz de responder perguntas do tipo:

> “Dado o perfil de um cliente, ele tem alta probabilidade de cancelar o serviço (churn)?”

Esse tipo de problema é extremamente comum em Ciência de Dados, especialmente em:
- Telecom
- Streaming
- SaaS
- Bancos
- Assinaturas digitais

---

## 🧠 Conceitos Aplicados

- Aprendizado de Máquina Supervisionado
- Árvores de Decisão (Decision Tree Classifier)
- Entropia e Ganho de Informação
- Geração de dados sintéticos
- Feature engineering simples
- Treinamento e validação de modelo
- Avaliação com métricas de classificação
- Visualização do modelo aprendido
- Boas práticas de organização de projeto ML

---

## 🗂 Estrutura do Projeto

```text
predicao-churn-arvore-de-decisao/
│
├── data/ # (gerada automaticamente)
│ └── churn_synthetic.csv
│
├── images/ # (gerada automaticamente)
│ └── decision_tree.png
│
├── src/
│ ├── generate_data.py # Gera dataset sintético de churn]
│ ├── interpret_model.py # Interpreta decisões e importância das variáveis
│ ├── train_model.py # Treina e avalia a árvore de decisão
│ └── visualize_tree.py # Gera imagem da árvore aprendida
│
├── .gitignore
├── main.py # Orquestra todo o pipeline
├── requirements.txt
└── README.md
```

📌 Importante:
As pastas data/ e images/ não precisam ser criadas manualmente.
O main.py verifica e cria automaticamente se não existirem.

---

## 📦 Tecnologias Utilizadas

- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📈 Dataset

O dataset é 100% sintético, gerado via código, com aproximadamente 1.500 registros, simulando características comuns de clientes.

Exemplos de variáveis:
- Tempo de contrato
- Tipo de plano
- Uso mensal
- Reclamações
- Atrasos de pagamento
- Churn (variável alvo)

👉 O arquivo CSV não é versionado, seguindo boas práticas de ML.

---

## ⚙️ Instalação e Execução

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/coderpedrosilva/predicao-churn-arvore-de-decisao.git

cd predicao-churn-arvore-de-decisao
```

### 2️⃣ Crie um ambiente virtual (opcional, recomendado)
```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windows
```

### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o pipeline completo
```bash
python main.py
```

Esse comando irá:
1. Gerar o dataset sintético
2. Treinar o modelo de Árvore de Decisão
3. Avaliar o desempenho
4. Gerar a visualização da árvore em images/

---

## 🌳 Visualização do Modelo

O projeto gera automaticamente uma imagem da Árvore de Decisão, permitindo entender:
- Quais variáveis são mais importantes
- Como o modelo toma decisões
- Onde ocorrem os principais splits

---

## 📊 Avaliação do Modelo

O modelo é avaliado utilizando:
- Accuracy
- Relatório de Classificação (Precision, Recall, F1-score)

---

## 🚀 Diferenciais do Projeto

✔ Pipeline automatizado (sem notebooks)

✔ Código modular e organizado

✔ Dados gerados por script (reprodutibilidade)

✔ Visualização do modelo aprendido

✔ Estrutura profissional para portfólio

✔ Fácil extensão para outros algoritmos

---

## 🔮 Próximos Passos

- Ajuste de hiperparâmetros
- Comparação com Random Forest
- Validação cruzada
- Feature importance detalhada
- Exportação do modelo treinado
- API simples para inferência

---

Projeto desenvolvido com foco em aprendizado conceitual, clareza e boas práticas de Machine Learning.
