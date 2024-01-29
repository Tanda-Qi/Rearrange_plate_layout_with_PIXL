#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:20:56 2023

@author: tanda
"""

import csv
import os
os.chdir("/Users/tanda/Dropbox (The University of Manchester)/Working/2023_Protein_SGA/2023_07_96_well_plate_rearrangement/pipeline")

input_path="./Input_file/0_seperated_source_file/"
output_path = "./Input_file/1_merged_3_plates/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
a=0
b=0
c=0
for i in range(0,17):
    j=i+1
    a=3*i+1
    b=3*i+2  
    c=3*i+3 
    input_file1 = "./Input_file/0_seperated_source_file/protein_collection_plate"+str(a)+".csv"
    input_file2 = "./Input_file/0_seperated_source_file/protein_collection_plate"+str(b)+".csv"
    input_file3 = "./Input_file/0_seperated_source_file/protein_collection_plate"+str(c)+".csv"
    # Output file path
    output_file = output_path+"Merged_plates_No"+str(j)+".csv"

    # Merge CSV files
    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
    
        # Process the first file
        with open(input_file1, "r") as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read and save the header
            writer.writerow(header)  # Write the header to the output file
            for row in reader:
                writer.writerow(row)  # Write each row to the output file
    
        # Process the second file
        with open(input_file2, "r") as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header
            for row in reader:
                writer.writerow(row)  # Write each row to the output file
    
        # Process the third file
        with open(input_file3, "r") as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header
            for row in reader:
                writer.writerow(row)  # Write each row to the output file
                
#merge plate 70 and 71
plate70 = "./Input_file/0_seperated_source_file/protein_collection_plate70.csv"
plate71 = "./Input_file/0_seperated_source_file/protein_collection_plate71.csv"
output_file = output_path+"Merged_plates_No18.csv"

# Merge CSV files
with open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)

    # Process the first file
    with open(plate70, "r") as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read and save the header
        writer.writerow(header)  # Write the header to the output file
        for row in reader:
            writer.writerow(row)  # Write each row to the output file

    # Process the second file
    with open(plate71, "r") as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip the header
        for row in reader:
            writer.writerow(row)  # Write each row to the output file
