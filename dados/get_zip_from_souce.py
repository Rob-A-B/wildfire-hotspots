# Considerando que os arquivos de dados eram muito grandes, não sendo possível de 
# mandar para o repositório no github, este script mostra fonte e processo de download
# para os arquivos RAW utilizados no projeto.


import os
import re
import requests
import zipfile
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed

# URL base da listagem
BASE_URL = "https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/mensal/Brasil/"
DEST_DIR = "downloads_inpe"
EXTRACT_DIR = os.path.join(DEST_DIR, "extraidos")
os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

# Regex para achar arquivos mensais .zip ou .csv
PADRAO = re.compile(r'href="(focos_mensal_br_2023\d{2}\.(?:zip|csv))"', re.IGNORECASE)

# --- 1) Obter a lista de arquivos disponíveis ---
resp = requests.get(BASE_URL, timeout=30)
resp.raise_for_status()
html = resp.text

arquivos = PADRAO.findall(html)
urls = [urljoin(BASE_URL, a) for a in arquivos]
print(f"Encontrados {len(urls)} arquivos.\n")

# --- 2) Função de download e extração ---
def baixar_e_extrair(url: str) -> str:
    nome = url.split("/")[-1]
    caminho_zip = os.path.join(DEST_DIR, nome)
    try:
        # Baixar
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(caminho_zip, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 64):
                    if chunk:
                        f.write(chunk)
        msg = f"OK  {nome} baixado."

        # Descompactar se for .zip
        if nome.lower().endswith(".zip"):
            with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
                zip_ref.extractall(EXTRACT_DIR)
            msg += f" Extraído em {EXTRACT_DIR}."
        return msg
    except Exception as e:
        return f"ERRO {nome} -> {e}"

# --- 3) Executar downloads em paralelo ---
with ThreadPoolExecutor(max_workers=4) as ex:
    futuros = [ex.submit(baixar_e_extrair, u) for u in urls]
    for fut in as_completed(futuros):
        print(fut.result())

print("\n✅ Todos os downloads e extrações foram concluídos.")