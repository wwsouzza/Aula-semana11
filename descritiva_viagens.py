import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use( "Agg")
dias = pd.read_csv( "dias.csv" , parse_dates=[ "data"])
viagens = pd.read_csv( "viagens.csv" )

print("--- 3 primeiras linhas de dias ---")
print(dias.head(3))

print("\n--- 3 primeiras linhas de viagens ---")
print(viagens.head(3))

print(dias[["temperatura_c" , "chuva_mm", "alugueis"]].describe(). round(2))
print(dias[["chuva_mm", "alugueis"]].agg(["mean", "median", "std"]).round(2))

print(viagens[["distancia_km" , "duracao_min", "valor_rs"]].describe().round(2))
print(viagens[["distancia_km" , "duracao_min", "valor_rs"]].agg(["mean", "median", "std"]).round(2))

dias["fim_semana"] = dias["dia_semana"] >= 5
print(dias.groupby("fim_semana")["alugueis"].agg(["count", "mean", "median", "std"]).round(1))
print(viagens.groupby("bicicleta")["duracao_min"].agg(["mean", "median", "std"]).round(1))


duracoes = viagens["duracao_min"]

primeiro_quartil_duracao, terceiro_quartil_duracao = duracoes.quantile([0.25, 0.75])
limite_superior = terceiro_quartil_duracao + 1.5 * (terceiro_quartil_duracao - primeiro_quartil_duracao)
viagens_atipicas = viagens[duracoes > limite_superior]

print(
    f"limite superior = {limite_superior:.1f} min | viagens acima: "
    f"{len(viagens_atipicas)} ({len(viagens_atipicas)/len(viagens):.1%})"
)
print(f"maior duração = {duracoes.max():.0f} min ({duracoes.max()/60:.1f} h)")
duracoes_sem_atipicas = duracoes[duracoes <= limite_superior]
print("média sem os outliers:", round(duracoes_sem_atipicas.mean(), 1), "| mediana sem:", round(duracoes_sem_atipicas.median(), 1)
)

for tipo in ["comum", "eletrica"]:
  grupo = viagens[viagens["bicicleta"] == tipo]["duracao_min"]
  q1, q3 = grupo.quantile([0.25, 0.75])
  limite_sup = q3 + 1.5 * (q3 - q1)
  outliers = grupo[grupo > limite_sup]
  print(
      f"{tipo.capitalize()}: limite = {limite_sup:.1f} min | outliers ="
      f" {len(outliers)} ({len(outliers)/len(grupo):.1%})"
  )


