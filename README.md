# 🔥 Pipeline de Análise e Monitoramento de Focos de Queimadas 

## 💻 Sobre o Projeto

O **Pipeline de Análise e Monitoramento de Focos de Queimadas** consiste em uma infraestrutura de dados (Data Pipeline) projetada para automatizar a ingestão, o processamento e a consolidação de dados históricos de focos de queimadas (incêndios florestais).

Esta aplicação foi desenvolvida como parte da atividade prática para demonstrar a implementação da camada **Bronze** de um Data Lake (Lakehouse/Medallion Architecture) em um ambiente simulado. O objetivo final é criar uma base de dados limpa, particionada e consolidada em formato parquet, que servirá como fonte de dados confiável para análises geoespaciais e relatórios.

### 🔗 Arquitetura Implementada (Camada Bronze)

O pipeline implementado no ambiente simulado (Google Colab) estabelece a camada **Bronze** do Data Lake com as seguintes características:

| Etapa | Fluxo de Dados | Lógica Implementada |
| :--- | :--- | :--- |
| **Ingestão** | Google Drive (Fonte) → Bronze Raw | Cópia de arquivos CSV de uma fonte externa (Drive) para o ambiente de processamento. |
| **Armazenamento Raw** | Bronze Raw | Estrutura de particionamento hierárquico por data (`ano={yyyy}/mes={mm}`) para os CSVs originais. |
| **Transformação** | Bronze Raw → Bronze Current | Concatenamento de DataFrames, enriquecimento com metadados (`ano`, `mes`) e aplicação de **impenência** (remoção de duplicatas). |
| **Armazenamento Final** | Bronze Current | Salvamento do conjunto de dados limpo e consolidado no formato **Parquet** e CSV. |

### 🛠 Tecnologias Utilizadas

| Camada | Tecnologias Atuais (Open Source/Simuladas) |
| :--- | :--- |
| **Linguagem/Processamento** | Python, Pandas |
| **Ambiente/Orquestração** | Google Colab (Execução manual/interativa) |
| **Armazenamento (Fonte/Destino)** | Google Drive (Fonte), File System do Colab (Destino), CSV, Parquet |

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python"/> &nbsp; <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> &nbsp; <img src="https://img.shields.io/badge/apache%20parquet-2A62AA?style=for-for-the-badge&logo=apache&logoColor=white" alt="Parquet"/>

### 🚀 Sugestões de Refinamento (Tecnologias Pagas/Gerenciadas)

Para levar este pipeline a um ambiente de produção escalável e robusto, sugerimos a migração para o ecossistema Google Cloud Platform (GCP):

* **Armazenamento Central:** **Google Cloud Storage (GCS)** para o Data Lake e **Google BigQuery** para o Data Warehouse analítico.
* **Orquestração:** **Google Cloud Composer** (Apache Airflow Gerenciado) para agendamento, monitoramento e gestão do fluxo de trabalho.
* **Processamento em Escala:** **Google Cloud Dataproc** (Apache Spark Gerenciado) para processamento distribuído de grandes volumes de dados.

<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud"/> &nbsp; <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white" alt="Apache Airflow"/> &nbsp; <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white" alt="Apache Spark"/>

***

## 🗂 Como rodar o projeto (Ambiente Simulador)

As instruções a seguir pressupõem a execução no ambiente interativo do Google Colab:

```bash
# 1. Carregar o arquivo 'queimadas.ipynb' no Google Colab.
# 2. Executar as células de setup e importações iniciais.

# 3. Montar o Google Drive para acessar a fonte de dados simulada (CSV):
# from google.colab import drive
# drive.mount('/content/drive')

# 4. Executar o pipeline de Ingestão:
#    - Criação da estrutura de pastas de destino (Bronze Raw, Bronze Current).
#    - Cópia dos CSVs da fonte para a pasta Bronze Raw particionada.

# 5. Executar o pipeline de Transformação:
#    - Leitura e concatenação dos DataFrames.
#    - Aplicação da lógica de limpeza e remoção de duplicatas.

# 6. Executar o pipeline de Armazenamento:
#    - Salvamento do DataFrame consolidado no formato CSV e Parquet.
```
## 📝 Documento de Arquitetura

### Fonte dos Dados

| Campo | Conteúdo |
| :--- | :--- |
| **Fonte de Dados** | Arquivos CSV de focos de queimadas (Ex: dados do INPE/Monitoramento). |
| **Localização da Fonte** | Google Drive (Simulação de fonte externa) |
| **Formato de Entrada** | CSV (Comma Separated Values) |

***

## ✅ Checklist do Estado Atual

A implementação atual no `queimadas.ipynb` reflete a conclusão das seguintes fases do pipeline:

| Parte do Pipeline | Estado Atual (Ambiente Colab) |
| :--- | :--- |
| **Ingestão** | **(x) Finalizado** (Cópia da fonte para o Bronze Raw) |
| **Armazenamento** | **(x) Finalizado** (Estrutura de Data Lake Bronze implementada) |
| **Transformação** | **(x) Finalizado** (Limpeza básica, metadados e deduplicação aplicadas) |

***

## 🚀 Equipe e Divisão de Tarefas

| Membro da Equipe | Função | Tarefas e Responsabilidades |
| :--- | :--- | :--- |
| **Julio Padilha** | **Engenheiro de dados(Otimização e Escalabilidade do Pipeline)** | Expandiu o dataset de 1 para 22 meses, realizando a concatenação e integração de arquivos. Implementou soluções de otimização de desempenho e memória com Dask e cuDF, aproveitando o processamento paralelo e o uso da GPU do Colab. |
| **Matheus Bione** | **Suporte Técnico** | Verificando se os dados transformados mantêm integridade em relação à ingestão original. Realizou a organização de diretórios, limpeza de arquivos duplicados e padronização de nomes dentro do projeto. |
| **Nicole Victory** | **Analista de dados(validação e qualidade dos dados)** | Criou scripts para verificação e limpeza dos datasets após a ingestão na camada Bronze, garantindo que os arquivos contenham as colunas esperadas e sem valores nulos críticos. Gerou relatórios automáticos de estatísticas e qualidade dos dados (profiling) para documentação e análise. |
| **Roberto Arruda** | **Cientista de Dados (Ingestão e Modelagem)** |  Realizou a ingestão inicial dos dados, estruturando o pipeline nas camadas Bronze, Silver e Gold. Foi responsável pela organização da arquitetura de pastas, padronização do fluxo de dados e pela criação das primeiras transformações entre as camadas. |


***

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
