import io
import os
#import json

#from itertools import islice

datafile = "RC_2015-01"
#note: you must create this file
#TODO: create if doesn't exist
outputfile = "new_data.json"


#N = 2

#with open(datafile) as myfile:
#        head = list(islice(myfile, N))
#        print head

#output file
#s = os.path.abspath("new_data.json")
#print s

N=1000

#open for writing
o = open(outputfile, 'r+')

with open(datafile) as f:
    i = 0
#can't use range loop because the bounds of iterator need to change based on # of deleted comments skipped
#warning: could run outside bounds of data file. TODO: check size?
    while i < N:
        line=f.next().strip()

#Only use comments that don't contain "[deleted]"
        if line.find("[deleted]") == -1:
          print line
#delimit the comments by the new line character
#TODO: could also use a ,
          o.write(line + '\n')
#increment loop counter, since you added a comment
          i+=1
        else:
          print "deleted entry"
          continue
f.close()

o.close()

#with open(data_file) as f:
#    for line in f:
#        j_content = json.loads(line);

#data_file = "RC_2015-01"
#s = os.path.abspath("new_data.json")
#print s
#from pprint import pprint
#
#with open('RC_2015-01', 'r') as fobj:
#    daa = json.load(fobj);
#
##with open(s)as data_file:
##        daa=json.loads("RC_2015-01.json")
#
#pprint(daa)
#print type(daa)
#print daa[0]['author']
#
#for line in daa: 
#    print daa [999]
