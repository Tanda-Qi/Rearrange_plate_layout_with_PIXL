#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:25:27 2023

@author: tanda
"""
import os
import csv
import re
#Things you need to change when you use
os.chdir("your/working/directory")


coordinate_column=0
coordinate_row=0

def generate_coordinate_row (i):
    coordinate_row=0
    if i<10:
        coordinate_row=1+i
    else:
        coordinate_row=i-8
    return coordinate_row


def generate_coordinate_column (i):
    coordinate_column=0
    if i<10:
        coordinate_column=2
    else:
        coordinate_column=7
    return coordinate_column

print("How many plates you have in ./Input_file/1_merged_plates/?")
your_plate_number = input()


for plate_number in range(1,int(your_plate_number)+1):
    coordinate_column=0
    coordinate_row=0
    column_start = generate_coordinate_column(plate_number)
    row_start = generate_coordinate_row(plate_number)
    #print(row_start, column_start)
    blank_row= row_start+1
    blank_column1=column_start+1
    blank_column2=column_start+3
    template_file="./Input_file/template_border.csv"
    #input_file= "/Users/tanda/Dropbox (The University of Manchester)/Working/2023_07_96_well_plate_rearrangement/1_merged_3_plates/Merged_plates_No"+str(plate_number)+".csv"
    output_path = "./Input_file/2_New_coordinates/"
    if not os.path.exists(output_path):
            os.makedirs(output_path)
    output_file = output_path+"New_coordinates_added_plate"+str(plate_number)+".csv"
   

    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)    
     
        # Process the first file
        with open(template_file, "r") as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read and save the header
            writer.writerow(header)  # Write the header to the output file    
          
            for row in reader:
                for row_range in range(row_start, row_start + 3):
                    for column_range in range(column_start, column_start + 5):
                        #print(row_range,column_range)
                        if re.search(r'\b' + str(row_range) + r'\b', row[4]) and re.search(r'\b' + str(column_range) + r'\b', row[5]):
                            row[0] = "inner_border"
                if re.search(r'\b' + str(blank_row) + r'\b', row[4]) and re.search(r'\b' + str(blank_column1) + r'\b', row[5]):
                    row[0] = "Blank"
                if re.search(r'\b' + str(blank_row) + r'\b', row[4]) and re.search(r'\b' + str(blank_column2) + r'\b', row[5]):
                    row[0] = "Blank"    
                writer.writerow(row)
    










