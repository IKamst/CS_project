# Reading the gold standard file 

def read_file(in_file):
    tags = []
    sentences = []
    with open(in_file) as f:
        word, pos = [], []
        for line in f.readlines():
            sp = line.strip().split('\t')
            if len(sp) > 1:
                if '#' not in sp[0]:
                    word.append(sp[1])
                    pos.append(sp[3])
            elif len(word) > 0:
                tags.append({'word': word, 'pos': pos})
                sentences.append(" ".join(word))
                word, pos = [], []
                
        if len(word) > 0:
            tags.append({'word': word, 'pos': pos})
    return sentences, tags

'''
ID:     sp[0] styling 
FORM:   sp[1] styling 
LEMMA:  sp[2] style 
POS:    sp[3] EXG 
FEAT:   sp[4] (s:ng\np)/np  
HEAD:   sp[5] style.v.02  
DEPREL: sp[6] [Patient,Agent]
'''
file = "train.conll"

sentences, tags = read_file(file)

