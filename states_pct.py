#!/usr/bin/python

import json
import sys

# input block
filename = sys.argv[1]
infile = open(filename, 'rb')
records = json.load(infile)
infile.close()

# output block
# % table
for record in sorted(records):
    dempct = records[record]['Democratic']['%']
    reppct = records[record]['Republican']['%']
    othpct = 100. - (dempct + reppct)
    if 'total' in record.lower():
        print '{:<20}'.format('U. S.'),
    else:
        print '{:<20}'.format(record),
    print format(dempct, "8.2f"),
    print format(reppct, "8.2f"),
    print format(othpct, "8.2f")
