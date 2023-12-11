import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
multiline_text = """
Shekhar is very afraid always.
Dipjyot is very clever.
Saurabh is very handsome

"""
multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print( 
        f"""
        TOKEN: {token.text}
        =====
        {token.tag_ = }
        {token.head.text = }
        {token.dep_ = }
        """
    )

displacy.serve(multiline_doc, style="dep")

'''
TOKEN: 

        =====
        token.tag_ = '_SP'
        token.head.text = 'Shekhar'
        token.dep_ = 'dep'
        

        TOKEN: Shekhar
        =====
        token.tag_ = 'NNP'        
        token.head.text = 'is'    
        token.dep_ = 'nsubj'      
        

        TOKEN: is
        =====
        token.tag_ = 'VBZ'        
        token.head.text = 'is'    
        token.dep_ = 'ROOT'       
        

        TOKEN: very
        =====
        token.tag_ = 'RB'
        token.head.text = 'afraid'
        token.dep_ = 'advmod'     
        

        TOKEN: afraid
        =====
        token.tag_ = 'JJ'
        token.head.text = 'is'    
        token.dep_ = 'acomp'      


        TOKEN: always
        =====
        token.tag_ = 'RB'
        token.head.text = 'is'
        token.dep_ = 'advmod'


        TOKEN: .
        =====
        token.tag_ = '.'
        token.head.text = 'is'
        token.dep_ = 'punct'


        TOKEN:

        =====
        token.tag_ = '_SP'
        token.head.text = '.'
        token.dep_ = 'dep'


        TOKEN: Dipjyot
        =====
        token.tag_ = 'NNP'
        token.head.text = 'is'
        token.dep_ = 'nsubj'


        TOKEN: is
        =====
        token.tag_ = 'VBZ'
        token.head.text = 'is'
        token.dep_ = 'ROOT'


        TOKEN: very
        =====
        token.tag_ = 'RB'
        token.head.text = 'clever'
        token.dep_ = 'advmod'


        TOKEN: clever
        =====
        token.tag_ = 'JJ'
        token.head.text = 'is'
        token.dep_ = 'acomp'


        TOKEN: .
        =====
        token.tag_ = '.'
        token.head.text = 'is'
        token.dep_ = 'punct'


        TOKEN:

        =====
        token.tag_ = '_SP'
        token.head.text = '.'
        token.dep_ = 'dep'


        TOKEN: Saurabh
        =====
        token.tag_ = 'NNP'
        token.head.text = 'is'
        token.dep_ = 'nsubj'


        TOKEN: is
        =====
        token.tag_ = 'VBZ'
        token.head.text = 'is'
        token.dep_ = 'ROOT'


        TOKEN: very
        =====
        token.tag_ = 'RB'
        token.head.text = 'handsome'
        token.dep_ = 'advmod'


        TOKEN: handsome
        =====
        token.tag_ = 'JJ'
        token.head.text = 'is'
        token.dep_ = 'acomp'


        TOKEN:


        =====
        token.tag_ = '_SP'
        token.head.text = 'handsome'
        token.dep_ = 'dep'


Using the 'dep' visualizer
Serving on http://0.0.0.0:5000 ...

127.0.0.1 - - [01/Dec/2023 10:18:05] "GET / HTTP/1.1" 200 13090
127.0.0.1 - - [01/Dec/2023 10:18:06] "GET /favicon.ico HTTP/1.1" 200 13090

'''