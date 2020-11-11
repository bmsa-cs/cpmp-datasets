#!/usr/bin/env python3
"""
cmt_to_tsv

Converts CPMP-Tools .cmt data files to more generic .tsv files.
"""

import os
import csv
import json

data_folder = os.path.abspath('data/')

dir_list = os.listdir(data_folder)

for file in dir_list:
    out_rows = []
    title = None
    description = ''
    if file.endswith('.cmt'):
        with open(os.path.join(data_folder, file), 'r', encoding="ISO-8859-1") as cmt_file:
            csv_reader = csv.reader(cmt_file, delimiter='\t')
            last_row = None # Keep track of last row for purposes of knowing when the data begins.
            for row in csv_reader:
                if len(row) > 0:
                    if row[0].startswith("#"):
                        description += row[0][1:] + '\n'
                        last_row = 'desc'
                    elif last_row == 'desc':
                        title = row[0]
                        last_row = 'title'
                    elif last_row == 'title':
                        last_row = 'types'
                    elif last_row == 'types' or last_row == 'data':
                        # TODO: Some of the files have formulas (ex: =log(A)). Need to calculate/convert/remove?
                        out_rows.append(row)
                        last_row = 'data'
                        

            # TODO: Create some sort of documentation about each file using titles and descriptions.
            # print(title)
            # print(description)
        
        # Write the cleaned data to a .tsv
        with open(os.path.join('tsv/', file.split('.cmt')[0] + '.tsv'), 'w', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file, delimiter='\t')
            writer.writerows(out_rows)