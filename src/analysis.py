import matplotlib.pyplot as plt


def get_top10_latest_year(df):
    ultimo_ano = df["year"].max()

    top10 = (
        df[df["year"] == ultimo_ano]
        .sort_values(by="happiness_score", ascending=False)
        .head(10)
    )

    return ultimo_ano, top10


def filter_top_countries(df, top_countries):
    df_filtered = df[df["country"].isin(top_countries)]
    return df_filtered.sort_values(by=["country", "year"])


def plot_top10_evolution(df, top_countries):
    plt.figure(figsize=(10, 6))

    # garantir ordenação
    df = df.sort_values(by=["year"])

    # anos únicos ordenados (CORREÇÃO PRINCIPAL)
    years = sorted(df["year"].unique())

    for country in top_countries:
        df_country = df[df["country"] == country]

        plt.plot(
            df_country["year"],
            df_country["happiness_score"],
            marker='o',
            label=country
        )

    # 👇 garante anos claros no eixo X
    plt.xticks(years, rotation=45)

    plt.title("Evolução da felicidade - Top 10 países")
    plt.xlabel("Ano")
    plt.ylabel("Happiness Score")

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid()
    plt.tight_layout()

    # salvar imagem
    plt.savefig("top10_evolution.png")

    plt.show()


def run_top10_analysis(df):
    ultimo_ano, top10 = get_top10_latest_year(df)

    print(f"\nTop 10 países mais felizes em {ultimo_ano}:")
    print(top10[["country", "happiness_score"]])

    top_countries = top10["country"].tolist()

    df_top = filter_top_countries(df, top_countries)

    plot_top10_evolution(df_top, top_countries)