import sys
import os
import csv

args = sys.argv[1:]

if args:
	if(len(args) == 1):
		infile = args[0]
		outfile = infile.replace(".csv", ".plist")
		plisttype = 'array'
	
	if(len(args) == 2):
		infile = args[0]
		outfile = args[1]
		plisttype = 'array'
	
	if(len(args) == 3):
		infile = args[0]
		outfile = args[1]
		plisttype = args[2]
	
	if(open(os.path.abspath(outfile),'w')):
		if(os.path.isfile(infile)):
			data = csv.reader(open(infile))
			warningShown = None
			output = open(os.path.abspath(outfile),'w')
			
			output.write('<?xml version="1.0" encoding="UTF-8"?>\n')
			output.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
			output.write('<plist version="1.0">\n')
			output.write('<array>\n')
			
			for row in data:
				if(plisttype == 'array' and len(row) > 1 and warningShown == None):
					warningShown = True
					print 'Warning: Converting to an array only uses first column of data'

				output.write('\t<string>' + row[0] + '</string>\n')
			
			output.write('</array>\n')
			output.write('</plist>')
			output.close()
			print os.path.basename(os.path.abspath(outfile)) + ' created successfully'
		else:
			print infile + ' could not be opened'
			exit()
	else:
		print outfile + ' is not writable'
		exit()
	
	
else:
	print '\ncsv2plist usage:\npython csv2plist.py <CSVFile> [output plist file] [type]\n';
	