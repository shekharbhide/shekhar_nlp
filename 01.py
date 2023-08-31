import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
   "Good better best"
     "Never let it rest"
     "Till your good is better "
     " And your better best."
 )
about_doc = nlp(about_text)

for token in about_doc:
  print (token, token.idx)
  


spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
    custom_about_text = (
    "Good better best"
     "Never let it rest"
     "Till your good is better "
     " And your better best."
)
nlp = spacy.load("en_core_web_sm")
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])

