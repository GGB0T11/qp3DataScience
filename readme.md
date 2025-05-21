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

### Fatos Interessantes
1. O gênero "Drama" foi o mais popular em todas as décadas desde 1960.
2. A duração média dos filmes aumentou nas décadas de 1980 e 2000, mas vem diminuindo desde 2010.
3. Os filmes com maior nota média tendem a ter diretores premiados e orçamentos maiores.

### Nossos Gráficos
**Gráfico:** Gráfico de Quantidade de Filmes X Décadas
![Gráfico de Quantidade de Filmes X Décadas](FimesDecada.png)

- O que mostra: Quantidades de filmes por década

### Problemas Encontrados
- Colunas: **opening_weekend_gross**, **gross_us_canada**, **gross_us_canada** e **meta_score** tinham **67%** ou mais de dados ausentes, por isso as respectivas colunas não foram analizadas

### 🤖 4. Nossos Algoritmos

### Primeiro Algoritmo: Agrupamento de Gêneros com K-Means
**O que faz:** Agrupa os gêneros de filmes em grupos parecidos com base em variáveis como nota média (rating), duração média e quantidade de votos
**Por que usamos:** Para entender melhor quais gêneros são mais populares, bem avaliados ou longos. Isso nos ajuda a ver padrões de produção e preferências ao longo do tempo
**Exemplo de resultado:** Gêneros como Ação e Aventura ficaram no mesmo grupo por serem populares, enquanto Documentário e Drama foram agrupados juntos por terem duração maior e avaliação mais alta

### Segundo Algoritmo: Cálculo de Quantidade de filmes com Pandas
**O que faz:** Calcula a quantidade de filmes a cada década usando a biblioteca pandas
**Por que usamos:** Para descobrir se há algum padrão na quantidade de filmes por década
**Exemplo de resultado:** As décadas tem uma quantidade de filmes que varia de 5799 a 6002

## 📋 5. Próximos Passos
1. Aprofundar a análise de gêneros para entender melhor a relação entre popularidade, avaliação e duração dos filmes ao longo do tempo
2. Comparar a avaliação do público (rating) com a avaliação da crítica (meta_score), identificando possíveis divergências por década ou gênero
3. Analisar a representatividade geográfica, verificando como países de origem e idiomas influenciam na produção de filmes mais bem avaliados
4. Estudar a evolução dos orçamentos e lucros, ajustando os valores pela inflação para entender as mudanças reais nos investimentos da indústria do cinema
5. Aplicar algoritmos de agrupamento (como K-Means) para identificar perfis de filmes com base em múltiplas variáveis (gênero, duração, orçamento, nota, etc.)


## 👥 6. O Que Cada Um Fez
- **Gustavo Freitas:** Carregou o time nas costas
- **José Pedro Bueno:** Relatorio
- **Sofia Vicente:** Nada
- **Acauã Barros:** Nada
- **Orlando Alguma Coisa:** Nada
---
**Data de Entrega:** 05/05/2025
**Link do Notebook:** [Cole aqui o link do Google Colab]