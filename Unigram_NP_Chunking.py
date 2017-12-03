#1. unigram chunker with NP

import nltk

class UnigramChunker(nltk.ChunkParserI):
    def __init__(self, t_sents):
        td = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(s)]
                      for s in t_sents]
        self.tagger = nltk.UnigramTagger(td)

    def parse(self, s):
        postags = [p for (w,p) in s]
        t_postags = self.tagger.tag(postags)
        ctags = [ctag for (p, ctag) in t_postags]
        conlltags = [(w, p, ctag) for ((w,p),ctag)
                     in zip(s, ctags)]
        return nltk.chunk.conlltags2tree(conlltags)