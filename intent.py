from rasa.core.agent import Agent
import asyncio

agent = Agent.load(model_path='20241218-223527-threaded-mango.tar.gz')

def getIntent():
    message = listenForMessage()
    result = asyncio.run(agent.parse_message(message))
    print(result)


def listenForMessage():
    # Record audio while user is talking (test: 10 seconds)
    # Speech to text (vosk)
    # Return speech
    return input("User: ") # Test output using input string