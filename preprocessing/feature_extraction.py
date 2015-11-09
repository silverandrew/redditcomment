#!/usr/bin/env python
import io
import os
import json
import csv
import string 
import nltk
import gensim
from itertools import dropwhile
import postagger
import sys
import re

"""
Passive sentence detection kudos to: https://github.com/j-c-h-e-n-g/nltk-passive-voice
"""

TAGGER = None

def tag_sentence(sent):
    """Take a sentence as a string and return a list of (word, tag) tuples."""
    assert isinstance(sent, basestring)

    tokens = nltk.word_tokenize(sent)
    return TAGGER.tag(tokens)

def passivep(tags):
    """Takes a list of tags, returns true if we think this is a passive
    sentence."""
    # Particularly, if we see a "BE" verb followed by some other, non-BE
    # verb, except for a gerund, we deem the sentence to be passive.
    
    postToBe = list(dropwhile(lambda(tag): not tag.startswith("BE"), tags))
    nongerund = lambda(tag): tag.startswith("V") and not tag.startswith("VBG")

    filtered = filter(nongerund, postToBe)
    out = any(filtered)

    return out

punkt = nltk.tokenize.punkt.PunktSentenceTokenizer()

def is_passive(sent, tagged_words):
    """Given a sentence, tag it and print if we think it's a passive-voice
    formation."""
#tagged words from this sentence
    tagged = tag_sentence(sent)
#now add to global list so all the tags for this sentence are tracked
#hack to prevent double-tokenizing words
    for new_tags in tagged:
      tagged_words.append(new_tags)

    tags = map( lambda(tup): tup[1], tagged)
    if passivep(tags):
      return True

#open json dataset and create a csv file with features and labels

#input file
#s = os.path.abspath("../data/new_data2.json")
s = os.path.abspath("../data/thousands.json")
#print s

#TODO: implement using http://www.nltk.org/book/ch05.html

#Tagger for finding passive sentences
global TAGGER
TAGGER = postagger.get_tagger()

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
    #print "ready to tokenize comment"
#tokenize into sentences to check for passive voice
    punkt = nltk.tokenize.punkt.PunktSentenceTokenizer()
    sentences = punkt.tokenize(body)
    #print "sentences"
    #tagged_sentences = nltk.pos_tag(sentences)
    #print tagged_sentences
    #print sentences
    num_passive_sentences = 0
#fill tag words, pass as reference so we don't need to run twice
    tagged_words = list()
    for sent in sentences:
      if (is_passive(sent, tagged_words)):
        num_passive_sentences += 1
#at the end of loop, tagged_words contains all the tagged words from each sentence

#now tokenize words
#    text = nltk.word_tokenize(body)
    #tagged words
#    tagged_words = nltk.pos_tag(text)

    #print tagged_words
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
#    print ("done tokenizing comment")

    #print body

    #stoplist for excluding words for gensim
    stoplist = set(nltk.corpus.stopwords.words("english"))

#    print "the sentence is: "
#    print sentences

   #at this point already used sentences data for NLTK NLP, so modify
   #remove punctuation
    letters_only_sentence = list()
    for a_sent in sentences:
      letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                            " ",                   # The pattern to replace it with
                            a_sent)  # The text to search
      letters_only_sentence.append(letters_only)
      #sentences = ''.join(ch for ch in body if ch not in exclude)

#      print letters_only_sentence

#create text
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in letters_only_sentence]
    dictionary = gensim.corpora.Dictionary(texts)
#create corpus
    corpus = [dictionary.doc2bow(text) for text in texts]

#whether or not to save this as a data point in file
    save_feature = True
# no non-stopwords in comment, then don't save this as a feature
    for subs in texts:
      if len(subs) == 0:
        save_feature = False
        print "IGNORING FEATURE. MISSING ENOUGH WORDS FOR TOPIC MODELING."

#Latent Dirchlet Analysis on text
    if save_feature:
#      print len(texts)
      lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1, update_every=1, chunksize=10000, passes=1)
#      print "LDA finished"
      print lda.print_topics(1)

#output
#    print lda.print_topics(5)

#slow, need to do because text is unicode
#get rid of punctuation
#TODO: don't need to do twice, already available via nltk
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
  
  #NOTE: delimit each new feature added with a "," or it will break svmpredict.py
      
      #label
      #column 0 
      ups = line['ups']
      spamwriter.writerow([ups, ",", number_of_words, ",", 
      num_passive_sentences, ",",
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
