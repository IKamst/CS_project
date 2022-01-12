# try at a baseline using TnT with demo() from https://www.nltk.org/_modules/nltk/tag/tnt.html#demo

import nltk
from nltk.tag import TnT
from nltk.metrics.scores import (precision, recall)

from read_sentences import read_file


train_file = "gold_data/train.conll"
validation_file = "gold_data/dev.conll"

train_sentences, train_dictionary, train_tagged_sents = read_file(train_file)
validation_sentences, validation_dictionary, validation_tagged_sents = read_file(validation_file)

train_tagged = list(train_tagged_sents)
validation_sents = list(validation_sentences)
validation_tagged = list(validation_tagged_sents)

tagger = TnT()
tagger.train(train_tagged)


output = tagger.tagdata(validation_sents)

num_correct = 0
num_words = 0

for j in range(len(output)):
	s = output[j]
	t = validation_tagged[j]
	for i in range(len(s)):
		print(s[i], "--", t[i])
		if s[i][1] == t[i][1]:
			num_correct += 1
	num_words += len(s)
	print()

print(num_correct)
print(num_words)

word_accuracy = num_correct / num_words
print("word_accuracy = ", word_accuracy)
