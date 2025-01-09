import spacy

# Load the trained model
nlp = spacy.load("en_core_web_sm") # intent_model_with_entities

# Function to predict intent and extract entities
def predict_intent_and_extract_entities(text):
    doc = nlp(text)  # Process the input text
    intent = doc.cats  # Get the predicted intent
    entities = [(ent.text, ent.label_) for ent in doc.ents]  # Extract entities
    print(doc.ents)
    return intent, entities

# Test with different inputs
test_inputs = [
    # "Turn on the living room lights",  # Should extract "living room" as ROOM
    # "Set a timer for 10 minutes",      # Should extract "10 minutes" as DURATION
    "Tell me about the Eiffel Tower",  # Should extract "Eiffel Tower" as PLACE
    "Set the living room lamp to 50 percent",
    "Set moodlight to 88 percent"
]

for input_text in test_inputs:
    predicted_intent, extracted_entities = predict_intent_and_extract_entities(input_text)
    print(f"Input: '{input_text}'")
    print("Predicted Intent:", predicted_intent)
    print("Extracted Entities:", extracted_entities)
    print("-" * 40)
