df["Data"] = df["Data"].astype("int64") #Transformando a coluna de data em tipo inteiro
df.dtypes #Verifica o tipo de dado
df["Data"] = pd.to_datetime(df["Data"]) #Transformando coluna de data em data
df.groupby(df["Data"].dt.year)["Receita"].sum() #Agrupamento por ano
df["Ano_venda"] = df["Data"].dt.year #Criar nova coluna
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day) #Extraindo mes e o dia
df.sample(5)
df["Data"].min() #Retornando a data mais antiga
df["diferenca_dias"] = df["Data"] - df["Data"].min() #Calculando a diferença de dias
df["trimestre_venda"] = df["Data"].dt.quarter #Cria coluna de trimestre
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)] #Filtrando as vendas de 2019 do mês de março

