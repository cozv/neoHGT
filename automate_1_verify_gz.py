"""
///////////////////////////////////////////////////////
│	
│	Filename:	automate_1_verify_gz.py
│	Description:
│	To verify the integrity of .gz files in directory
│	and print the corrupted ones' file names.
│	==================================================
│	Authorship:	@cgneo
│	Copyright:	Modified BSD License.
│	Made with love by https://github.com/cgneo
│	
///////////////////////////////////////////////////////
"""


import os
import gzip
from auto_print_progress import printProgressBar


"""
│	(optional):
│	Please choose the directory containing .gz files for database:
│	For example:
│	directory = './hgtdb'
"""
#============================================================
directory = './'
#============================================================
success = 0
failed = 0
all_file = 0
list_of_files = []
for root, subdirectories, files in os.walk(directory):
	subdirectories.sort()
	for file in files:
		name, extension = os.path.splitext(file)
		if extension == '.gz':
			list_of_files.append(os.path.join(root, file))

print(f'Finish scaning: {len(list_of_files)} .gz files in total.')


for i in range(len(list_of_files)):
	line_count_test = 0
	try:
		fin = gzip.open(list_of_files[i], 'rt')
		for line in fin:
			line_count_test += 1
			if line_count_test >= 2: break
		success += 1
	except Exception as e:
		failed += 1
		print(f'failed at {file}: {e}')
	
	all_file += 1
	printProgressBar(i+1, len(list_of_files), prefix='Progress:', suffix=list_of_files[i], length=30)

print()
print(f'Sucesss: {success}/{all_file},  Failed: {failed}/{all_file}')