import pandas as pd
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df1.head()
df = pd.concat([df1, df2, df3, df4, df5]) #Junta os arquivos
df.tail()
df.sample() #Amostra
df.dtypes()
df["LojaID"] = df["LojaID"].astype("object") #Altera tipo de dado
df.isnull().sum() #Consulta linhas com valores nulos
df["vendas"].fillna(df["vendas"].mean(), inplace=True) #Substitui valores nulos pela média
df["vendas"].fillna(0, inplace=True) #Substitui valores nulos por zero
df.dropna(inplace=True) #Apagando linhas com valores nulos
df.dropna(subset=["vendas"], inplace=True) #Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(row="all", inplace=True) #Removendo linhas que estejam com valores faltantes em todas as colunas

df["Receita"] = df["vendas"].mul(df["Qtde"]) #Criar coluna
df["Receita/vendas"] = df["Receita"]/df["vendas"]
df["Receita"].max()
df["Receita"].min()
df.nlargest(3, "Receita")
df.nsmallest(3, "Receita")
df.groupby("Cidade")["Receita"].sum()
df.sort_values("Receita", ascending=False).head(10) #Ordenando conjunto de dados