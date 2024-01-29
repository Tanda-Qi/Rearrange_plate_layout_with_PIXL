#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:15:20 2023

@author: tanda

如果是bord er: A12 or A11
WT:A10 or A9
Blank: 空
Y7092:A1 or A2
"Collection_BY":C1 or C2
"Cai_BY":E1 orE2
"Euro_BY":G1 or G2

"""
import os
import csv
import re
os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")


output_path = "./Input_file/5_Rest_filled/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
        
for plate_number in range(1,10):
    input_file = "./Input_file/4_WT_filled/WT_filled_plate_No"+str(plate_number)+".csv"
    output_file = output_path+"Rest_filled_plate_No"+str(plate_number)+".csv"
    
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)  # Read and save the header
        writer.writerow(header)  # Write the header to the output file
    
        for row in reader:
            if re.search(r'\b' + "Border" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "12"
            if re.search(r'\b' + "WT" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "10"
            if re.search(r'\b' + "Y7092" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "1"
            if re.search(r'\b' + "Collection_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "C"
                row[3] = "1"
            if re.search(r'\b' + "Cai_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "E"
                row[3] = "1"
            if re.search(r'\b' + "Euro_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "G"
                row[3] = "1"
            writer.writerow(row)

for plate_number in range(10,19):
    input_file = "./Input_file/4_WT_filled/WT_filled_plate_No"+str(plate_number)+".csv"
    output_file = output_path+"Rest_filled_plate_No"+str(plate_number)+".csv"
    
    with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)  # Read and save the header
        writer.writerow(header)  # Write the header to the output file
    
        for row in reader:
            if re.search(r'\b' + "Border" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "11"
            if re.search(r'\b' + "WT" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "9"
            if re.search(r'\b' + "Y7092" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "2"
            if re.search(r'\b' + "Collection_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "C"
                row[3] = "2"
            if re.search(r'\b' + "Cai_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "E"
                row[3] = "2"
            if re.search(r'\b' + "Euro_BY" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "G"
                row[3] = "2"
            writer.writerow(row)
