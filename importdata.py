import pandas as pd

def read_file(fileread, folha):
    """
    Goal: Make data available in Python from the source;
    Input1: Excel file, with type xls;
    Input2: Name of the sheet in the file passed as Input1;
    Output: pandas.df with raw data
    """

    xls = ('.xls')
    file = fileread + xls
    xl = pd.ExcelFile(file)
    xl = xl.parse(folha)

    return xl

# File do read txt com parametros

def read_txt(fileread = 'user_input.txt'):

    f = open(fileread, 'r')

    fl =f.readlines()
    for x in fl:
        print(x)

    f.close()

    return fl

def parameter_txt(f = read_txt()):

    d = dict()



    for line in range(len(f)):

        if f[line][0] == '.':

            key = f[line]
            key = ''.join(key)
            key = key.replace('.', '')
            key = key.replace('\n', '')
            nom = f[line +1]
            nome = nom.replace('\n', '')
            d[key] = nome

    return d

if __name__ == '__main__':
    H = read_txt()

    print(parameter_txt())




