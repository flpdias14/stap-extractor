#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


filename = 'fragmentacao.txt'

file = open(filename, "r") # read the file

day = 0 # day controller

previous_day = '' # controls when the day change

# list to add the processes and ocurrences
days = []
process_names = []
process_ids = []
process_fathers = []
process_father_ids = []
uids = []
ocurrences = []

for register in file: # for each register (line) in file

    if "Mar" in register: # checking if the register has the month tag
        if previous_day != register.split(' ')[2]: # verify if the day changed
            day += 1
            previous_day = register.split(' ')[2]

    if "#" in register: # verify if the register has the stap tag
        days.append(day)

        aux = register.split('/')[0].split('(')

        process_names.append(aux[0])

        if len(aux) == 2:
            process_ids.append(aux[1].replace(')', ''))
        else:
            process_ids.append('')

        aux = register.split('/')[1].replace("Pai: ", "").split('(')
        
        process_fathers.append(aux[0])

        if len(aux) == 2:
            process_father_ids.append(aux[1].replace(')', ''))
        else:
            process_father_ids.append('')

        uids.append(register.split('/')[2].replace("UID: ", "").split('#')[0])

        if len(register.split('/')[2].replace("UID: ", "").split('#')) == 2:
            ocurrences.append(register.split('/')[2].replace("UID: ", "").split('#')[1].replace(",\n", ""))
        else:
             ocurrences.append(0)
print(" days: {}, process: {}, processid: {}, father: {}, fatherid: {}, uid: {}, ocurrences: {} ".format(len(days), len(process_names), len(process_ids), len(process_fathers), len(process_father_ids), len(uids), len(ocurrences)))

# dictionary of lists  
dict = {'day': days, 'process': process_names, 'process_id': process_ids, 'father': process_fathers, 'father_id': process_father_ids, 'uid': uids, 'ocurrences': ocurrences}



# cria um dataframe com os dados
df = pd.DataFrame(dict)

df.to_csv("pre_processed_"+filename.replace('txt', 'csv'))

df['ocurrences'] = pd.to_numeric(df['ocurrences'])


groupby_process =  df.groupby(['day','process'], as_index=False)['ocurrences'].agg(['count', 'min', 'mean', 'max', 'sum']).sort_values(['day', 'sum'], ascending=[True, False])
# groupby_process = groupby_process.sort_values('sum', ascending=False)
# # groupby_process =  df.groupby('process')
groupby_process.to_csv("processed_groupby_day_and_process_"+filename.replace(".txt", ".csv"))
# # net =  groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# # net.ocurences.astype(int)
# # print net.dtypes()
# list_process = []
# list_ocurences = []
# # for process, process_df in groupby_process:
# #     list_process.append(process)
# #     list_ocurences.append(process_df[process_df['process']==process]['ocurences'].sum())
# # f = groupby_process.get_group('NetworkManager(402)/Pai: systemd(1)/UID: 0')
# # print f.ocurences.sum()

# # print list_process[0:5]
# # print list_ocurences[0:5]


# # print df.head()