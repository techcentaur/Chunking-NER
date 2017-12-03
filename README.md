# Chunking-NER
Chunking Data techniques in Named Entity Recognition(NER) using NLP libraries and algorithms

Chunking Data Algorithms and techniques are used for named entity recognition. We first take the text-data from a file and then tokenize its data into a list of words.

After it we need to extract the information from the data given to make the machine learn for future assertions

So, we will go through simple steps as:

> Tokens --> POS tags --> Chunking --> Named Entity Detection and Recognition --> Relation Extraction --> Understanding and Evaluating Relationships

### Chunking -
 It involves the techniques for entity detection.

**Regex chunking**

1. Simple Regular expression (Regex) based NP(Noun phrase) based chunker

[Code]()

### Chinking -
It involves the techniques for a sequence of tokens that isn't included in a chunk.

[Code]()

2. Simple Regular expression (Regex) based NP(Noun phrase) based chinker

**n-gram chunking**

3. This techniques uses IOB format which means it gives a B-NP tag when chunking Noun-Phrase at the beginning and the next tag if included in the chunk it will give it a I-NP tag, if it doesn't lie in the tag it will give it a O tag
(NP doesn't need to be tagged here)

[Code](code)

It uses **IOB** format to determine the position of chunk in the sentence.


> These are some common chunking techniques and contributed by [Techcentaur]() , Contributions and Pull-Requests are welcome