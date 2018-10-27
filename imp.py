'''Importing Stuff'''

import pandas as pd

'''Inputs da pessoa'''
fileread = input("Qual é o ficheiro que deve ser lido? \n \n")
decisao = input("Gráfico em função do pulso (p), ou em função do tempo (t)? \n \n")


'''Uploading file; file must have two sheets: one with a matrix of pH values per pulse and another with t;
everything should be normalized, starting with t = 0 h'''
xls=('.xls')
file = fileread + xls
xl = pd.ExcelFile(file)
t = xl.parse('t')
pH = xl.parse('pH')
tpulso = xl.parse('tpulso')
