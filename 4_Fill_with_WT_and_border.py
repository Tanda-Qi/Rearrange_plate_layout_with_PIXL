#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:13:36 2023

@author: tanda

please prepare a 96 well plate that the following well is filled with what you need" 
border: A12 or A11
inner border:A10 or A9
Blank: blank
WT1:A1
WT2: A2
etc
"""

import os
import csv
import re


#Things you need to change when you use
os.chdir("your/working/directory")

output_path = "./Input_file/4_WT_filled/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
        

print("How many plates you have in ./Input_file/1_merged_plates/?")
your_plate_number = input()

print("How many WT you want to include in your plate")
WT_number = input()
WT_list=[] 
for i in range(1,int(WT_number)+1):         
    WT_list.append(f"WT{i}")  
#print(WT_list)

for plate_number in range(1,int(your_plate_number)+1):
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
    
output_path = "./Input_file/5_Rest_filled/"
if not os.path.exists(output_path):
        os.makedirs(output_path)

for plate_number in range(1,int(your_plate_number)+1):
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
            if re.search(r'\b' + "inner_border" + r'\b', row[0]):
                row[1] = "SourcePlate0"
                row[2] = "A"
                row[3] = "10"
            for i in range(0,len(WT_list)):     
                if re.search(r'\b' + f"WT{i+1}" + r'\b', row[0]):
                    row[1] = "SourcePlate0"
                    row[2] = "A"
                    row[3] = f"{i+1}"

            writer.writerow(row)
