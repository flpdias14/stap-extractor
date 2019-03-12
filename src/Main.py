#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


filename = '/home/felipe/Área de trabalho/resultados docker final/com networkmanager/felipe/stap-networkmanager.txt'

# cria um dataframe com os dados
df = pd.read_csv(filename, sep="\n", header=None)

# adiciona o nome da coluna
df.columns = ['process']
df['index'] = df.index
# print df.iloc[21278:21282, 0]

df_filtered =  df[df.process.str.contains('#')]

# df_filtered = df_filtered[df_filtered.process.str.contains(',P')]

def filtrar_data_frame():
    indexes =  df_filtered.index
    ranges = len(indexes)
    for i in xrange(ranges):
        if i+1 >= ranges:
            break 
        diff = indexes[i+1] -indexes[i];
        if diff > 1:
            print df.iloc[i:i+diff, 0]
 

registers = df_filtered['process'].str.replace('[\[\]]', '').str.split(',');

separated_process = []
for register in registers:
    register.remove(register[0])
    for r in register:
        separated_process.append(r)
        
separated_process = pd.Series(separated_process).str.split('#')

df['process'] = separated_process.str.get(0)
df['ocurences'] = separated_process.str.get(1).astype(float)
signatures= df['process'].unique()

# print df[df['process'].str.contains('NetworkManager')]['ocurences'].head().sum(axis=1)

groupby_process =  df.groupby('process', as_index=False)['ocurences'].agg(['count', 'min', 'mean', 'max', 'sum'])
groupby_process = groupby_process.sort_values('sum', ascending=False)
#groupby_process =  df.groupby('process')
print groupby_process.head(5)
# net =  groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# net.ocurences.astype(int)
# print net.dtypes()
list_process = []
list_ocurences = []
# for process, process_df in groupby_process:
#     list_process.append(process)
#     list_ocurences.append(process_df[process_df['process']==process]['ocurences'].sum())
# f = groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# print f.ocurences.sum()

# print list_process[0:5]
# print list_ocurences[0:5]


# print df.head()