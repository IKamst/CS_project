from collections import Counter, OrderedDict
import matplotlib.pylab as plt


file = open("incorrectly_classified_baseline.txt", "r")

words, wrong_class, correct_class = [], [], []

for x in file: 
	line = x.split()
	if line[2] == "correct_class":
		pass
	else:
		words.append(line[0])
		wrong_class.append(line[1])
		correct_class.append(line[2])
file.close()

correct_counts = Counter(correct_class)
wrong_counts = Counter(wrong_class)

correct_counts = dict(sorted(correct_counts.items(), key=lambda item: item[1], reverse=True))

x = [] # keys
y = [] # values
for key, value in correct_counts.items():
	if value >= 10:
		x.append(key)
		y.append(value)
plt.bar(x,y, color = 'green')

for i in range(len(x)):
    plt.text(i, y[i]//2, y[i], ha = 'center', fontsize = 8, fontweight='bold')


plt.title('Occurences of the Incorrectly Classified Semnatic Tags by the Baseline', fontsize = 14, fontweight='bold', fontfamily='serif')
plt.xlabel('Semantic tag', fontweight='bold', fontfamily='serif', fontsize = 12)
plt.ylabel('Number of occurences', fontweight='bold', fontfamily='serif', fontsize = 12)
#plt.savefig("incorrectly_classified_baseline.png")
plt.show()


