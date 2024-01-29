#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:37:50 2023

@author: tanda
"""
import pandas as pd
import os

os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")


# 读取.xlsx文件
input_file = "./Input_file/mat_a_collection_for_python.xlsx"
df = pd.read_excel(input_file)
output_path = "./Input_file/0_seperated_source_file/"
if not os.path.exists(output_path):
        os.makedirs(output_path)

# 根据第五列的数字拆分成多个文件
groups = df.groupby(df.columns[1])

rows=0
i=0 
lines=0
# 遍历每个分组，输出为新的.csv文件
for group_name, group_data in groups:
    output_file = f"./Input_file/0_seperated_source_file/protein_collection_plate{int(group_name)}.csv"
    #print(output_file)
    print(len(group_data))
    group_data.to_csv(output_file, index=False)
    rows=rows+len(group_data)
    i=i+1
lines=rows-i
print(lines,rows,i)
