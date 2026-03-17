def load(df):

    df.to_csv("output/datos_procesados.csv", index=False)

    print("Datos cargados correctamente",flush=True)