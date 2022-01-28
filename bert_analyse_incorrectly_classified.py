from collections import Counter, OrderedDict
import matplotlib.pylab as plt


file = open("bert_testeval.txt", "r")
words, correct_class, wrong_class = [], [], []

for x in file: 
	line = x.split()
	if line:
		if line[1] == line[2]: # only retrieve words that were incorrect
			pass
		else:
			words.append(line[0])
			correct_class.append(line[1])
			wrong_class.append(line[2])
file.close()

print(len(words), len(wrong_class), len(correct_class))
print("-------------------------")

correct_counts = Counter(correct_class)
wrong_counts = Counter(wrong_class)

wrong_counts = dict(sorted(wrong_counts.items(), key=lambda item: item[1], reverse=True))
correct_counts = dict(sorted(correct_counts.items(), key=lambda item: item[1], reverse=True))

print("wrong counts:\n", wrong_counts)
print("-------------------------")
print("correct counts:\n", correct_counts)
print("-------------------------")
print("percentage of wrong_counts:")
percent = dict((x, round((value/310)*100, 2)) for x,value in wrong_counts.items())
print(percent)

print("-------------------------")

x_wrong = [] # keys
y_wrong = [] # values
for key, value in wrong_counts.items():
	if len(x_wrong) < 15:
		x_wrong.append(key)
		y_wrong.append(value)
'''plt.bar(x_wrong,y_wrong, color = 'green')
plt.show()
'''
print(x_wrong)
print(y_wrong)

print("-------------------------")

x = [] # keys
y = [] # values
for key, value in correct_counts.items():
	if len(x) < 15:
		x.append(key)
		percentage = (value / 310) * 100
		y.append(round(percentage, 2))

plt.bar(x,y, color = 'green')

for i in range(len(x)):
    plt.text(i, y[i]/2, y[i], ha = 'center', fontsize = 12, fontweight='bold')

plt.title('Percentages of the Incorrectly Classified Semantic Tags by the BERT Model', fontsize = 18, fontweight='bold')
plt.xlabel('Semantic tag', fontweight='bold', fontsize = 14)
plt.ylabel('Percentage of Incorrectly Classified Words', fontweight='bold', fontsize = 14)
#plt.savefig("incorrectly_classified_baseline.png")
plt.show()
