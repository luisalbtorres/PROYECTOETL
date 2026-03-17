import pandas as pd
import matplotlib.pyplot as plt
import seaborn as np
import streamlit as st

def transford_data(data_df1, data_df2, data_df3, data_df4):

    print("Transformacion de datos")

    #Analisis exploratorio de los datos
    #Estadistica descriptiva
    #Pre-visualizacion de los datos

    print("Informacion basica datasset cancer mama 2022:",flush=True)
    print(data_df1.info()) # Info permite hacer un resumen
    print(data_df1.columns)
    print(data_df1.head())
    print("Estadistica descriptiva datasset cancer mama 2022:",flush=True)
    print(data_df1.describe())
    plt.figure(figsize=(10,6))
    plt.subplot(1,4,1)
    plt.hist(data_df1['edad_'],bins=20, color='green', alpha=0.7)
    plt.xlabel('EDAD')
    plt.ylabel('NUMERO PERSONAS DIAGNOSTICADAS')
    plt.title('DISTRIBUCION POR EDAD DE \n PACIENTES DIAGNOSTICADOS \n 2022', fontsize=7)
    plt.grid()
    plt.tight_layout()

    print("Informacion basica datasset cancer mama 2021:",flush=True)
    print(data_df2.info())
    print(data_df2.columns)
    print(data_df2.head())
    print("Estadistica descriptiva datasset cancer mama 2021:",flush=True)
    print(data_df2.describe())
    plt.subplot(1,4,2)
    plt.hist(data_df2['edad'],bins=20, color='green', alpha=0.7)
    plt.xlabel('EDAD')
    plt.ylabel('NUMERO PERSONAS DIAGNOSTICADAS')
    plt.title('DISTRIBUCION POR EDAD DE \n PACIENTES DIAGNOSTICADOS \n 2021', fontsize=7)
    plt.grid()
    plt.tight_layout()

    print("Informacion basica datasset cancer mama 2023:",flush=True)
    print(data_df3.info())
    print(data_df3.columns)
    print(data_df3.head())
    print("Estadistica descriptiva datasset cancer mama 2023:",flush=True)
    print(data_df3.describe())
    plt.subplot(1,4,3)
    plt.hist(data_df3['edad_'],bins=20, color='green', alpha=0.7)
    plt.xlabel('EDAD')
    plt.ylabel('NUMERO PERSONAS DIAGNOSTICADAS')
    plt.title('DISTRIBUCION POR EDAD DE \n PACIENTES DIAGNOSTICADOS \n 2023', fontsize=7)
    plt.grid()
    plt.tight_layout()

    print("Informacion basica datasset Hospital:",flush=True)
    print(data_df4.info())
    print(data_df4.columns)
    print(data_df4.head())
    print("Estadistica descriptiva datasset Hospital:",flush=True)
    print(data_df3.describe())
    plt.subplot(1,4,4)
    plt.hist(data_df4['edad'],bins=20, color='green', alpha=0.7)
    plt.xlabel('EDAD')
    plt.ylabel('NUMERO PERSONAS DIAGNOSTICADAS')
    plt.title('DISTRIBUCION POR EDAD DE \n PACIENTES DIAGNOSTICADOS \n 2022HOSPITAL', fontsize=7)
    plt.grid()
    plt.tight_layout()
    #plt.show()
    plt.savefig("grafica_edades.png")
    plt.close()


#Limpieza de datos


    print("Detectar nulos y duplicados")
    print("nulos en data_df1")
    print(data_df1.isnull().sum())
    print("Duplicados en data_df1")
    print(data_df1.duplicated().sum())

    print("nulos en data_df2")
    print(data_df2.isnull().sum())
    print("Duplicados en data_df2")
    print(data_df2.duplicated().sum())

    print("nulos en data_df3")
    print(data_df3.isnull().sum())
    print("Duplicados en data_df3")
    print(data_df3.duplicated().sum())

    print("nulos en data_df4")
    print(data_df4.isnull().sum())
    print("Duplicados en data_df4")
    print(data_df4.duplicated().sum())

    data_df1['res_biops9'].fillna('np.nan', inplace=True)
    data_df1['tip_ss_'].fillna('np.nan', inplace=True)
    data_df1['grad_histo'].fillna('np.nan', inplace=True)
    print(data_df1.isnull().sum())
    

    data_df3['res_biops9'].fillna('np.nan', inplace=True)
    data_df3['per_etn_'].fillna('np.Gitano', inplace=True)
    print(data_df3.isnull().sum())

    
    Lista_codigos = ['C501', 'C502', 'C503', 'C504', 'C505', 'C506', 'C507', 'C508', 'C509', 'D056', 'D057', 'D486']
    df_mama = data_df4[data_df4["var017"].isin(Lista_codigos)]
    print(df_mama)




    

    
    

