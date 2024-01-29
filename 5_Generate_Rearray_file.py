#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:45:51 2023

@author: tanda
"""

import os
import csv

#Things you need to change when you use
os.chdir("your/working/directory")


output_path = "./Input_file/6_Rearray_file/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
  
        
  
print("How many plates you have in ./Input_file/1_merged_plates/?")
your_plate_number = input()

for plate_number in range(1,int(your_plate_number)+1):
    
    input_file = "./Input_file/5_Rest_filled/Rest_filled_plate_No"+str(plate_number)+".csv"
    output_file = output_path+"Rearray_file_plate_No"+str(plate_number)+".csv"
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        next(reader)  # Read and save the header
        unique_elements = []  # 存储唯一的元素
        for row in reader:
            if len(row) >= 2:  # 检查第二列是否存在
                element = row[1]  # 提取第二列的元素
                if element not in unique_elements:  # 如果元素不在列表中，则添加到列表
                    unique_elements.append(element)
        for i in unique_elements:
            if i != "":
                writer.writerow([i,"SBS","96","Source"])
        writer.writerow(["Target_Plate"+str(plate_number), "SBS","384","Target"])

        infile.seek(0)  # 将文件指针重置到文件开头
        next(reader)  # 跳过标题行
        for row in reader:
            writer.writerow([row[1], row[2], row[3], "Target_Plate" + str(plate_number), row[4], row[5]])
            
    #break