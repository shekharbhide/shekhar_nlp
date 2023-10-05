# 2nd assignmnet BOW

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



# bow output
'''
[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 
1), (8, 1), (9, 1)], [(10, 1), 
(11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 2), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 2), (24, 1), (25, 1), (26, 1), (27, 1)], [(1, 1), (2, 1), (3, 2), (4, 2), (5, 2), (6, 1), (7, 1), (8, 1), (9, 1), (11, 2), (16, 1), (23, 1), (24, 1), (28, 1), (29, 1), (30, 1), (31, 1), (32, 1), (33, 1), (34, 1), (35, 1), (36, 1), (37, 1), (38, 2), (39, 1), (40, 1), (41, 1), (42, 1), (43, 
1), (44, 1), (45, 1), (46, 1), 
--------------------------------------------------------------------------------------------------------
[[('ai', 1), ('artificial', 1), ('intelligence', 1), ('is', 1), 
('language', 1), ('natural', 1), ('nlp', 1), ('of', 1), ('processing', 1), 
('subfield', 1)], [('accordingly', 1), ('and', 1), ('breaks', 1), ('by', 1), 
('down', 1), ('for', 1), ('it', 2), ('on', 1), ('processes', 1), ('proper', 1), 
('provided', 1), ('speech', 1), ('technology', 1), ('the', 2), ('this', 1), 
('understanding', 1), ('user', 1), ('works', 1)], [('artificial', 1), 
('intelligence', 1), ('is', 2), ('language', 2), ('natural', 2), ('nlp', 1), 
('of', 1), ('processing', 1), ('subfield', 1), ('and', 2), ('it', 1), 
('the', 1), ('this', 1), ('approach', 1), ('between', 1), ('computers', 1), ('deals', 1), ('demand', 1), ('due', 1), ('effective', 1), ('has', 1), ('high', 1), ('humans', 1), ('in', 2), ('interaction', 1), ('market', 1), ('really', 1), ('recent', 1), ('that', 1), ('to', 1), ('today', 1), ('very', 1), ('which', 1), ('with', 1)]]
'''