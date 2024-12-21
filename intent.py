from rasa.core.agent import Agent
import asyncio
import os

# Function to load the agent from cache or disk
def load_agent(model_path):
    # Check if the agent cache exists
    cache_path = model_path + '.cache'
    if os.path.exists(cache_path):
        print("Loading agent from cache...")
        agent = Agent.load(cache_path)
    else:
        print("Loading agent from disk...")
        agent = Agent.load(model_path)
        # Serialize and persist the agent for future use
        agent.persist(cache_path)
    return agent

model_path = 'RASA Intent/models/nlu-20241221-232155-overcast-moss.tar.gz'
agent = load_agent(model_path)

agent = Agent.load(model_path='RASA Intent/models/nlu-20241221-232155-overcast-moss.tar.gz')
agent.parse_message("Hi")

def getIntent():
    message = listenForMessage()
    result = asyncio.run(agent.parse_message(message))
    # print(result)
    print(f"{result['intent']['name']} ({result['intent']['confidence']})")
    for entity in result["entities"]:
        print(f"{entity['entity']}: {entity['value']} ({entity['confidence_entity']})")


def listenForMessage():
    # Record audio while user is talking (test: 10 seconds)
    # Speech to text (vosk)
    # Return speech
    return input("User: ") # Test output using input string