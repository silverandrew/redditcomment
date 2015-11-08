import io
import os
import json
import csv
import string 
import nltk
import gensim

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
#    spamwriter.writerow(['ups', 'num_words', 'avg_word_length'])

  for line in daa:

#iterate and fill
#list of unique tags per comment
    pos_frequency = list()
#for each possible tag
#start with 0 frequency
    for x in range(0, 36):
      pos_frequency.append(0)

    body=line['body']
    print "ready to tokenize comment"
    text = nltk.word_tokenize(body)
    #tagged words
    tagged_words = nltk.pos_tag(text)
    for tags in tagged_words:
      if tags[1] == "CC":
        pos_frequency[0] += 1
      elif tags[1] == "CD":
        pos_frequency[1] += 1
      elif tags[1] == "DT":
        pos_frequency[2] += 1
      elif tags[1] == "EX":
        pos_frequency[3] += 1
      elif tags[1] == "FW":
        pos_frequency[4] += 1
      elif tags[1] == "IN":
        pos_frequency[5] += 1
      elif tags[1] == "JJ":
        pos_frequency[6] += 1
      elif tags[1] == "JJR":
        pos_frequency[7] += 1
      elif tags[1] == "JJS":
        pos_frequency[8] += 1
      elif tags[1] == "LS":
        pos_frequency[9] += 1
      elif tags[1] == "MD":
        pos_frequency[10] += 1
      elif tags[1] == "NN":
        pos_frequency[10] += 1
      elif tags[1] == "NN":
        pos_frequency[11] += 1
      elif tags[1] == "NNS":
        pos_frequency[12] += 1
      elif tags[1] == "NNP":
        pos_frequency[13] += 1
      elif tags[1] == "NNPS":
        pos_frequency[14] += 1
      elif tags[1] == "PDT":
        pos_frequency[15] += 1
      elif tags[1] == "POS":
        pos_frequency[16] += 1
      elif tags[1] == "PRP":
        pos_frequency[17] += 1
      elif tags[1] == "PRP$":
        pos_frequency[18] += 1
      elif tags[1] == "RB":
        pos_frequency[19] += 1
      elif tags[1] == "RBR":
        pos_frequency[20] += 1
      elif tags[1] == "RBS":
        pos_frequency[21] += 1
      elif tags[1] == "RP":
        pos_frequency[22] += 1
      elif tags[1] == "SYM":
        pos_frequency[23] += 1
      elif tags[1] == "TO":
        pos_frequency[24] += 1
      elif tags[1] == "UH":
        pos_frequency[25] += 1
      elif tags[1] == "VB":
        pos_frequency[26] += 1
      elif tags[1] == "VBD":
        pos_frequency[27] += 1
      elif tags[1] == "VBG":
        pos_frequency[28] += 1
      elif tags[1] == "VBN":
        pos_frequency[29] += 1
      elif tags[1] == "VBP":
        pos_frequency[30] += 1
      elif tags[1] == "VBZ":
        pos_frequency[31] += 1
      elif tags[1] == "WDT":
        pos_frequency[32] += 1
      elif tags[1] == "WP":
        pos_frequency[33] += 1
      elif tags[1] == "WP$":
        pos_frequency[34] += 1
      elif tags[1] == "WRB":
        pos_frequency[35] += 1
   
   #    print(tagged_words)[0]
   #    print pos_frequency
    print ("done tokenizing comment")

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
    
#      author = line['author']
#      subreddit = line ['subreddit']

#nltk tokenize words
#      text = nltk.word_tokenize(body)
    
    #label
    #column 0 
    ups = line['ups']
    spamwriter.writerow([ups, ",", number_of_words, ",", 
    pos_frequency[0],",",
    pos_frequency[1],",",
    pos_frequency[2],",",
    pos_frequency[3],",",
    pos_frequency[4],",",
    pos_frequency[5],",",
    pos_frequency[6],",",
    pos_frequency[7],",",
    pos_frequency[8],",",
    pos_frequency[9],",",
    pos_frequency[10],",",
    pos_frequency[11],",",
    pos_frequency[12],",",
    pos_frequency[13],",",
    pos_frequency[14],",",
    pos_frequency[15],",",
    pos_frequency[16],",",
    pos_frequency[17],",",
    pos_frequency[18],",",
    pos_frequency[19],",",
    pos_frequency[20],",",
    pos_frequency[21],",",
    pos_frequency[22],",",
    pos_frequency[23],",",
    pos_frequency[24],",",
    pos_frequency[25],",",
    pos_frequency[26],",",
    pos_frequency[27],",",
    pos_frequency[28],",",
    pos_frequency[29],",",
    pos_frequency[30],",",
    pos_frequency[31],",",
    pos_frequency[32],",",
    pos_frequency[33],",",
    pos_frequency[34],",",
    pos_frequency[35],",",
    avg_word_length])
