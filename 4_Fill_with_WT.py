#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:13:36 2023

@author: tanda
"""

import os
import csv

os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")


output_path = "./Input_file/4_WT_filled/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
WT_list=["Y7092","Collection_BY","Cai_BY","Euro_BY"]


for plate_number in range(1,19):
    input_file = "./Input_file/3_gene_filled/Gene_filled_plate_No"+str(plate_number)+".csv"
    output_file = output_path+"WT_filled_plate_No"+str(plate_number)+".csv"
    

    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)  # Read and save the header
        writer.writerow(header)  # Write the header to the output file
    
        WT_index = 0  # Initialize the letter index
    
        for row in reader:
            if not row[0]:  # Check if the first column is empty
                WT = WT_list[WT_index % len(WT_list)]  # Get the letter based on the letter index
                #print(WT)
                row[0] = WT  # Fill the first column with the letter
                WT_index += 1  # Increment the letter index
            writer.writerow(row)
    #break