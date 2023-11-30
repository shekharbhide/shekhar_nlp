"""
Asg No 4
Name - Shekhar Bhide
Batch - B1
Roll - 6
Title: Implement Bi-gram, Tri-gram word sequence and its count in text inputs or twitter data
using NLTK library
"""
from nltk import ngrams

# Unigram model
n = 1
sentence = '''Your smile makes me smile Your laugh makes me laugh Your eyes are enchanting You make my thoughts seem daft Since the day I first laid eyes on you My feelings grew and grew In that first conversation my knees clicked and clacked And those butterflies flipped and flapped And as I spill these simple rhymes My mind goes over time and time I have a crush, a little teenage crush I dont know what to do, about this lovely little crush'''
unigrams = ngrams(sentence.split(), n)
for item in unigrams:
    print(item)

# Bigram model
n = 2
sentence = '''Your smile makes me smile Your laugh makes me laugh Your eyes are enchanting You make my thoughts seem daft Since the day I first laid eyes on you My feelings grew and grew In that first conversation my knees clicked and clacked And those butterflies flipped and flapped And as I spill these simple rhymes My mind goes over time and time I have a crush, a little teenage crush I dont know what to do, about this lovely little crush'''
bigrams = ngrams(sentence.split(), n)
for item in bigrams:
    print(item)

# Trigram model
n = 3
sentence = '''Your smile makes me smile Your laugh makes me laugh Your eyes are enchanting You make my thoughts seem daft Since the day I first laid eyes on you My feelings grew and grew In that first conversation my knees clicked and clacked And those butterflies flipped and flapped And as I spill these simple rhymes My mind goes over time and time I have a crush, a little teenage crush I dont know what to do, about this lovely little crush'''
trigrams = ngrams(sentence.split(), n)
for item in trigrams:
    print(item)

# Using text file input
file = open("/home/exam/Awesome-NLP/Num.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
    print()

# OUTPUT -
'''
('Your',)
('smile',)
('makes',)
('me',)
('smile',)
('Your', 'smile')
('smile', 'makes')
('makes', 'me')
('me', 'smile')
('smile', 'Your')
('Your', 'laugh')
('laugh', 'makes')
('makes', 'me')
('Your', 'smile', 'makes')
('smile', 'makes', 'me')
('makes', 'me', 'smile')
('me', 'smile', 'Your')
('smile', 'Your', 'laugh')
('Your', 'laugh', 'makes')
('laugh', 'makes', 'me')
('makes', 'me', 'laugh')
('me', 'laugh', 'Your')
('grew', 'In', 'that')
('In', 'that', 'first')
('that', 'first', 'conversation')
('first', 'conversation', 'my')
('conversation', 'my', 'knees')
('my', 'knees', 'clicked')
('knees', 'clicked', 'and')
('clicked', 'and', 'clacked')
('and', 'clacked', 'And')
('clacked', 'And', 'those')
('And', 'those', 'butterflies')
('those', 'butterflies', 'flipped')
('butterflies', 'flipped', 'and')

'''
