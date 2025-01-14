import spacy

conf_value = 0.5

nlp = spacy.load("textcat_model/model-best")
while True: 
    doc = nlp(input("Input: "))
    print(dict((k, v) for k, v in doc.cats.items() if v >= conf_value))
