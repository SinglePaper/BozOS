# https://snips-nlu.readthedocs.io/en/latest/installation.html

def getIntent():
    listenForCommand()
    print("Intent: WAHOO")


def listenForCommand():
    # Record audio while user is talking (test: 10 seconds)
    # Speech to text
    # Return speech
    return input("User: ") # Test output using input string