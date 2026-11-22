 Classificação das variáveis:

1- temperatura_c - apresentou p < 0,05, w = 0,973, skew = -0,03 e curtose = -1,03 
    Não apresenta distribuição normal, mas simétrica. Apresenta um achatamento central e poucos outliers.
    Indicaria somente a StandardScaler

2- alugueis - apresenta p = 0,049, w = 0,96, skew = 0,03 e curtose - -0,34 
    Distribuição próxima da normal e simétrica. Indicaria somente a StandardScaler

3- umidade - apresenta p = 0,14, w = 0,997, skew = 0,08 e curtose - -0,07
    Distribuição normal e simétrica. Indicaria somente a StandardScaler

4- chuva -  apresentou p < 0,05, w = 0,28, skew = 5,74 e curtose = 38,48 
    Não apresenta distribuição normal e é fortemente assimétrica a direita. 
    Indicaria Logaritmo com deslocamento (np.log1p)

5- vento - chuva -  apresentou p < 0,05, w = 0,899, skew = 1,53 e curtose = 3,84 
    Não apresenta distribuição normal e é fmoderadamente assimétrica a direita. 
    Indicaria Logaritmo (np.log1p) (ou PowerTransformer / Yeo-Johnson).
