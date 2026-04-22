import sqlite3


def load_data(df):
    conn = sqlite3.connect("happiness.db")
    df.to_sql("happiness", conn, if_exists="replace", index=False)
    conn.close()

    print("Dados carregados no banco com sucesso!")