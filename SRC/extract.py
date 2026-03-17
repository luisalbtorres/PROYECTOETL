import pandas as pd

def extract():

    print("Extrayendo datos",flush=True)

    info_df1 = pd.read_csv(r"C:\Users\diego\Desktop\Maestria\Etl\Proyecto\Proyecto\Data\Raw\Cancer-mama-2022.csv",sep=";")
    info_df2 = pd.read_csv(r"C:\Users\diego\Desktop\Maestria\Etl\Proyecto\Proyecto\Data\Raw\Cancer-mama-2021.csv",sep=";")
    info_df3 = pd.read_csv(r"C:\Users\diego\Desktop\Maestria\Etl\Proyecto\Proyecto\Data\Raw\Cancer-mama-2023.csv",sep=";")
    info_df4 = pd.read_csv(r"C:\Users\diego\Desktop\Maestria\Etl\Proyecto\Proyecto\Data\Raw\Hospital.csv",sep=";")

    print("Extrayendo datos correctamente",flush=True)

    return info_df1, info_df2, info_df3, info_df4