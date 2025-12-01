# 1. Introdução

O Brasil enfrenta um crescimento contínuo no número de focos de queimadas monitorados por satélite, tornando a análise e o monitoramento destes eventos um desafio típico de Big Data. A volumetria elevada e a velocidade de geração dos dados inviabilizam abordagens tradicionais de processamento baseadas em CPU e bibliotecas como Pandas, que apresentam gargalos devido à limitação de memória e baixa capacidade de paralelização.

Nesse contexto, este projeto propõe a construção de uma Plataforma Cloud para Big Data (PCB) capaz de realizar ingestão, transformação, análise exploratória e modelagem preditiva em escala massiva, utilizando aceleração por GPU e arquiteturas distribuídas.

# 2. Motivação e Justificativa
## 2.1 Relevância do Tema

A análise dos focos de calor é fundamental para a gestão ambiental, o planejamento de combate a incêndios e a formulação de políticas públicas. A demora na obtenção de insights pode custar recursos naturais, vidas e agravar crises climáticas. A implementação de uma plataforma de Big Data eleva a qualidade da resposta governamental e científica ao permitir:
- Detecção de Padrões: Identificação ágil de tendências sazonais e regionais de queimadas.
- Modelagem Preditiva: Treinamento rápido de modelos para prever as variáveis de interesse.
- Suporte à Decisão: Fornecimento de dados atualizados para equipes em campo e tomadores de decisão.

# 2.2 Justificativa Tecnológica

A adoção de uma arquitetura distribuída de Big Data é motivada por:
- Limitações de RAM: conjuntos de dados maiores que a memória inviabilizam o uso de Pandas/CPU.
- Demanda de desempenho: análises exploratórias e ciclos de treinamento de modelos exigem múltiplas leituras e operações pesadas.
- Escalabilidade: ambientes cloud distribuem carga, adaptam-se ao volume crescente de dados e eliminam a necessidade de migrações complexas.

Assim, tecnologias como Dask-cuDF, GPU NVIDIA Tesla T4 e formato Parquet tornam-se essenciais para obter desempenho adequado.

# 3. Objetivo do Projeto

O objetivo principal deste projeto é desenvolver e implementar uma Plataforma Cloud para Big Data (PCB) capaz de processar, analisar e modelar os dados de focos de queimadas em escala massiva e com alta performance seguindo a arquitetura Medallion.

## 3.1 Objetivos Específicos

- Transformação e Consolidação (ETL): criação de pipelines para ingestão e transformação de dados brutos (Bronze) em versões limpas e otimizadas (Gold).
- Análises Exploratórias em Escala: geração de visualizações complexas e séries temporais com baixa latência.
- Modelagem Preditiva (ML): treinamento e avaliação de modelos de regressão para previsão de variáveis de interesse relacionadas a queimadas.

# 4. Metodologia (Pipeline de Dados)

A metodologia envolve a construção de um pipeline robusto e acelerado para processar dados históricos de queimadas em ambiente distribuído.

## 4.1 Arquitetura e Tecnologias

A arquitetura utiliza princípios de Data Lake simulado e aceleração por GPU, adotando:

<img src="https://cdn.discordapp.com/attachments/958708354765705256/1445015539184566453/image.png?ex=692ecf17&is=692d7d97&hm=853ac428fd687c73bb1d70e8c1edb2772892188093186948b9148fec62051b0a&" alt= "Tabela de arquitetura"></img>


## 4.2 Pipeline Implementado (Prova de Conceito)

A PoC validou a capacidade da arquitetura distribuída, com ênfase na fase Silver/Gold.

## 4.2.1 Fluxo de Processamento

Fontes: dados CSV previamente limpos.
Ingestão: carregamento dos dados para a camada Silver.
Armazenamento: persistência em arquivos Parquet particionados.
Transformação (Gold): utilização de Dask-cuDF para operações massivas de filtragem, agregação e manipulação de colunas.
Aceleração por GPU: operações executadas em ambiente com NVIDIA Tesla T4, comprovando desempenho superior ao Pandas/CPU.

## 4.2.2 Arquitetura Parcial e Ganhos

A PoC validou:
- Configuração e utilização adequada de GPU e bibliotecas RAPIDS.
- Throughput significativamente maior em leitura/transformação de Parquet.
- Viabilidade técnica para escalonar o pipeline em cenários reais de Big Data.

# 5. Resultados e Visualizações

A análise dos dados tratados permitiu compreender o comportamento das queimadas entre biomas brasileiros.

## 5.1 Distribuição Mensal

Observou-se um pico de queimadas entre julho e outubro, período atípico pois coincide com o inverno brasileiro. Em biomas como Amazônia e Cerrado, fatores como estiagem prolongada, déficit hídrico e influência do fenômeno El Niño (2024) explicaram a intensificação dos eventos.

## 5.2 Comparação Entre Biomas

Cerrado: vegetação seca, baixa umidade e clima sazonal explicam queimadas naturais, embora a ação humana também seja significativa.
Amazônia: grande parte das queimadas possui origem antropogênica; o ano de 2024 mostrou anomalias ligadas ao El Niño e à ausência da Zona de Convergência Intertropical (ZCIT).

## 5.3 Modelagem Preditiva

Dois modelos se destacaram:

Random Forest: identificou o pico anômalo de 2024 como padrão recorrente, falhando ao prever 2025.
Seasonal Ratio Forecasting: reconheceu a anomalia e previu 2025 com maior aderência aos dados reais.

# 6. Conclusão
## 6.1 Análise Crítica dos Resultados

O projeto demonstrou a viabilidade de uma arquitetura Big Data acelerada por GPU para processamento massivo de dados de queimadas.

A análise revelou padrões climatológicos consistentes e destacou a necessidade de distinguir eventos naturais de queimadas causadas por intervenções humanas. Modelos preditivos apresentaram diferentes sensibilidades a anomalias climáticas, com maior eficácia dos métodos sazonais em cenários com variabilidade extrema.

## 6.2 Dificuldades Encontradas

Limitações de hardware tradicional (RAM insuficiente).
Interpretação de anomalias climáticas em séries históricas (ex.: El Niño).
Complexidade de diferenciar causas naturais e antropogênicas.

## 6.3 Trabalhos Futuros

Expansão do pipeline para todo o histórico de queimadas.
Integração de dados meteorológicos e socioeconômicos.
Avaliação de modelos híbridos e Deep Learning.
Desenvolvimento de dashboards de monitoramento em tempo real.
