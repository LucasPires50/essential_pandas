import pandas as pd

# Carregar dataset no formato csv
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

# Retorna as 5 primeiras linhas do dataset ou dataframe, por padrão
first_5_lines = data.head()
# Para mais linhas, adicionar a quantidade de linhas no valor da função
more_lines = data.head(10)

# Informações gerais do dataser
general_information = data.info()

print(general_information)