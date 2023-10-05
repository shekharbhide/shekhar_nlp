import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess

doc_list = [
   "Natural language processing (NLP) is a subfield of Artificial Intelligence (AI).", 
   "This technology works on the speech provided by the user breaks it down for proper understanding and processes it accordingly.", 
   "This is a very recent and effective approach due to which it has a really high demand in today’s market. "
   "Natural Language Processing (NLP) is a subfield of artificial intelligence that deals with the interaction between computers and humans in natural language."
   
]

doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
print(BoW_corpus)
print("--------------------------------------------------------------------------------------------------------")
id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
print(id_words)