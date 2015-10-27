 import io
 import os
 import json
 s = os.path.abspath("../data/new_data2.json")
 print s
 with open(s)as data_file:
	daa=json.load(data_file)
 for line in daa:
	str=line['body']
	list = str.split(" ")
    print list
    print len(list)
    if len(list) < 100:
		print line['author'],line['subreddit'],line['ups'] 
		
