# A baseline using TnT with demo() from https://www.nltk.org/_modules/nltk/tag/tnt.html#demo
# written by Ella Collins, Iris Kamsteeg & Rik Zijlema 

import nltk
from nltk.tag import TnT
#from nltk.metrics.scores import precision, recall
from collections import defaultdict
from sklearn.metrics import precision_score, accuracy_score, f1_score, recall_score

from read_sentences import read_file # function to properly read the sentences and tags from the file

# the train and validation files
train_file = "gold_data/train.conll"
validation_file = "gold_data/dev.conll"

# loading the data to be used from the files
train_sentences, train_tagged_sents = read_file(train_file)
validation_sentences, validation_tagged_sents = read_file(validation_file)

train_tagged = list(train_tagged_sents)
validation_sents = list(validation_sentences)
validation_tagged = list(validation_tagged_sents)

# create the TnT tagger and train on the training data
tagger = TnT()
tagger.train(train_tagged)

output = tagger.tagdata(validation_sents)

# put the output and validation data in a dictionary format for easy comparison
validation_sets = defaultdict(list)
for sent in validation_tagged:
	for word, sem in sent:
		validation_sets["word"].append(word)
		validation_sets["sem"].append(sem)
output_sets = defaultdict(list) # dictionary with word and sem
for sent in output:
	for word, sem in sent:
		output_sets["word"].append(word)
		output_sets["sem"].append(sem)

# determine the accuracy, precision, recall and F1 score
print("Validation accuracry : ", accuracy_score(validation_sets['sem'], output_sets['sem']))
print("Validation precision: ", precision_score(validation_sets['sem'], output_sets['sem'], average='macro'))
print("Validation recall: ", recall_score(validation_sets['sem'], output_sets['sem'], average='macro'))
print("Validation F1 score: ", f1_score(validation_sets['sem'], output_sets['sem'], average='macro'))

# writing the incorrectly classified words to a file for later inspection (if wanted)
incorrectly_classified = [] # incorrectly_classified has word, classification, correct answer
f = open("incorrectly_classified_baseline.txt", "w")
f.write("word classification correct_class \n")
for j in range(len(output)):
	s = output[j]
	t = validation_tagged[j]
	for i in range(len(s)):
		if s[i][1] != t[i][1]:
			incorrectly_classified.append((s[i][0], s[i][1], t[i][1]))
			f.write("{} {} {} \n".format(s[i][0], s[i][1], t[i][1]))
f.close()
