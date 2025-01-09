import spacy
from spacy.training import Example

# Create a blank English model
nlp = spacy.blank("en")

# Create a new pipeline with the text categorizer
text_cat = nlp.add_pipe("textcat", last=True)

# Add labels for the intents
text_cat.add_label("animal_of_the_day")
text_cat.add_label("control_lights")
text_cat.add_label("play_music")
text_cat.add_label("set_timer")
text_cat.add_label("ask_information")
text_cat.add_label("set_brightness")
text_cat.add_label("casting")

# Add the NER component
ner = nlp.add_pipe("ner", before="textcat")

# Add labels for the entities
ner.add_label("ROOM")
ner.add_label("BRIGHTNESS")

# TRAINING_DATA = [
#     ("What's the animal of the day?", {"cats": {"animal_of_the_day": 1.0}, "entities": []}),
#     ("Turn on the living room lights", {"cats": {"control_lights": 1.0}, "entities": [(12, 23, "ROOM")]}),
#     ("Play some music", {"cats": {"play_music": 1.0}, "entities": []}),
#     ("Set a timer for 10 minutes", {"cats": {"set_timer": 1.0}, "entities": [(16, 26, "DURATION")]}),
#     ("Tell me about the Eiffel Tower", {"cats": {"ask_information": 1.0}, "entities": [(18, 30, "PLACE")]}),
#     ("Cast Spotify to my speaker", {"cats": {"casting": 1.0}, "entities": [(5, 12, "SERVICE")]}),
# ]

TRAINING_DATA = [
    (u"Set the living room lamp to 50 percent ", {"cats": {"set_brightness": 1.0}, "entities": [(8, 19, "ROOM"), (28, 30, "BRIGHTNESS")]}),
    (u"Dim the bedroom light to 30 percent ", {"cats": {"set_brightness": 1.0}, "entities": [(8, 15, "ROOM"), (25, 27, "BRIGHTNESS")]}),
    (u"Brighten the kitchen lamp to 70 percent ", {"cats": {"set_brightness": 1.0}, "entities": [(13, 20, "ROOM"), (29, 31, "BRIGHTNESS")]}),
    (u"Turn the office light down to 20 percent ", {"cats": {"set_brightness": 1.0}, "entities": [(9, 15, "ROOM"), (30, 32, "BRIGHTNESS")]}),
    (u"Set the hallway lamp to maximum brightness ", {"cats": {"set_brightness": 1.0}, "entities": [(8, 15, "ROOM"), (24, 31, "BRIGHTNESS")]}),
    # ("Lower the brightness of the dining room light", {"cats": {"set_brightness": 1.0}, "entities": [(30, 43, "ROOM")]}),
    # ("Make the living room lamp brighter", {"cats": {"set_brightness": 1.0}, "entities": [(20, 37, "ROOM")]}),
    # ("Set the brightness of the lamp to 10%", {"cats": {"set_brightness": 1.0}, "entities": [(30, 34, "BRIGHTNESS")]}),
    # ("Adjust the brightness of the study light to 40%", {"cats": {"set_brightness": 1.0}, "entities": [(36, 41, "ROOM"), (47, 49, "BRIGHTNESS")]}),
    # ("Turn the lamp in the living room to 80 percent", {"cats": {"set_brightness": 1.0}, "entities": [(30, 43, "ROOM"), (47, 49, "BRIGHTNESS")]}),
]

# Prepare the training examples
train_examples = []
for text, annotations in TRAINING_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    train_examples.append(example)

# Train the model
nlp.initialize()
for epoch in range(10):  # Number of training epochs
    nlp.update(train_examples)

# Save the model
nlp.to_disk("intent_model_with_entities")
