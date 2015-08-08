Usage:
------
./perceplearn.py <TRAININGFILE> <MODELFILE>

./percepclassify.py <MODELFILE> <STDIN> <STDOUT>

./postrain.py <TRAININGFILE> <MODELFILE>

./postag.py <MODELFILE> <STDIN> <STDOUT>

./nelearn.py <TRAININGFILE> <MODELFILE>

./netag.py <MODELFILE> <STDIN> <STDOUT>

Output Files:
-------------
Part 2: pos.test.out

Part 3: ner.esp.test.out

Q&A:
----
1.What is the accuracy of your part-of-speech tagger?

no_of_correctly_tagged_tokens/total_no_of_tokens =   38558/40117 * 100 = 96.1138

2.What are the precision, recall and F-score for each of the named entity types for your named entity recognizer, and what is the overall F-score?

Location:
Precision = 577/936 = 0.62
Recall = 577/984 = 0.59
F-Score = 0.6046

Person:
Precision = 776/1118 = 0.694
Recall = 776/1222 = 0.64
F-Score = 0.6659

Organization:
Precision = 1121/1776 = 0.63
Recall = 1121/1700 = 0.66
F-Score = 0.6446

Miscellaneous:
Precision = 200/394 = 0.51
Recall = 200/445 = 0.45
F-Score = 0.478

Overall F-score:
Precision = 2674/4224 = 0.633
Recall = 2674/4351 = 0.6145
F-Score = 0.6236

3.What happens if you use your Naive Bayes classifier instead of your perceptron classifier (report performance metrics)? Why do you think that is?

 Since Naive Bayes assumes that all the features are independent of each other, we are losing the context while doing POS and also NER.
 Accuarcy of POS is 35707/40117 = 89% 
 NER:
 Precision = 1987/4224= 0.47
 Recall =  1987/4351 = 0.456
 F-Score = 0.462

