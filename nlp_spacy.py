import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("hi this wasn't a sample text!")
print(doc.text.split())
tokens = []
for token in doc:
    tokens.append(token)

print(tokens)  #tokenrepresentation
print([token.orth_ for token in doc]) #token representation as string
