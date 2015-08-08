#!/usr/bin/python3
import sys
import collections
import pickle
if(len(sys.argv) == 2):
	model_file = str(sys.argv[1])
	#test_file= str(sys.argv[2])
else:
	print("Invalid Arguments.\nUsage: ./percepclassify.py MODEL_FILE")
	sys.exit()
	#test_file="dev_file.txt"
	#output_file="spam.out"
	#model_file="percep_model"
#output_file="spam.out"
model={}
avg_feature_vector=collections.defaultdict(dict)
model=pickle.load(open(model_file,"rb"))
classes={}
classes=model[0]
avg_feature_vector=model[1]

#print(avg_feature_vector)
#print(classes)
#ipf=open(test_file,"r")
#opf=open(output_file,"w")
#for line in ipf:
for line in sys.stdin:
	for c in classes:
		classes[c]=0
		features=line.split()
		for ft in features:
			if(avg_feature_vector[ft].get(c)):
				classes[c]+=avg_feature_vector[ft][c]
		#print("classes=",classes[c])
	max = -999
	for c  in classes:
		if(classes[c]>max):
			max=classes[c]
			found_class=c
	sys.stdout.write(found_class+"\n")
	#opf.write(found_class+"\n")
