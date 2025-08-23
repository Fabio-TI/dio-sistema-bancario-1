import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(__file__)

#os.mkdir( ROOT_PATH / "novo-diretorio")
#arquivo = open(ROOT_PATH / "novo-arquvio.txt", "w")

#os.rename(ROOT_PATH / "novo-arquvio.txt", ROOT_PATH / "novo-arquivo.txt")

#os.remove(ROOT_PATH / "novo-arquivo.txt")

shutil.move(ROOT_PATH / "novo-arquivo.txt", ROOT_PATH / "novo-diretorio/novo-arquivo.txt")