import io
import os
import json
import csv

#open json dataset and create a csv file with features and labels

    

#spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

s = os.path.abspath("../data/new_data2.json")
#print s

#TODO: implement http://www.nltk.org/book/ch05.html

with open(s)as data_file:
  daa=json.load(data_file)

with open('reddit_no_labels.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #leave out for python code
#    spamwriter.writerow(['ups', 'author', 'subreddit', 'num_words', 'avg_word_length'])

    for line in daa:
      body=line['body']
    
      #count number of words
    
      words = body.split(" ")
      
      #number of words
      #print "Number of words:"
      number_of_words = len(words)
    
    #  print words[0] 
      #find # of characters in words
    
    #TODO: ignore punctuation
      
      sum_of_word_lengths = 0
      for word in words:
        num_of_chars = sum(c != ' ' for c in word)
        sum_of_word_lengths = sum_of_word_lengths + num_of_chars
    #    print(sum)
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

#  if len(list) < 100:
#    print line['author'],line['subreddit'],line['ups'] 
