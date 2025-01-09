# import json

# def annotate_sentences(input_file, output_file):
#     """
#     Annotate sentences for NER and save them in SpaCy-compatible format.

#     Args:
#         input_file (str): Path to the input text file containing sentences (one per line).
#         output_file (str): Path to save the annotated data in JSON format.
#     """
#     annotations = []

#     # Read sentences from the input file
#     with open(input_file, 'r', encoding='utf-8') as f:
#         sentences = f.readlines()

#     for sentence in sentences:
#         sentence = sentence.strip()
#         if not sentence:
#             continue

#         print("\nSentence:")
#         print(sentence)
#         print("\nIndices:")

#         # Display character indices spaced out
#         indices = " ".join(f"{i:2}" for i in range(len(sentence)))
#         print("  ".join(sentence))
#         print(indices.strip())

#         entities = []
#         while True:
#             # Get entity start index
#             start = input("Enter start index of entity (or press Enter to finish): ")
#             if not start.strip():
#                 break

#             try:
#                 start = int(start)
#             except ValueError:
#                 print("Invalid input. Please enter a valid index.")
#                 continue

#             # Get entity end index
#             end = input("Enter end index of entity: ")
#             try:
#                 end = int(end)+1
#             except ValueError:
#                 print("Invalid input. Please enter a valid index.")
#                 continue

#             # Get entity label
#             label = input("Enter label for the entity (e.g., PERSON, ORG, etc.): ")
#             if not label.strip():
#                 print("Label cannot be empty.")
#                 continue

#             # Append the entity annotation
#             entities.append((start, end, label))

#         # Add the annotated sentence to the list
#         annotations.append((sentence, {"entities": entities}))

#     # Save annotations to the output file in JSON format
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(annotations, f, ensure_ascii=False, indent=4)

#     print(f"\nAnnotations saved to {output_file}")

# # Usage
# # Provide the input and output file paths
# input_file = "data/raw_data.txt"  # Replace with your input file path
# output_file = "data/annotated_data.json"  # Replace with your desired output file path

# annotate_sentences(input_file, output_file)


import json

def annotate_sentences(input_file, output_file):
    """
    Annotate sentences for NER and save them in SpaCy-compatible format.

    Args:
        input_file (str): Path to the input text file containing sentences (one per line).
        output_file (str): Path to save the annotated data in JSON format.
    """
    annotations = []
    unique_intents = set()

    # Read sentences from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    try:
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            print("\nSentence:")
            print(sentence)
            print("\nIndices:")

            # Display character indices spaced out
            indices = " ".join(f"{i:2}" for i in range(len(sentence)))
            print("  ".join(sentence))
            print(indices.strip())

            # Ask for intent recognition question
            intent = input("What is the intent of this sentence? (e.g., question, command, etc.): ").strip()
            if not intent:
                print("Intent cannot be empty. Defaulting to 'unknown'.")
                intent = "unknown"
            else:
                unique_intents.add(intent)

            entities = []
            while True:
                # Get entity start index
                start = input("Enter start index of entity (or press Enter to finish): ")
                if not start.strip():
                    break

                try:
                    start = int(start)
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
                    continue

                # Get entity end index
                end = input("Enter end index of entity: ")
                try:
                    end = int(end)+1
                except ValueError:
                    print("Invalid input. Please enter a valid index.")
                    continue

                # Get entity label
                label = input("Enter label for the entity (e.g., PERSON, ORG, etc.): ")
                if not label.strip():
                    print("Label cannot be empty.")
                    continue

                # Append the entity annotation
                entities.append((start, end, label))

            # Add the annotated sentence to the list
            annotations.append((sentence, {"intent": intent, "entities": entities}))

            with open(f"{output_file[:-5]}_{intent}.json", 'a', encoding='utf-8') as f:
                f.write(sentence+"\n")
    except KeyboardInterrupt:
        pass
    # Save annotations to the output file in JSON format
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(annotations, f, ensure_ascii=False, indent=4)
    

    print(f"\nAnnotations saved to {output_file}")

# Usage
# Provide the input and output file paths
input_file = "data/raw_data.txt"  # Replace with your input file path
output_file = "data/annotated_data.json"  # Replace with your desired output file path


annotate_sentences(input_file, output_file)
