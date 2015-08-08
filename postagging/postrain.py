#!/usr/bin/python3

import sys
sys.path.append('../')
import collections
import pickle
import perceplearn
import re
if(len(sys.argv) == 3):
	training_file = str(sys.argv[1])
	model_file = str(sys.argv[2])
else:
	print("Invalid Arguments.\nUsage: ./postrain.py TRAINING_FILE MODEL_FILE")
	sys.exit()
temp_model_file="pos_inter"
opf = open(temp_model_file,"w")
ipf = open(training_file,"r")

count=0
for line in ipf:
	words=line.split()
	count+=1
	#print(words)
	l=len(words)
	i=0
	for word in words:
		if(i!=0):
			prev_word=words[i-1].split('/')[0]
		else:
			prev_word='BOS'
		if(i!=l-1):
			next_word=words[i+1].split('/')[0]
		else:
			next_word='EOS'
		tags=word.split('/')
		"""wshape='a'
		if(re.match('^[A-Z]+$',tags[0])):
			wshape='AA'
		if(re.match('^[A-Z][a-z]+',tags[0])):
			wshape='Aa'
		if(re.match('[0-9]+',tags[0])):
			wshape='9'
		if(re.match('[a-z]+',tags[0])):
			wshape='aa' """
		word=tags[0]
		features=[]
		if(len(word) >= 4):
			
		
			features.append("prefix=%s" % word[0:1].lower())
			features.append("prefix=%s" % word[0:2].lower())
			features.append("prefix=%s" % word[0:3].lower())
			features.append("suffix=%s" % word[len(word)-1:len(word)].lower())
			features.append("suffix=%s" % word[len(word)-2:len(word)].lower())
			features.append("suffix=%s" % word[len(word)-3:len(word)].lower())
		#Substring features (don't seem to help)
		#for i in range(1,len(word)-2):
		# for j in range(i+1,len(word)-1):
		# features.append("substr=%s" % word[i:j])
		if re.search(r'^[A-Z]', word):
			features.append('INITCAP')
		
		if re.match(r'^[A-Z]+$', word):
			features.append('ALLCAP')
		
		if re.match(r'.*[0-9].*', word):
			features.append('HASDIGIT')
		if re.match(r'[0-9]', word):
			features.append('SINGLEDIGIT')
		if re.match(r'[0-9][0-9]', word):
			features.append('DOUBLEDIGIT')
		if re.match(r'.*-.*', word):
			features.append('HASDASH')
		if re.match(r'[.,;:?!-+\'"]', word):
			features.append('PUNCTUATION')
		ft=' '.join(features)	
		#print("%s cw=%s pw=%s nw=%s" % (tags[1],tags[0],prev_word,next_word))
		opf.write("%s %s pt=%s nt=%s %s\n" % (tags[-1],tags[0],prev_word,next_word,ft))
		i+=1
	#if(count):
		#break
pargv=list()
pargv.append("")
pargv.append(temp_model_file)
pargv.append(model_file)	
perceplearn.AVG_Perceptron(pargv)
