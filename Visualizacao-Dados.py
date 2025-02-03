df["LojaID"].value_counts(ascending=False)
df["LojaID"].value_counts(ascending=False).plot.bar() #Gráfico de Barras
df["LojaID"].value_counts(ascending=True).plot.barh() #Gráfico de Barras Horizontais
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie() #Gráfico de Pizza
df["Cidade"].value_counts() #Total vendas por cidade

#Adicionando um título e alterando o nome dos eixos
import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title= "Total vendas por cidade")
plt.xlabel("Cidade")
plt.ylabel("Total vendas");

#Alterando a cor
df["Cidade"].value_counts().plot.bar(title= "Total vendas por cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total vendas");

#Alterando o estilo
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos por mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos vendidos")
plt.legend()

df.groupby(df["mes_venda"])["Qtde"].sum() #Quantidade de produtos vendidos no mes

df_2019 = df(df["Ano_venda]"] == 2019) #Filtro/ Seleciona apenas as vendas de 2019

#Total de produtos vendidos por mês/ adiciona marcador
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.xlabel("mês")
plt.ylabel("Total Produtos vendidos")
plt.legend()

plt.hist(df["Qtde"], color="magenta") #Cria um Histograma

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]) #Cria gráfico de dispersão

#Salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("mês")
plt.ylabel("total produtos vendidos")
plt.legend()
plt.savefig("gráfico QTde x MES.png")




