# https://snips-nlu.readthedocs.io/en/latest/installation.html

from rasa.nlu.model import Interpreter

interpreter = Interpreter.load("models/nlu")

def getIntent():
    command = listenForCommand()
    result = interpreter.parse(command)
    print(result)


def listenForCommand():
    # Record audio while user is talking (test: 10 seconds)
    # Speech to text (vosk)
    # Return speech
    return input("User: ") # Test output using input string