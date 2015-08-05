
import csv, sys

reader=csv.reader(sys.stdin,delimiter="\t")
try:
    for row in reader:
		
        data = str(row).strip().split(',');
        if data[0] == 'DATEn':
            cotinue
        else:
            wrow = '{0}\t{1}\n'.format(data[3], data[1])
            print wrow
except csv.Error as e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))