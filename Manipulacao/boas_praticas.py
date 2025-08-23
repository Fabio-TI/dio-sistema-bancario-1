from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "ilorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")

# arquivo.close()
