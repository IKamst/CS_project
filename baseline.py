# A baseline using TnT with demo() from https://www.nltk.org/_modules/nltk/tag/tnt.html#demo
# written by Ella Collins, Iris Kamsteeg & Rik Zijlema 

import nltk
from nltk.tag import TnT
#from nltk.metrics.scores import precision, recall
from collections import defaultdict
from sklearn.metrics import accuracy_score, classification_report

from read_sentences import read_file # function to properly read the sentences and tags from the file

# the train and validation files
train_file = "gold_data/train.conll"
validation_file = "gold_data/dev.conll"
test_file = "gold_data/test.conll"
eval_file = "gold_data/eval.conll"

# loading the data to be used from the files
train_sentences, train_tagged_sents = read_file(train_file)
validation_sentences, validation_tagged_sents = read_file(validation_file)
test_sentences, test_tagged_sents = read_file(test_file)
eval_sentences, eval_tagged_sents = read_file(eval_file)

train_tagged = list(train_tagged_sents)

validation_sents = list(validation_sentences)
validation_tagged = list(validation_tagged_sents)

final_test_sents = list(test_sentences + eval_sentences)
final_test_tagged = list(test_tagged_sents + eval_tagged_sents)

# create the TnT tagger and train on the training data
tagger = TnT()
print("Training the baseline...\n")
tagger.train(train_tagged)

# predict the validation tags
val_output = tagger.tagdata(validation_sents)

# put the output and validation data in a dictionary format for easy comparison
validation_sets = defaultdict(list)
for sent in validation_tagged:
	for word, sem in sent:
		validation_sets["word"].append(word)
		validation_sets["sem"].append(sem)
val_output_sets = defaultdict(list) # dictionary with word and sem
for sent in val_output:
	for word, sem in sent:
		val_output_sets["word"].append(word)
		val_output_sets["sem"].append(sem)

# determine the accuracy, precision, recall and F1 scores
print("Validation accuracy : ", accuracy_score(y_true = validation_sets['sem'], y_pred= val_output_sets['sem']))
print("Classification report : \n", classification_report(y_true = validation_sets['sem'], y_pred= val_output_sets['sem'], zero_division=0))

# writing the incorrectly classified words to a file for later inspection (if wanted)
incorrectly_classified = [] # incorrectly_classified has word, correct tag, predicted tag
num_words_val = 0
f = open("val_incorrectly_classified_baseline.txt", "w")
for j in range(len(val_output)):
	s = val_output[j]
	t = validation_tagged[j]
	for i in range(len(s)):
		num_words_val +=1
		if s[i][1] != t[i][1]:
			incorrectly_classified.append((s[i][0], t[i][1], s[i][1]))
			f.write("{} {} {} \n".format(s[i][0], t[i][1], s[i][1]))
f.close()

# testing the baseline
print("----------------------")
print("Testing the baseline...\n")
final_output = tagger.tagdata(final_test_sents)

# put the output and testing data in a dictionary format for easy comparison
final_sets = defaultdict(list)
for sent in final_test_tagged:
	for word, sem in sent:
		final_sets["word"].append(word)
		final_sets["sem"].append(sem)
final_output_sets = defaultdict(list) # dictionary with word and sem
for sent in final_output:
	for word, sem in sent:
		final_output_sets["word"].append(word)
		final_output_sets["sem"].append(sem)

# determine the accuracy, precision, recall and F1 scores
print("Testing accuracy : ", accuracy_score(y_true= final_sets['sem'], y_pred= final_output_sets['sem']))
print("Classification report : \n", classification_report(y_true= final_sets['sem'], y_pred= final_output_sets['sem'], zero_division=0))

# writing the incorrectly classified words to a file for later inspection (if wanted)
incorrectly_classified_final = []  # incorrectly_classified_final has word, correct tag, predicted tag
num_words_final = 0
f = open("test_incorrectly_classified_baseline.txt", "w") 
for j in range(len(final_output)):
	s = final_output[j]
	t = final_test_tagged[j]
	for i in range(len(s)):
		num_words_final += 1
		if s[i][1] != t[i][1]:
			incorrectly_classified_final.append((s[i][0], t[i][1], s[i][1]))
			f.write("{} {} {} \n".format(s[i][0], t[i][1], s[i][1]))
f.close()

print("num words val: ", num_words_val)
print("num words final: ", num_words_final)
