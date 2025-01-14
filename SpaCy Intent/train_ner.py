import spacy
import json
import random
from spacy.training import Example

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Ensure the data is formatted for SpaCy training
    formatted_data = [(text, {"entities": annotations["entities"]}) for text, annotations in data]
    return formatted_data

def train_spacy(train_data, iterations):
    # Create a blank English model
    nlp = spacy.blank("en")
    
    # Create the NER component and add it to the pipeline
    ner = nlp.add_pipe("ner", last=True)
    ner.add_label("DEVICE")
    ner.add_label("STATUS")
    ner.add_label("COLOR")

    # Start the training process
    optimizer = nlp.begin_training()
    
    for itn in range(iterations):
        print(f"Starting iteration {itn}")
        random.shuffle(train_data)
        losses = {}
        
        for text, annotations in train_data:
            # Create Example objects for training
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.2, losses=losses)
        
        print(losses)
    
    return nlp

# Load training data
train_data = load_data("data/annotated_data.json")
random.shuffle(train_data)

# Train the model
trained = train_spacy(train_data, 50)

# Test the trained model
doc = trained("Set ceiling to 5 percent")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Save the trained model to disk
trained.to_disk("sprout_ner")
