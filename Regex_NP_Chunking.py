#1. Simple Regular expression (Regex) based NP(Noun phrase) based chunker

import nltk

def regex_chunking(tokens):
    sent = nltk.pos_tag(tokens)
    regex = "NP: {<DT><JJ>*<NN>}"
    t= nltk.RegexpParser(regex)
    r = t.parse(sent)
    return r

#The output contains a formatted tree with NP-chunked
