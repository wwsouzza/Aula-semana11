import pandas as pd
import numpy as np
import matplotlib
matplotlib.use( "Agg")
import matplotlib.pyplot as plt
import seaborn as sns


from scipy import stats
dias = pd.read_csv( "dias.csv" )
viagens = pd.read_csv( "viagens.csv" )
alugueis_por_dia = dias[ "alugueis" ]
duracoes = viagens[ "duracao_min" ]
umidade = dias["umidade_pct"]
vento = dias["vento_kmh"]
temperatura = dias["temperatura_c"]
chuva = dias["chuva_mm"]


for nome_coluna, serie in [("alugueis", alugueis_por_dia), ( "temperatura_c" ,
temperatura), ("umidade" , umidade),  ( "chuva_mm", chuva), ("vento" , vento)]:
 print(f"{nome_coluna:14s} skew={serie.skew():6.2f} curtose={serie.kurt():6.2f}" )

for nome_coluna, amostra in [("alugueis", alugueis_por_dia), ( "temperatura_c" ,
temperatura), ("umidade" , umidade),  ( "chuva_mm", chuva), ("vento" , vento)]:
 estatistica_w, p_valor = stats.shapiro(amostra)
 print(f"{nome_coluna:12s} W={estatistica_w:.3f} p={p_valor:.4g} ->" ,
 "compatível com normal" if p_valor > 0.05 else "NÃO normal")

 figura, eixos = plt.subplots( 2, 3, figsize=( 13, 7))

sns.histplot(alugueis_por_dia, kde= True, ax=eixos[ 0, 0], color="#3FB950"); eixos[0,
0].set_title( "Aluguéis/dia" )
sns.histplot(temperatura, kde= True, ax=eixos[ 0, 1], color="#3FB950"); eixos[0,
1].set_title( "temperatura" )
sns.histplot(umidade, kde= True, ax=eixos[ 0, 2], color="#3FB950"); eixos[0,
2].set_title( "umidade" )
sns.histplot(chuva, bins=30, ax=eixos[1, 0], color="#3FB950")
eixos[1, 0].set_title("Chuva (assimétrica à direita)")
sns.histplot(vento, kde= True, ax=eixos[ 1, 1], color="#3FB950"); eixos[1,
1].set_title( "vento" )
plt.tight_layout(); plt.savefig( "figuras/a2_distribuicoes.png" , dpi=110)

figura, eixos = plt.subplots(2, 3, figsize=(13, 7))

stats.probplot(alugueis_por_dia, dist= "norm", plot=eixos[ 0, 0]); eixos[ 0, 0].set_title("QQ-plot aluguéis")
stats.probplot(temperatura, dist= "norm", plot=eixos[ 0, 1]); eixos[ 0, 1].set_title( "QQ-plot temperatura")
stats.probplot(umidade, dist= "norm", plot=eixos[ 0, 2]); eixos[ 0, 2].set_title( "QQ-plot umidade")
stats.probplot(chuva, dist= "norm", plot=eixos[ 1, 0]); eixos[ 1, 0].set_title( "QQ-plot chuva" )
stats.probplot(vento, dist= "norm", plot=eixos[ 1, 1]); eixos[ 1, 1].set_title( "QQ-plot vento")
plt.tight_layout(); plt.savefig( "figuras/a3_distribuicoes.png" , dpi=110)

