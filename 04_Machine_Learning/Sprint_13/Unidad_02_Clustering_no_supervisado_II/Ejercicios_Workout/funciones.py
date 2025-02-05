
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Defino funcion para calcular y monitorar la cantidad de valores nulos por columna
def Calcular_missing(df):
    print("\nCantidad de valores nulos y porcentaje por columna:")
    df_missing = df.isna().sum()
    df_missing_percent = (df.isna().sum()/len(df)) *100
    missing = pd.DataFrame({
        'Valores totales': df.count(),
        'Tipo' : df.dtypes,
        'Valores faltantes': df_missing,
        'Porcentaje faltante (%)': df_missing_percent
        })
    return missing


#FUNCION que me devuelve un DF con cardinalidades, % variación cardinalidad, y tipos
# Primero dividir las variables por tipo
def card_tipo(df,umbral_categoria = 20, umbral_continua = 30):
    # Primera parte: Preparo el dataset con cardinalidades, % variación cardinalidad, y tipos
    df_temp = pd.DataFrame([df.nunique(), df.nunique()/len(df) * 100, df.dtypes]) # Cardinaliad y porcentaje de variación de cardinalidad
    df_temp = df_temp.T # Como nos da los valores de las columnas en columnas, y quiero que estas sean filas, la traspongo
    df_temp = df_temp.rename(columns = {0: "Card", 1: "%_Card", 2:"Tipo"}) 
    # Cambio el nombre de la transposición anterior para que tengan más sentido, y uso asignación en vez de inplace = True (esto es arbitrario para el tamaño de este dataset)

    # Corrección para cuando solo tengo un valor
    df_temp.loc[df_temp.Card == 1, "%_Card"] = 0.00

    # Creo la columna de sugerencia de tipo de variable, empiezo considerando todas categóricas pero podría haber empezado por cualquiera, siempre que adapte los filtros siguientes de forma correspondiente
    df_temp["tipo_sugerido"] = "Categorica"
    df_temp.loc[df_temp["Card"] == 2, "tipo_sugerido"] = "Binaria"
    df_temp.loc[df_temp["Card"] >= umbral_categoria, "tipo_sugerido"] = "Numerica discreta"
    df_temp.loc[df_temp["%_Card"] >= umbral_continua, "tipo_sugerido"] = "Numerica continua"

    return df_temp


# FUNCION para conversion de campo fecha str en float
def str_to_float(row):
    if '-' in row:
        row = np.nan
    else:
        row = float(row)
    return row


#funcion que calcula el IQR
def get_IQR(df, col):
    return df[col].quantile(0.75) - df[col].quantile(0.25)


#Calculo Variabiidad
def variabilidad(df):
    df_var = df.describe().loc[["std","mean"]].T
    #llamo al describe y 
    # creo una nueva columna con el coef de Variacion =std/mean
    df_var["Coef_Var"] = df_var["std"]/df_var["mean"]
    return df_var