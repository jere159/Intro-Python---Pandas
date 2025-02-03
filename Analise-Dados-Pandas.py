import pandas as pandas #Importanto biblioteca
df = pd.read_csv("caminho do arquivo", error_bad_lines=False, sep=";") #Ler arquivo
df.head() #Visualiza 5 primeiras linhas
df.rename(colums={"country":"Pais", "continent":"continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})
df.head(10) #Visualiza 10 primeiras linhas
df.shape #Total de linhas e colunas
df.columns #Colunas
df.dtypes #Tipos de variáveis
df.tail() #Ultimas linhas
df.describe() #Média, desvio padrão, min, max, quartis
df["continente"].unique() #Verificar valores da coluna
Oceania = df.loc[df["continente"] == "Oceania"]
Oceania.head()
df.groupby("continente")["Pais"].unique()
df.groupby("Ano")["Expectativa de vida"].mean()
df["PIB"].mean()
