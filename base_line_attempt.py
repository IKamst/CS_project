# try at a baseline using TnT with demo() from https://www.nltk.org/_modules/nltk/tag/tnt.html#demo

import nltk
from nltk.tag import TnT

from read_sentences import read_file


file = "gold_data/train.conll"

sentences, dictionary, tagged_sents = read_file(file)

sents = list(tagged_sents)
test = list(sentences)

tagger = TnT()
tagger.train(sents[200:1000])

tagged_data = tagger.tagdata(test[100:120])

num_correct = 0
num_words = 0

for j in range(len(tagged_data)):
	s = tagged_data[j]
	t = sents[j+100]
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
