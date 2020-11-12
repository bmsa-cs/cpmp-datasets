#!/usr/bin/env python3
"""
cmt_to_tsv

Converts CPMP-Tools .cmt data files to more generic .tsv files.
"""

import os
import csv
import json

def process_cmt(cmt_file):
    """Given an open cmt_file, process the rows and return the title, description, and out_rows."""

    title = None
    description = ''
    out_rows = []

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
    return title, description, out_rows

def build_documentation_string(title, description, filename):
    description = description.replace("\n","\n\n")
    return f"## {title}\n\nFile: {filename}\n\nDescription:{description}\n"

# def get_course_from_title(title):
#     """
#     Given a title, attempts to match it with a course and unit,
#     however not all titles match the one in the file.
#     """
#     for course in titles:
#         for unit in titles[course]:
#             for exploration in titles[course][unit]['explorations']:
#                 if exploration == title:
#                     return course+unit
#     return "N/A"

if __name__ == "__main__":
    data_folder = os.path.abspath('../data/')
    out_folder = os.path.abspath('../tsv')

    dir_list = os.listdir(data_folder)
    dir_list = sorted(dir_list)
    
    documentation = "# Filelist\n\n"

    # UNUSED: Titles don't match the ones in the files.
    # with open('dataset-titles.json', 'r') as title_file:
    #     titles = json.load(title_file)

    for file in dir_list:
        if file.endswith('.cmt'):
            out_file = file.split('.cmt')[0] + '.tsv'

            with open(os.path.join(data_folder, file), 'r', encoding="ISO-8859-1") as cmt_file:
                t,d, out_rows = process_cmt(cmt_file)
                ds = build_documentation_string(t,d,out_file)
                # course = get_course_from_title(t)
                # print("course: " + course)
                documentation += ds
            
            # Write the cleaned data to a .tsv
            with open(os.path.join(out_folder, out_file), 'w', encoding='UTF-8') as csv_file:
                writer = csv.writer(csv_file, delimiter='\t')
                writer.writerows(out_rows)
    
    
    with open(os.path.join(out_folder, "README.md"), 'w') as dataset_file:
        dataset_file.write(documentation)
