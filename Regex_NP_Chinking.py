#2. Simple Regex based NP chinker

import nltk

def regex_chinker(tokens):
    sent = nltk.pos_tag(tokens)
    regex = """NP:{<.*>+}               
                    }<VBD | IN>+{"""
    # it will chunk everything first and then chink VBD and IN
    t = nltk.RegexpParser(regex)
    r = t.parse(sent)
    return r

#The output contains a formatted tree with NP-chunked
