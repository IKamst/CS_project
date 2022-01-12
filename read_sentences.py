# Reading the gold standard file 

def read_file(in_file):
    tags = []
    tagged_sents = []
    sentences = []
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
                tags.append({'word': word, 'pos': pos})
                sentences.append(word)
                tagged_sents.append(tagged_sent)
                word, pos, tagged_sent = [], [],[]
                
        if len(word) > 0:
            tags.append({'word': word, 'pos': pos})
            tagged_sents.append(tagged_sent)
    return sentences, tags, tagged_sents

'''
ID:     sp[0] styling 
FORM:   sp[1] styling 
LEMMA:  sp[2] style 
POS:    sp[3] EXG 
FEAT:   sp[4] (s:ng\np)/np  
HEAD:   sp[5] style.v.02  
DEPREL: sp[6] [Patient,Agent]
'''
'''file = "gold_data/train.conll"

sentences, tags, tagged_sents = read_file(file)
print(sentences[0])
print(tags[0]["word"], tags[0]["pos"])
print(tags[0]["word"][0], tags[0]["pos"][0])
print(tagged_sents[0])'''