# import spacy
# # import classy_classification 
# from glob import glob

# def load_data(path):
#     data = {}
#     categories = set()
#     print(f"{path}/annotated_data_*.json")
#     for file in list(glob(f"{path}/annotated_data_*.json")):
#         intent = file.split("data_")[-1].replace(".json", "")
#         examples = [line.strip() for line in open(file).readlines()]
#         data[intent] = examples
#         categories.add(intent)
#     return data, list(categories)

# data, categories = load_data("SpaCy Intent/data/intent classification")
# print(categories)

# nlp = spacy.load("SpaCy Intent/sprout_ner")
# nlp.add_pipe(
#     "textcat",
#     config={
#         "data": data,
#         "model": "spacy"
#     }
# )

# print(nlp("What is today's animal of the day?")._.cats)

from spacy.tokens import DocBin
import spacy
from glob import glob
import json
import random

def load_data(path):
    data = {}
    categories = set()
    for file in list(glob(f"{path}/annotated_data_*.json")):
        intent = file.split("data_")[-1].replace(".json", "")
        examples = [line.strip() for line in open(file).readlines()]
        data[intent] = examples
        categories.add(intent)
    return data, list(categories)

data, categories = load_data("SpaCy Intent/data/intent classification")
print(categories)

train_size = 0.7
test_size = 0.15
val_size = 0.15

def convert():
    nlp = spacy.blank("en")
    db_train = DocBin()
    db_test = DocBin()
    db_val = DocBin()
    
    for cat in categories:
        set_split =  (int(test_size * len(data[cat])) * ["test"]) + (int(val_size * len(data[cat])) * ["val"])
        set_split += ["train"] * int(len(data[cat]) - len(set_split))
        for example in data[cat]:
            doc = nlp.make_doc(example)
            doc.cats = {category: 0 for category in categories}
            doc.cats[cat] = 1
            if set_split[0] == "train":
                db_train.add(doc)
            elif set_split[0] == "test":
                db_test.add(doc)
            elif set_split[0] == "val":
                db_val.add(doc)
            set_split.pop(0)
    db_train.to_disk("train.spacy")
    db_test.to_disk("test.spacy")
    db_val.to_disk("val.spacy")
convert()