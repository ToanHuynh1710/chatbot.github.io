from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter, RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
print("Bot đã sẵn sàng để trò chuyện, nhập 'stop' để kết thúc")
while True:
    print('user: ', end='')
    a = input()
    if a == 'stop':
        break
    for response in responses:
        print('bot:',response["text"])