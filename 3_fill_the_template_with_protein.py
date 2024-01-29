#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:00:16 2023

@author: tanda
"""

import os
import csv

os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")


output_path = "./Input_file/3_gene_filled/"
if not os.path.exists(output_path):
        os.makedirs(output_path)


for plate_number in range(1,19):
    remain_number=0
    template_file = "./Input_file/2_New_coordinates/New_coordinates_added_plate"+str(plate_number)+".csv"
    input_file = "./Input_file/1_merged_3_plates/Merged_plates_No"+str(plate_number)+".csv"
    output_file = output_path+"Gene_filled_plate_No"+str(plate_number)+".csv"
    
    template_data = []
    with open(template_file, "r") as template:
        reader = csv.reader(template)
        header = next(reader)     
        template_data = list(reader)
    
    # Read the input file
    input_data = []
    with open(input_file, "r") as input_csv:
        reader = csv.reader(input_csv)
        next(reader)  # Skip the header
        input_data = list(reader)
    
    # Fill the template with input data
    output_data = []
    template_row_index = 0
    input_row_index = 0
    for input_row in input_data:        
        while template_data[template_row_index][0]:
            output_data.append(template_data[template_row_index])
            template_row_index += 1  # Find the first empty row in the template
            continue      
        template_data[template_row_index][:4] = input_row[:4]  # Fill the first four columns with input data
        print(input_row_index,template_row_index)
        output_data.append(template_data[template_row_index])
        input_row_index += 1
        template_row_index += 1
    remain_nummber=384-template_row_index
    for i in range(0,remain_nummber):
        output_data.append(template_data[template_row_index])
        template_row_index += 1
        i +=1
        
    
    # Write the output file
    with open(output_file, "w", newline="") as output:       
        writer = csv.writer(output)
        writer.writerow(header)
        writer.writerows(output_data)
