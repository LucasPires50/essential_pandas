import pandas as pd

# Carregar dataset no formato csv
data = pd.read_csv('./datasets/GasPricesinBrazil_2004-2019.csv', sep=';')

# Retorna as 5 primeiras linhas do dataset ou dataframe, por padrão
first_5_lines = data.head()
# Para mais linhas, adicionar a quantidade de linhas no valor da função
more_lines = data.head(10)

# Informações gerais do dataser
# general_information = data.info()

# Acessar as dimensões ou forma do Data Frame(nº de linhas x nº de colunas)
dimensions = data.shape
# print(f'O DataFrame possui {dimensions[0]} linhas/registros e {dimensions[1]} colunas/atributos/variáveis.')

# Criar um dataframe a partir de um dicionário
new_dataframe = pd.DataFrame({
    'nome': ['Ailton', 'Marcos', 'Lucas'],
    'idade': [16, 1000, 70],
    'peso': [70, 15, 60],
    'eh jedi': [True, True, True],
})

# Retorna uma lista com o nome das colunas do dataframe
columns_dataframe = new_dataframe.columns
# Converter para lista
list_columns = list(columns_dataframe)
print(list_columns)

# Renomear colunas, o método abaixo irá retorna uma cópia do dataframe com as colunas renomeadas
rename_columns = new_dataframe.rename(columns={
    'nome':'nome completo',
    'idade':'idade da pessoa',
})
# Renomear as colunas do proprio dataframe, sem gerar uma nova cópia
rename_columns_inplace = new_dataframe.rename(columns={
    'nome':'nome completo',
    'idade':'idade da pessoa',
}, inplace=True)
# Renomar todas as colunas do dataframe passando uma lista
new_dataframe.columns = ['NOME', 'IDADE', 'PESO', 'JEDI']

print(new_dataframe)
