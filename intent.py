import spacy

conf_value = 0.5

textcat = spacy.load("SpaCy Intent/textcat_model/model-best")
ner = spacy.load("SpaCy Intent/sprout_ner")

doc = textcat("Set sky to 40 percent")    
print(dict((k, v) for k, v in doc.cats.items() if v >= conf_value))

doc = ner("Set sky to 40 percent")
for ent in doc.ents:
    print(ent.text, ent.label_)

    

def getIntent():
    prompt = input("Prompt: ")

    doc = textcat(prompt)    
    print("\nDetected Intent\n=================")
    print(dict((k, v) for k, v in doc.cats.items() if v >= conf_value))

    doc = ner(prompt)
    print("\nDetected Parameters\n=================")
    for ent in doc.ents:
        print(ent.text, ent.label_)
