#!/usr/bin/python3
import sys
import collections
import pickle

def AVG_Perceptron(argv):
	if(len(argv) == 3):
		training_file = str(argv[1])
		model_file = str(argv[2])
	else:
		print("Invalid Arguments.\nUsage: ./perceplearn.py TRAINING_FILE MODEL_FILE")
		sys.exit()
	
	#opf = open("precep_model_ascii","w")
	ipf = open(training_file,"r")

	feature_vector=collections.defaultdict(dict)
	avg_feature_vector=collections.defaultdict(dict)
	classes={}
	with open(training_file,"r") as ipf:
		for line in ipf:
			class_name = line.split()[0]
			if class_name not in classes:
				classes[class_name]=0;

	#print(classes)
	wrongly_classified=0
	total_docs=0
	with open(training_file,"r") as ipf:
		for line in ipf:
			features = line.split()
			features = features[1:]

			for ft in features:
				feature_vector[ft]={}
				for c in classes:
					feature_vector[ft][c]=0		
			total_docs+=1	

	updated=1
	count=0
	accuracy=0
	while(updated==1 and count<=30):
		updated=0
		wrongly_classified=0
		with open(training_file,"r") as ipf:	
			for line in ipf:
				train_fts = line.split()
				#print("\nline read=",train_fts)
				true_class = train_fts[0]
				train_fts = train_fts[1:]
				#print("true_class=",true_class)	
				for c in classes:
					classes[c]=0
					for ft in train_fts:
						classes[c]+=feature_vector[ft][c]
						#initialize average feature vector
				
				#print("classes contains", classes)		
				max=-9999
				for c in classes:
					if(classes[c]>max):
						max=classes[c]
						class_max=c
				#print("max class=",class_max)
				if(class_max!=true_class):
					updated=1
					wrongly_classified+=1
					#print("updating weights")
					for ft in train_fts:
						feature_vector[ft][true_class]+=1
						feature_vector[ft][class_max]-=1
				
					#print(feature_vector)
	
		#averaged weights
	
		for c in classes:		
			for ft in feature_vector:
				if(count==0):
					avg_feature_vector[ft][c]=0
				else:	
					avg_feature_vector[ft][c]+=feature_vector[ft][c]				
			
			
		count+=1
		accuracy=wrongly_classified/total_docs
		print("iteration no.%d error_rate=%f" % (count,accuracy))
	#print("count=",count)
	model={}
	model[0]=classes
	model[1]=avg_feature_vector
	pickle.dump(model,open(model_file,"wb"))
	#opf.write(str(model))	
		
if __name__ == "__main__":
	AVG_Perceptron(sys.argv)	
			
		
