import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
dias = pd.read_csv("dias.csv")
viagens = pd.read_csv("viagens.csv")
pd.set_option("display.width", 120) # evita quebrar tabelas largas em várias linhas

def resumo_estatistico(tabela):
 colunas_numericas = tabela.select_dtypes("number")
 resultado = pd.DataFrame({
 "media": colunas_numericas.mean(), "mediana": colunas_numericas.median(),
 "desvio": colunas_numericas.std(),
 "cv_%": colunas_numericas.std() / colunas_numericas.mean() * 100,
 "skew": colunas_numericas.skew(),
 "ausentes_%": tabela[colunas_numericas.columns].isna().mean() * 100,
 }).round(2)
 resultado["alerta"] = np.where(resultado["skew"].abs() > 1, "assimétrica", "")
 return resultado

print(resumo_estatistico(viagens.drop(columns="id_viagem")))
print(resumo_estatistico(dias))

colunas_clima = ["temperatura_c", "sensacao_termica_c", "umidade_pct", "vento_kmh",
"chuva_mm", "alugueis"]
nomes_curtos = {"temperatura_c": "temp", "sensacao_termica_c": "sensacao",
"umidade_pct": "umidade",
 "vento_kmh": "vento", "chuva_mm": "chuva", "alugueis": "alugueis"}
matriz_correlacao = dias[colunas_clima].corr().rename(columns=nomes_curtos,
index=nomes_curtos)
print(matriz_correlacao.round(2))
print("\ncorrelação de cada variável com o alvo:")
print(matriz_correlacao["alugueis"].drop("alugueis").sort_values(key=abs,
ascending=False).round(2))


atributos_clima = dias[[ "temperatura_c" , "sensacao_termica_c" , "umidade_pct" , "vento_kmh" ,
"chuva_mm" ]]
def calcular_vif(atributos):
 vif_por_coluna = {}
 for coluna in atributos.columns:
    demais_colunas = atributos.drop(columns=coluna)
    r_quadrado = LinearRegression().fit(demais_colunas,
    atributos[coluna]).score(demais_colunas, atributos[coluna])
    vif_por_coluna[coluna] = 1 / (1 - r_quadrado)
    return pd.Series(vif_por_coluna). round(1)
print("VIF com as duas temperaturas:\n" , calcular_vif(atributos_clima))
print("\nVIF sem sensacao_termica_c:\n" ,
calcular_vif(atributos_clima.drop(columns= "sensacao_termica_c" )))

