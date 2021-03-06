#!/usr/bin/python3
import sys
import math
import collections
import pickle
import re
import io

if(len(sys.argv) == 2):
	model_file = str(sys.argv[1])
else:
	print("Invalid Arguments.\nUsage: netag.py MODEL_FILE")
	sys.exit()

model={}
avg_feature_vector=collections.defaultdict(dict)
model=pickle.load(open(model_file,"rb"))
classes={}
classes=model[0]
avg_feature_vector=model[1]
#print(avg_feature_vector)
#print(classes)
temp_file="temp_file"

count=0
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8',errors='replace')
for line in input_stream:
	opf = open(temp_file,"w")
	words=line.split()
	l=len(words)
	i=0
	for word in words:
		if(i!=0):
			prev_word=words[i-1]
		else:
			prev_word='Bos'
		if(i!=l-1):
			next_word=words[i+1]
		else:
			next_word='Eos'
		#print('word=',word)
		tags=word
		
		#print('tag=',tags)
		"""
		wshape='a'
		if(re.match('^[A-Z]+$',tags)):
			wshape='AA'
		if(re.match('^[A-Z][a-z]+$',tags)):
			wshape='Aa'
		if(re.match('^[0-9]+$',tags)):
			wshape='9'
		if(re.match('^[a-z]+$',tags)):
			wshape='aa' """
		word=' '.join(word.split('/')[0:-1])
		#print("word=",word)
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
		#print("%s pt=%s nt=%s\n" % (tags,prev_word,next_word))
		#opf.write("%s pt=%s nt=%s\n" % (tags,prev_word,next_word))
		#opf.write("%s pw=%s nw=%s %s\n" % (tags,prev_word,next_word,ft))
		opf.write("%s pw=%s nw=%s %s\n" % (tags,prev_word,next_word,ft))
		i+=1
	count+=1
	#if(count):
		#break
	#	sys.exit()
	opf.close()
	tf=open(temp_file,"r")	
	for lin in tf:
		for c in classes:
			classes[c]=0
			feature=lin.split()
			#print(feature)
			for ft in feature:
				if(avg_feature_vector[ft].get(c)):
					classes[c]+=avg_feature_vector[ft][c]
			#print("classes=",classes[c])
		max = -999
		for c  in classes:
			if(classes[c]>max):
				max=classes[c]
				found_class=c
		sys.stdout.write(feature[0]+'/'+found_class+' ')
	sys.stdout.write('\n')
	
