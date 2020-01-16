'''
mergeCSV.py

Merges list of CSV files.
Gets list by accessing specific directory and getting the names of the files
in that directory
'''

import os
import glob
import pandas as pd


os.chdir("/Users/smoreno/Dropbox (Partners HealthCare)/bms025/Output/benefit_fisher/")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')