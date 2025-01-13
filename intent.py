import spacy

trained = spacy.load("SpaCy Intent/sprout_ner")

doc = trained("Set sky to 40 percent")
for ent in doc.ents:
    print(ent.text, ent.label_)

def getIntent():
    prompt = input("Prompt: ")
    doc = trained(prompt)
    print("\nDetected Parameters\n=================")
    for ent in doc.ents:
        print(ent.text, ent.label_)