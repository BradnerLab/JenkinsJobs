#!/usr/bin/env python

import csv

#property_file_path = '???/jobs/Bam_Plot/placeholder_data/selectionChoicesPropertyFile.txt'
#table_file_path    = '/mnt/d0-0/share/bradnerlab/projects/masterBamTable.txt'

property_file_path = '/Users/Shared/Jenkins/Home/jobs/Bam_Plot/placeholder_data/selectionChoicesPropertyFile.txt'
table_file_path    = '/Users/Shared/Jenkins/Home/jobs/Bam_Plot/placeholder_data/masterBamTable.txt'

name_col = 3

with open(property_file_path, 'w') as property_file:
    property_file.write('selectionChoices=')

    with open(table_file_path, 'r') as table_data_file:
        reader = csv.reader(table_data_file, delimiter='\t')

        processedFirstRecord = False
        for record in reader:
            if processedFirstRecord:
                property_file.write('%s,' % record[name_col])
            else:
                processedFirstRecord = True

    property_file.write('\n')
