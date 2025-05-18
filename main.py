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
    bins = range(df['year'].min(), df['year'].max() + 5, 5)
    labels = [f'{start}-{start+4}' for start in bins[:-1]]
    
    # Agrupar por década
    df['decade'] = pd.cut(df['year'], bins=bins, labels=labels, right=False)
    count = df['decade'].value_counts().sort_index()
    
    return count.reset_index()

# Lendo o dataset
df = pd.read_csv("imdb_filmes.csv")

fpm = films_per_decade(df)
print(fpm)
# fpm.to_csv("analises_raw/fpm.csv", index=False)