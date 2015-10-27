import io
import os
import json
import csv
import string 

#open json dataset and create a csv file with features and labels

#input file
s = os.path.abspath("../data/new_data2.json")
#print s

#TODO: implement using http://www.nltk.org/book/ch05.html

with open(s)as data_file:
  daa=json.load(data_file)

with open('reddit.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #leave out for python code
    spamwriter.writerow(['ups', 'author', 'subreddit', 'num_words', 'avg_word_length'])

    for line in daa:
      body=line['body']

#slow, need to do because text is unicode
#get rid of punctuation
      exclude = set(string.punctuation)
      body = ''.join(ch for ch in body if ch not in exclude)
    
      #count number of words
      words = body.split(" ")
      
      #number of words
      #print "Number of words:"
      number_of_words = len(words)
    
      #find # of characters in words
      sum_of_word_lengths = 0
      for word in words:
        num_of_chars = sum(c != ' ' for c in word)
        sum_of_word_lengths = sum_of_word_lengths + num_of_chars
        # of chars divided by total # of words
    
      avg_word_length = sum_of_word_lengths / len(words)
    
    #avg word length of this comment
      #print "Average Word Length:"
      #print avg_word_length
    
      author = line['author']
      subreddit = line ['subreddit']
    
    #label
    #column 0 
      ups = line['ups']
      spamwriter.writerow([ups, author, subreddit, number_of_words, avg_word_length])
