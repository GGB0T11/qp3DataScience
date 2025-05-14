# 📊 Relatório do Projeto - Ciência de Dados

## 👥 Informações do Grupo
**Turma:** 3ºC
**Grupo:** 2
**Integrantes:** Acauã, Gustavo José Pedro, Sofia, Orlando

**Link do Dataset:** [IMDb Filmes](https://basedosdados.org/dataset/6ba4745d-f131-4f8e-9e55-e8416199a6af?table=79de8c5e-9c21-4398-a9fb-bc40e6d6e77f)

## 📈 1. Nossos Dados

### Sobre o Dataset
- **Nome do dataset:** IMDb Filmes
- **Tamanho:** 63249 linhas e 24 colunas
- **Período:** 1960 até 2024

### Principais Informações
- **Tipo de dados:**
- **Informações Básicas do Filme:** id, title, year, duration, MPA, rating, votes, meta_score, description, Movie_Link
- **Dados Financeiros:** budget, opening_weekend_gross, gross_worldwide, gross_us_canada
- **Creditos:** directors, writers, stars
- **Detalhes Extras:** genres, countries_origin, filming_locations, production_companies, languages
- **Prêmios:** awards_content (wins, nominations, Oscars)
- **Informação de lançamento:** release_date
- **Região coberta:** Mundo
- **Fonte original:** Kaggle

## ❓ 2. Nossa Pergunta Principal

**Queremos descobrir:** Como os filmes foram mudando durante os anos

### Por que isso é importante?
Estudar este tema nos ajuda a:
- Entender melhor como os filmes impactam a cultura socio-mundial
- Entender como esses filmes são feitos e pensados em diferentes épocas

### Nossas 5 Perguntas Específicas
1. Quais são os melhores filmes do mundo?
2. Existe alguma década ou ano com mais filmes bem avaliados?
3. Quais são os filmes com maior avaliação ao longo das décadas?
4. Como o orçamento dos filmes evoluiu ao longo do tempo?
5. Quais são os gêneros mais populares em cada década?

## 🔍 3. O Que Descobrimos

---
# Não alterei daqui pra baixo
---

### Fatos Interessantes
1. "Brasília é a cidade mais rica, mas também uma das mais desiguais"
2. "Durante a pandemia em 2020, a desigualdade aumentou em quase todo o país"
3. "No Nordeste, mesmo sendo uma região mais pobre, a desigualdade diminuiu mais que em outras regiões"

### Nossos Gráficos
**Exemplo de Gráfico:** Renda Média por Estado
![Gráfico de Rendimento Médio x Índice de Gini](graficos-PNAD-continua-rendimento-de-todas-as-fontes-2.png)
- O que mostra: Relação entre rendimento médio e índice de Gini por estado

### Problemas Encontrados
- Dados faltantes em alguns períodos para estados específicos, especialmente durante 2020, provavelmente devido à pandemia.
- Dificuldade em normalizar os valores monetários considerando a inflação ao longo do período estudado.

## 🤖 4. Nossos Algoritmos

### Primeiro Algoritmo: Classificação com Árvore de Decisão
**O que faz:** Classifica os estados em grupos de "alta", "média" ou "baixa" desigualdade
**Por que usamos:** Para responder nossa pergunta "Quais estados apresentam os maiores e menores índices de desigualdade de renda?"
**Exemplo de resultado:** 
- Alta desigualdade: Distrito Federal, São Paulo
- Média desigualdade: Minas Gerais, Goiás
- Baixa desigualdade: Santa Catarina, Rio Grande do Sul

### Segundo Algoritmo: Análise de Clusters (K-means)
**O que faz:** Agrupa os estados brasileiros que são parecidos
**Por que usamos:** Para encontrar grupos de estados com características semelhantes
**Exemplo de resultado:** Encontramos 3 grupos de estados:
- Grupo 1: Estados ricos (Sul e Sudeste)
- Grupo 2: Estados de renda média (Centro-Oeste)
- Grupo 3: Estados de menor renda (Norte e Nordeste)

## 📋 5. Próximos Passos
1. Aprofundar a análise temporal para identificar tendências e sazonalidades na desigualdade
2. Incluir mais variáveis socioeconômicas para melhorar o modelo de regressão
3. Refinar a análise de clusters e interpretar as características de cada grupo
4. Criar visualizações interativas para facilitar a apresentação dos resultados

## 👥 6. O Que Cada Um Fez
- **Ana Silva:** Fez os gráficos
- **Bruno Santos:** Organizou os dados
- **Carolina Oliveira:** Escreveu o relatório
- **Daniel Pereira:** Fez as análises

---
**Data de Entrega:** 05/05/2025
**Link do Notebook:** [Cole aqui o link do Google Colab]