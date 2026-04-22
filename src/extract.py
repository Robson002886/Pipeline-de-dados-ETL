import kagglehub
import pandas as pd
import os


def extract_data():
    path = kagglehub.dataset_download("obaidhere/world-happiness-report")

    dfs = []

    for file in os.listdir(path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(path, file))
            df["source_file"] = file
            dfs.append(df)

    return dfs