import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
IMG_DIR = os.path.join(BASE_DIR, "images")

SRC_DIR = os.path.join(BASE_DIR, "src")

def create_directories():
    for directory in [DATA_DIR, IMG_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"[OK] Pasta criada: {directory}")
        else:
            print(f"[OK] Pasta já existe: {directory}")

def run_script(script_name):
    script_path = os.path.join(SRC_DIR, script_name)
    print(f"\n▶ Executando {script_name}...")
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"[ERRO] Falha em {script_name}")
        print(result.stderr)
        sys.exit(1)

    print(result.stdout)

def main():
    print("🚀 Iniciando pipeline de churn\n")

    create_directories()

    run_script("generate_data.py")
    run_script("train_model.py")
    run_script("interpret_model.py")
    run_script("visualize_tree.py")

    print("\n✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()
