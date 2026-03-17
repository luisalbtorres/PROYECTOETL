from extract import extract
from transform import transford_data
from load import load

def main():
    df1, df2, df3, df4 = extract()

    #print(df1.head())
    #print(df2.head())
    #print(df3.head())
    #print(df4.head())
    datos_limpios = transford_data(df1, df2, df3, df4)


if __name__ == "__main__":
    main()