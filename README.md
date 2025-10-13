# 🔥 Pipeline de Análise e Monitoramento de Focos de Queimadas 

## 💻 Sobre o Projeto

O **Pipeline de Análise e Monitoramento de Focos de Queimadas** consiste em uma infraestrutura de dados (Data Pipeline) projetada para automatizar a ingestão, o processamento e a consolidação de dados históricos de focos de queimadas (incêndios florestais).

Esta aplicação foi desenvolvida como parte da atividade prática para demonstrar a implementação até camada **Silver** de um Data Lake (Lakehouse/Medallion Architecture) em um ambiente simulado. O objetivo final é criar uma base de dados limpa, particionada e consolidada em formato parquet, que servirá como fonte de dados confiável para análises geoespaciais e relatórios.

### 🔗 Arquitetura Implementada 

O pipeline implementado no ambiente simulado (Google Colab) estabelece a camada **Bronze** do Data Lake com as seguintes características:

| Etapa | Lógica Implementada |
| :--- | :--- |
| **Ingestão** | Cópia de arquivos CSV de uma fonte externa (Drive) para o ambiente de processamento. |
| **Armazenamento Raw** | Estrutura de particionamento hierárquico por data (`ano={yyyy}/mes={mm}`) para os CSVs originais. |
| **Transformação**| Concatenamento de DataFrames, enriquecimento com metadados (`ano`, `mes`) e aplicação de **impenência** (remoção de duplicatas). |
| **Armazenamento Final**  | Salvamento do conjunto de dados limpo e consolidado no formato **Parquet** e CSV. |

### 🛠 Tecnologias Utilizadas

| Camada | Tecnologias Atuais (Open Source/Simuladas) |
| :--- | :--- |
| **Linguagem/Processamento** | Python, Pandas, Dask, cuDF |
| **Ambiente/Orquestração** | Google Colab (Execução manual/interativa) |
| **Armazenamento (Fonte/Destino)** | Google Drive (Fonte), File System do Colab (Destino), CSV, Parquet |

<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="python"/> &nbsp; <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> &nbsp;  <img src="https://img.shields.io/badge/Dask-F8766D?style=for-the-badge&logo=dask&logoColor=white" alt="Dask"/> &nbsp; <img src="https://img.shields.io/badge/cuDF-7097C2?style=for-the-badge&logo=nvidia&logoColor=white" alt="cuDF"/>

### 🚀 Sugestões de Refinamento (Tecnologias Pagas/Gerenciadas na AWS)

Para levar o pipeline, que já utiliza aceleração por GPU (cuDF/Dask-cuDF), a um ambiente de produção escalável e robusto, sugerimos a migração para o ecossistema **Amazon Web Services (AWS)**:

* **Armazenamento e Data Lakehouse (S3 & Athena/Redshift):**
    * O armazenamento central (Data Lake) deve ser persistido e escalado no **Amazon S3 (Simple Storage Service)**, ideal para armazenar os arquivos Parquet.
    * O destino analítico deve ser o **Amazon Athena** (consultas *serverless* diretamente no S3) ou o **Amazon Redshift** (Data Warehouse), implementando a arquitetura *Lakehouse*.

* **Orquestração e Automação (MWAA & Step Functions):**
    * O agendamento robusto e o monitoramento do *workflow* serão feitos com o **Amazon Managed Workflows for Apache Airflow (MWAA)**, mantendo a flexibilidade do Airflow.
    * Para *workflows* mais específicos ou *serverless*, pode-se utilizar **AWS Step Functions**.

* **Processamento Acelerado em Produção (AWS EMR & ECS/SageMaker):**
    * O processamento distribuído em escala será garantido pelo **Amazon EMR** configurado para rodar *clusters* **Apache Spark** (sem MapReduce).
    * Para manter a aceleração por GPU (Dask-cuDF/RAPIDS) em produção, sugere-se a utilização do **Amazon ECS (Elastic Container Service)** ou **Amazon SageMaker**, executando *containers* em instâncias **EC2** otimizadas com GPUs dedicadas (família P3/P4), garantindo a alta performance alcançada no Colab.

<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"/> &nbsp; <img src="https://img.shields.io/badge/Amazon_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white" alt="Amazon S3"/> &nbsp; <img src="https://img.shields.io/badge/Amazon_Redshift-C02A36?style=for-the-badge&logo=amazonredshift&logoColor=white" alt="Amazon Redshift"/> &nbsp; <img src="https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=Apache-Airflow&logoColor=white" alt="Apache Airflow"/> &nbsp; <img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white" alt="Apache Spark"/>

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
#    - Criação da estrutura de pastas de destino.
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
