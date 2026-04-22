from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.analysis import run_top10_analysis


def main():
    dfs = extract_data()
    df_final = transform_data(dfs)
    load_data(df_final)

    # análise
    run_top10_analysis(df_final)


if __name__ == "__main__":
    main()