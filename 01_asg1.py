#import libraries
import spacy
nlp = spacy.load("en_core_web_sm")

#taking input
about_text = (
    "Computer is an electronic device that is designed to work with Information. "
    "Computer can not do anything without"
    "a Program. The First mechanical computer designed "
    "by Charles Babbage was called Analytical Engine."
    )
about_doc = nlp(about_text)


#Sentence Detection
print("Sentence Detection----->")
sentences = list(about_doc.sents)
len(sentences)
2
for sentence in sentences:
    print(f"{sentence[:5]}...")
    
    
#Tokenization
print("Tokenization----->")
for token in about_doc:
  print (token, token.idx)
  
  
#Stop Words
print("Stop Words----->")
import spacy
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)


#Lemmatization
print("Lemmatization----->")
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Part-of-Speech
print("Part-of-Speech----->")
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )





#OUTPUT :

# Sentence Detection----->
# Computer is an electronic device...
# Computer can not do anything...
# The First mechanical computer designed...
# Tokenization----->
# Computer 0
# is 9
# an 12
# electronic 15
# device 26
# that 33
# is 38
# designed 41
# to 50
# work 53
# with 58
# Information 63
# . 74
# Computer 76
# can 85
# not 89
# do 93
# anything 96
# withouta 105
# Program 114
# . 121
# The 123
# First 127
# mechanical 133
# computer 144
# designed 153
# by 162
# Charles 165
# Babbage 173
# was 181
# called 185
# Analytical 192
# Engine 203
# . 209
# Stop Words----->
# wherever
# have
# if
# rather
# few
# regarding
# then
# more
# without
# out
# Lemmatization----->
#             Computer : computer
#                   is : be
#                   is : be
#             designed : design
#             Computer : computer
#                  The : the
#                First : first
#             designed : design
#                  was : be
#               called : call
# Part-of-Speech----->

# TOKEN: Computer
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: an
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: electronic
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: device
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: that
# =====
# TAG: WDT        POS: PRON
# EXPLANATION: wh-determiner

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: designed
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: work
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: with
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: Information
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: Computer
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: can
# =====
# TAG: MD         POS: AUX
# EXPLANATION: verb, modal auxiliary

# TOKEN: not
# =====
# TAG: RB         POS: PART
# EXPLANATION: adverb

# TOKEN: do
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: anything
# =====
# TAG: NN         POS: PRON
# EXPLANATION: noun, singular or mass

# TOKEN: withouta
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Program
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: The
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: First
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: mechanical
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: computer
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: designed
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: by
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: Charles
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Babbage
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: was
# =====
# TAG: VBD        POS: AUX
# EXPLANATION: verb, past tense

# TOKEN: called
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: Analytical
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Engine
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer