import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import re
from os import makedirs

# TODO: adicionar comentarios explicando o código

def format_votes(vote):
    multiplyers = {"K": 1000, "M": 1000000}
    if pd.isna(vote):
        return None
    s_vote = str(vote)
    if s_vote[-1] in multiplyers:
        multiply = multiplyers[s_vote[-1]]
        value = s_vote[:-1]
        return int(float(value) * multiply)
    else:
        return int(s_vote)

def format_duration(duration):
    if pd.isna(duration):
        return None
    hours = re.search(r"(\d+)\s*h", duration)
    minutes = re.search(r"(\d+)\s*m", duration)
    time = 0
    if hours:
        time += int(hours.group(1)) * 60
    if minutes:
        time += int(minutes.group(1))
    return time if time > 0 else None

def format_column(column, function):
    column = column.map(function)
    column = column.fillna(int(column.mean()))
    column = column.astype("Int64")

    return column

if __name__ == "__main__":
    df = pd.read_csv("imdb_filmes.csv")
    data = pd.DataFrame()

    # -----> Formatação dos Votos <-----
    data["votes"] = format_column(df["votes"], format_votes)

    # -----> Formatação da Duração <-----
    data["duration"] = format_column(df["duration"], format_duration)

    # -----> Formatação do Rating <-----
    data["rating"] = df["rating"].fillna(df["rating"].mean())

    data_scaled = StandardScaler().fit_transform(data)

    kmeans = KMeans(
    n_clusters=6,
    random_state=42,
    n_init=20,
    )
    kmeans.fit(data_scaled)
