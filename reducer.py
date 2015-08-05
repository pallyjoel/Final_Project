import logging
import csv, sys

reader=csv.reader(sys.stdin,delimiter='\t')
entries = 0
days = 0
old_key = None
with open("output.csv", 'w') as master_file:
	master_file.write( '{0},{1}\n'.format('Day', 'Avg_Hourly_Entries'))
	for row in reader:
		data = str(row).strip().split(',')
	
		if len(data) !=2 or data[1][4:-3] == 'ENTRIESn_hourly':

			continue
	
		new_key, value = data
		new_key = new_key[4:-2]
		value = (value[4:-4])

		if old_key != None and new_key !=old_key:
			master_file.write( '{0},{1}\n'.format(old_key, float(entries)/days))
			entries = 0
			days = 0
		
		old_key = new_key
		entries += float(value)
		days += 1
	if old_key != None:
		master_file.write( '{0},{1}\n'.format(old_key, float(entries)/days))