#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


filename = '/home/felipe/Área de trabalho/resultados docker final/com networkmanager/felipe/stap-networkmanager.txt'

# cria um dataframe com os dados
df = pd.read_csv(filename, sep="\n", header=None)

# adiciona o nome da coluna
df.columns = ['process']

df_filtered =  df[df.process.str.contains('#')]


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
# groupby_process =  df.groupby('process')
print groupby_process
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