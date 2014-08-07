#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, sys

reader=csv.reader(sys.stdin,delimiter="\t")
oldrow = None
with open("output.csv", 'w') as master_file:
	try:
		for row in reader:
		
			new_row = str(row).strip().split(',');
			for i in new_row:
				if (new_row[i]) == None:
					new_row[i] = old_row[i]
			master_file.write(new_row)
			old_row = new_row
        
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
	
