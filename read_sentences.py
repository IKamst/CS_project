# Reading the gold standard files
# written by Ella Collins, Iris Kamsteeg & Rik Zijlema 

def read_file(in_file):
    sentences = []  # array of the sentences
    tagged_sents = []  # array of pairs of words and tags for each sentence
    with open(in_file) as f:
        word, pos, tagged_sent = [], [],[]
        for line in f.readlines():
            sp = line.strip().split('\t')
            if len(sp) > 1:
                if '#' not in sp[0]:
                    word.append(sp[1])
                    pos.append(sp[3])
                    tagged_sent.append((sp[1], sp[3]))
            elif len(word) > 0:
                sentences.append(word)
                tagged_sents.append(tagged_sent)
                word, pos, tagged_sent = [], [],[]
                
        if len(word) > 0:
            tagged_sents.append(tagged_sent)
    return sentences, tagged_sents

'''
format of the sentences in the file with example styling
ID:     sp[0] styling 
FORM:   sp[1] styling 
LEMMA:  sp[2] style 
POS:    sp[3] EXG 
FEAT:   sp[4] (s:ng\np)/np  
HEAD:   sp[5] style.v.02  
DEPREL: sp[6] [Patient,Agent]
'''