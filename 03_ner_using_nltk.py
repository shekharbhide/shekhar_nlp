# Using NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

raw_text="""The Board of Control for Cricket in India (BCCI) is the 
governing body for cricket in India and is under the jurisdiction 
of Ministry of Youth Affairs and Sports, Government of India.[2] 
The board was formed in December 1928 as a society, registered under the 
Tamil Nadu Societies Registration Act. It is a consortium of 
state cricket associations and the state associations select 
their representatives who in turn elect the BCCI Chief. Its headquarters 
are in Wankhede Stadium, Mumbai. Grant Govan was its first president and 
Anthony De Mello its first secretary. """

import nltk
nltk.download('all')
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('treebank')
sent = nltk.corpus.treebank.tagged_sents()
print(nltk.ne_chunk(sent[0]))

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
raw_words= word_tokenize(raw_text)
tags=pos_tag(raw_words)
nltk.download('maxent_ne_chunker')
nltk.download('words')
ne = nltk.ne_chunk(tags,binary=True)
print(ne)
from nltk.chunk import tree2conlltags
iob = tree2conlltags(ne)
iob