import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

#Função para calcular quantidade de valores nulos nas colunas em %
def calc_nulls(df):
    return ((df.isnull().sum()) / df.shape[0] * 100).round(2)

def films_per_decade(df):
    # Criar intervalos de 10 anos
    last_year = df["year"].max()
    bins = list(range(df["year"].min(), df["year"].max(), 10)) + [last_year]
    labels = [f"{start}-{start+9}" if start+9 < last_year else f"{start}-{last_year}" for start in bins[:-1]]

    # Agrupar por década
    df["decade"] = pd.cut(df["year"], bins=bins, labels=labels, right=False)
    count = df["decade"].value_counts().sort_index()
    return count.reset_index()

def plot_bar(df):
    sns.set_theme(style="whitegrid")
    plt.figsize=(12, 6)
    ax = sns.barplot(data=df, x="decade", y="count", hue="decade", palette="Blues_d")
    for i, row in df.iterrows():
        ax.text(i, row["count"] + 50, row["count"], ha="center", va="bottom", fontsize=9)
    ax.set_title("Quantidade de filmes por Década", fontsize=14)
    ax.set_xlabel("Década")
    ax.set_ylabel("Quantidade de Filmes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/fpd.png")        
    return

# Lendo o dataset
df = pd.read_csv("imdb_filmes.csv")

fpd = films_per_decade(df)
plot_bar(fpd)
