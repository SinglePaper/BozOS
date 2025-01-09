import spacy

trained = spacy.load("SpaCy Intent/sprout_ner")

doc = trained("Set sky to 40 percent")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Save the trained model to disk
trained.to_disk("sprout_ner")