import pandas as pd


def transform_data(dfs):
    processed = []

    for df in dfs:
        # padronizar colunas
        df.columns = df.columns.str.lower().str.replace(" ", "_")

        # renomear país
        if "country_or_region" in df.columns:
            df = df.rename(columns={"country_or_region": "country"})

        # padronizar score
        if "score" in df.columns:
            df = df.rename(columns={"score": "happiness_score"})
        else:
            for col in df.columns:
                if "score" in col:
                    df = df.rename(columns={col: "happiness_score"})

        # remover nulos
        df = df.dropna(subset=["happiness_score"])

        # extrair ano
        year = df["source_file"].iloc[0][:4]
        if year.isdigit():
            df["year"] = int(year)
        else:
            continue

        # selecionar colunas finais
        df = df[["country", "happiness_score", "year"]]

        processed.append(df)

    df_final = pd.concat(processed, ignore_index=True)

    return df_final