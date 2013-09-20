#!/usr/bin/env python

import csv
import sys

if len(sys.argv) != 3:
    print "Usage: %s [table data file] [selection(s) from data file]" % sys.argv[0]
    print ""
    print "Returns the corresponding bam file and genome in the following format: BAM_FILE -g GENOME" 
    print ""
    print "Note that the selection(s) format is from the Extended Choice (Multi-Level Multi Select) Jenkins plugin."
    print ""
    print "Examples:"
    print ""
    print '\t$ python %s /mnt/d0-0/share/bradnerlab/projects/masterBamTable.txt "HG18,Multiple Myeloma,MM1S,MM1S_BRD4_500nM_JQ1"' % sys.argv[0]
    print "\t/ifs/labs/bradner/bam/hg18/mm1s/05242012_D0WUYACXX_3.ACAGTG.hg18.bwt.sorted.bam -g HG18 -n MM1S_BRD4_500nM_JQ1" 
    print "\t$"
    print ""
    print '\t$ python %s /mnt/d0-0/share/bradnerlab/projects/masterBamTable.txt "HG18,Multiple Myeloma,MM1S,MM1S_BRD4_500nM_JQ1,,HG18,Diffuse large B-cell lymphoma,LY1,LY1_BCL6_DMSO"' % sys.argv[0]
    print "\t/ifs/labs/bradner/bam/hg18/mm1s/05242012_D0WUYACXX_3.ACAGTG.hg18.bwt.sorted.bam,/ifs/labs/bradner/bam/hg18/ly1/06152012_C0VD4ACXX_6.AGTTCC.hg18.bwt.sorted.bam -g HG18 -n MM1S_BRD4_500nM_JQ1,LY1_BCL6_DMSO" 
    print "\t$"
    sys.exit(-1)

(table_data_file_name, comma_seperated_selections) = (sys.argv[1], sys.argv[2])

names = []
for selection in comma_seperated_selections.split(',,'):
    selection_columns = selection.split(',')
    if len(selection_columns) == 4:
        names.append(selection_columns[3]) 

# files are assumed to be in a 5 column tab delimited format such as the following:
# GENOME  SOURCE  CELL_TYPE       NAME    BAMFILE
# HG18    Diffuse large B-cell lymphoma   LY1     LY1_BCL6_DMSO   /ifs/labs/bradner/bam/hg18/ly1/06152012_C0VD4ACXX_7.GTCCGC.hg18.bwt.sorted.bam
genome_col  = 0
source_col  = 1 # ignored
celltyp_col = 2 # ignored
name_col    = 3
file_col    = 4

# old format:
# NAME    UNIQUE_ID       BAM_FILE        GENOME  COLOR
# MM1S_BRD4_500nM_JQ1     05242012_D0WUYACXX_3.ACAGTG     05242012_D0WUYACXX_3.ACAGTG.hg18.bwt.sorted.bam hg18    47,26,251
# name_col   = 0
# id_col     = 1
# file_col   = 2
# genome_col = 3
# color_col  = 4

files  = ""
genome = ""

with open(table_data_file_name, 'r') as table_data_file:
    reader = csv.reader(table_data_file, delimiter='\t')
   
    for record in reader:
        if record[name_col] in names:
            if len(files) > 0:
                files += ","
            files += record[file_col]
            genome = record[genome_col]


if files == "":
    print "Record not found for name '%s' in %s" % (name, table_data_file_name) 
    sys.exit(1)
else:
    print "%s -g %s -n %s" % (files, genome, ",".join(names)) 
    
