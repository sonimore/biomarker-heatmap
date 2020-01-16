'''
wrangle.py

Sonia Moreno
1/15/2019

Takes as input a list of csv files. 
Creates long form of data.
Outputs csv with new long-form data.

'''

from os import listdir
from os.path import isfile, join
import pandas as pd 
import numpy as np
import re, csv

'''
Takes as input some path/directory and gets list of all files in that directory
'''
def getFiles(dir, typeOfFiles):
	listOfFiles = [f for f in listdir(dir) if (isfile(join(dir, f)) and f.endswith('.csv'))]
	listOfFiles.sort()
	# Get the biomarker names and definitions from each filename w/out .csv at the end
	listOfBioDefs = []
	for f in listOfFiles:
		try:
			biodef = re.search("(?<=cibersort_wilcox_).*$", f)
			biodef = biodef.group()[:-4]
		except:
			print("Unable to find", typeOfFiles, "in name. Keeping original filename.")
			biodef = f
		# print("Number of samples found", num)
		
		# biodef = biodef.group()
		listOfBioDefs.append(biodef)

	print(listOfBioDefs)
	return listOfBioDefs

'''
Takes as input a datafile with features as the rows. Outputs a list of those features.
'''
def getFeatures(path, filename, typeOfFiles):
	data = pd.read_csv(path + typeOfFiles + filename + '.csv')
	if typeOfFiles == 'ssgsea_wilcox_' or typeOfFiles == 'cibersort_wilcox_':
		return data['Hugo_Symbol']
	else:
	# print(data['event'])
		return data['event']


'''
Takes as input list of data files and list of features/rows that each datafile has in common.
Outputs merged data in long form.
'''
def wrangleData(path, files, typeOfFiles):
	features = getFeatures(path, files[0], typeOfFiles)
	# print("List of files: ", files)
	# print("features: \n", features)
	# print(len(features))

	# output data/merged long-form data
	# output = np.empty((0, 4))
	output = []
	columns = ['event', 'group', 'pvalue', 'up_group', 'qvalue']
	output.append(columns)
	# print(output)


	# For every feature and for every biomarker-def group, 
	# Create new row with [event/feature, biomarker-def group, pvalue, up_group]
	for featureIndex in range(len(features)):
		feature = features[featureIndex]
		# print(feature)
		for file in files:
			d = pd.read_csv(path + typeOfFiles + file + '.csv')
			# print("DATA: \n")
			# print(d.head())
			# print("FEATURE: \n")
			# print(d.at[featureIndex, 'pvalue'])
			p = d.at[featureIndex, 'pvalue']
			up = ''
			if typeOfFiles == 'ssgsea_wilcox_' or typeOfFiles == 'cibersort_wilcox_':
				up = d.at[featureIndex, 'up_grp']
			else:
				up = d.at[featureIndex, 'up_group']
			q = d.at[featureIndex, 'qvalue']

			newRow = [feature, file, p, up, q]
			output.append(newRow)
			# output = np.append(output, newRow, axis = 0)
	# print(len(output))
	return output
			# print(newRow)



def getDataArray(dataFile, newFilename):
	with open(newFilename, 'w') as f:
		writer = csv.writer(f, delimiter = ',')
		for row in dataFile:
			writer.writerow(row)



def main():
	# Directory where mutation p-value tables are stored.
	# mutDir = "/Users/smoreno/Dropbox (Partners HealthCare)/bms025/Output/mutations_fisher/"
	ssgseaDir = "/Users/smoreno/Dropbox (Partners HealthCare)/bms025/Output/ssgsea_wilcox/"
	cibersortDir = '/Users/smoreno/Dropbox (Partners HealthCare)/bms025/Output/cibersort_wilcox/'
	# typeOfFiles = 'mutations_fisher_test_'
	# typeOfFiles = 'ssgsea_wilcox_'
	typeOfFiles = 'cibersort_wilcox_'
	listOfFiles = getFiles(cibersortDir, typeOfFiles)
	getFeatures(cibersortDir, listOfFiles[0], typeOfFiles)
	d = wrangleData(cibersortDir, listOfFiles, typeOfFiles)
	fn = '/Users/smoreno/Documents/heatmap/' + typeOfFiles + 'merged_longform.csv'
	print("NAME: \n", fn)
	getDataArray(d, fn)



main()