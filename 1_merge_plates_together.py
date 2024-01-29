#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:20:56 2023

@author: Tanda Qi
If you meet any issue, feel free to contact me via tanda.qi@gmail.com
"""

import csv
import os


#Things you need to change when you use
os.chdir("your/working/directory")
your_file_naming_way="My_file_name"   


#os.chdir("/Users/tanda/Dropbox (The University of Manchester)/General work(lab)/Rearrange_plates_PIXL")
#your_file_naming_way="protein_collection_plate"

       

#I merge 3 plate at the same time, but you can do 2 as well through not recommend 

def merge_plates_3(input_path, output_path, num_plates, your_file_naming_way):
    for i in range (int(int(num_plates)/3)):
        a = 3 * i + 1
        b = 3 * i + 2
        c = 3 * i + 3
        input_file1 = f"{input_path}/{your_file_naming_way}{a}.csv"
        input_file2 = f"{input_path}/{your_file_naming_way}{b}.csv"
        input_file3 = f"{input_path}/{your_file_naming_way}{c}.csv"
        output_file = f"{output_path}/Merged_plates_No{i + 1}.csv"

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



                
             
#merge 2 plates in this way 
def merge_plates_2(input_path, output_path, num_plates, your_file_naming_way):
    for i in range(int(int(num_plates)/2)):
        d = 2 * i + 1
        e = 2 * i + 2
        plateA = f"{input_path}/{your_file_naming_way}{d}.csv"
        plateB = f"{input_path}/{your_file_naming_way}{e}.csv"
        output_file = f"{output_path}/Merged_plates_No{i + 1}.csv"

        # Merge CSV files
        with open(output_file, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            
            # Process the first file
            with open(plateA, "r") as infile:
                reader = csv.reader(infile)
                header = next(reader)  # Read and save the header
                writer.writerow(header)  # Write the header to the output file
                for row in reader:
                    writer.writerow(row)  # Write each row to the output file
            
            # Process the second file
            with open(plateB, "r") as infile:
                reader = csv.reader(infile)
                next(reader)  # Skip the header
                for row in reader:
                    writer.writerow(row)  # Write each row to the output file
                    
                    
input_path="./Input_file/Source_file/"
output_path = "./Input_file/1_merged_plates/"                 
if not os.path.exists(output_path):
        os.makedirs(output_path)  
              
print('Choose how many plate you want to merge into one 384 plate。 You can choose 2 or 3')
num_to_merge = input()
print('How many plate you have in total? (Needs to be divisible by the last number you entered)')
num_plates = input()

print(num_to_merge,num_plates)


if int(num_to_merge) == 2:
    merge_plates_2(input_path, output_path, num_plates, your_file_naming_way)
elif int(num_to_merge) == 3:
    merge_plates_3(input_path, output_path, num_plates, your_file_naming_way)
else:
    print("You did something wrong!")

        