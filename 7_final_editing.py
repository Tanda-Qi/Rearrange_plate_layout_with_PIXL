#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:30:57 2023

@author: tanda
"""

import os
import csv

os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")


output_path = "./Input_file/7_Blank_removed/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
  
        
  
    
for plate_number in range(1,19):
    input_file = "./Input_file/6_Rearray_file/Rearray_file_plate_No"+str(plate_number)+".csv"
    output_file = output_path+"Rearray_file_plate_No"+str(plate_number)+".csv"


    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
    
        for row in reader:
            if len(row) >= 2 and row[1]:  # 检查第二列是否存在且不为空
                converted_row = [int(float(cell)) if cell.replace(".", "", 1).isdigit() else cell for cell in row]
                writer.writerow(converted_row)