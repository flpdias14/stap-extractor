#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


def separar_processos(processo=''):
    retorno = []
    try:
        retorno = processo.split(',P:')
    except:
        print processo
    return retorno

def separar_quantidades(quantidades, separador):
    return quantidades.split(separador)[1].split(',P')[0].split(',')

filename = '/home/felipe/Área de trabalho/resultados docker final/com networkmanager/felipe/stap-networkmanager.txt'

# cria um dataframe com os dados
df = pd.read_csv(filename, sep="\n", header=None)

# adiciona o nome da coluna
df.columns = ['process']
df['index'] = df.index
# print df.iloc[21278:21282, 0]

df_filtered_jan =  df[df.process.str.contains('  ')]
df_filtered_dec =  df[df.process.str.contains('2018,')]
# df =  df[df.process.str.contains(',P')]

# df_filtered = df_filtered[df_filtered.process.str.contains(',P')]

# def filtrar_data_frame():
#     indexes =  df_filtered.index
#     ranges = len(indexes)
#     for i in xrange(ranges):
#         if i+1 >= ranges:
#             break 
#         diff = indexes[i+1] -indexes[i];
#         if diff > 1:
#             print df.iloc[i:i+diff, 0]
 
# print df_filtered_dec.head(10)
# print df_filtered_jan.head(10)
dado = []
dados = []
count = 0
tempo = 0

matriz = pd.DataFrame(data = None, columns=['processo', 'qtd', 'tempo'])
for index, row in df_filtered_dec.iterrows():
    if (not df.iloc[index-1]['process'].__contains__('2018,')):
        
        if(type(df.iloc[index - 1]['process']) is str):
            processos = separar_processos(df.iloc[index - 1]['process'])
            quantidades = separar_quantidades(df.iloc[index]['process'], '2018,')
            if '' in processos:
                processos.remove('')
            if '' in quantidades:
                quantidades.remove('')
            if(len(processos) != len(quantidades)):
                pass
            else:
                ind = len(quantidades)
                for i in xrange(ind):
                    matriz.loc[count] = [processos[i].split('(')[0], quantidades[i], tempo]
                    count += 1
        else:
            print df.iloc[index - 1]['process']
    else:
        # duplicar registros do ultimo tempo
        df_temp = matriz[matriz['tempo'] == (tempo-1)]
        df_temp.at['tempo'] = tempo
        matriz.append(df_temp, ignore_index=True)
#         print "isso ai", matriz
    tempo +=1       
    
        
#     print index, row['process']

# registers = df_filtered['process'].str.replace('[\[\]]', '').str.split(',');

# print matriz.head(100)

# def separar_processos(registros):
#     """
#     registros: dataframe
#     
#     """
#     separated_process = []
#     for register in registers:
#         register.remove(register[0])
#         for r in register:
#             separated_process.append(r)
#     return separated_process

# separated_process = separar_processos(registers)        
# separated_process = pd.Series(separated_process).str.split('#')
# 
# df['process'] = separated_process.str.get(0)
# df['ocurences'] = separated_process.str.get(1).astype(float)
# signatures= df['process'].unique()

# print df[df['process'].str.contains('NetworkManager')]['ocurences'].head().sum(axis=1)

groupby_process =  matriz.groupby('processo', as_index=False)['qtd'].agg(['count', 'min', 'mean', 'max', 'sum'])
groupby_process = groupby_process.sort_values('sum', ascending=False)
#groupby_process =  df.groupby('process')
print groupby_process.head(5)
# # net =  groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# # net.ocurences.astype(int)
# # print net.dtypes()
# list_process = []
# list_ocurences = []
# for process, process_df in groupby_process:
#     list_process.append(process)
#     list_ocurences.append(process_df[process_df['process']==process]['ocurences'].sum())
# f = groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# print f.ocurences.sum()

# print list_process[0:5]
# print list_ocurences[0:5]


# print df.head()
