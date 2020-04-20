from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.utils import EndpointConfig
import time
import textToSpeech
import speechAnswer
import urllib.request
import os
from speechToText import speech_to_text

interpreter = NaturalLanguageInterpreter.create('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
cnt = 0
speechAnswer.play_music('./mp3/noneLabel.mp3', volume = 1)
print('Bot đã sẵn sàng trả lởi. Nói "dùng lại để kết thúc"')
while True:
    cnt+=1
    a = speech_to_text()
    print(a)
    if a == 'dừng lại':
        break
    responses = agent.handle_text(a)
    for response in responses:
        link_mp3 = textToSpeech.text_to_speech(response['text']) # convert string "answer" to file .mp3
        time.sleep(5) # wait for FPT server create link mp3
        try:
            urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3') # download file answer.mp3 from FPT server
        except:
            time.sleep(5)
            urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3')
        if os.path.exists('mp3/answer'+ str(cnt) +'.mp3'):
            speechAnswer.play_music('mp3/answer'+ str(cnt) +'.mp3', volume = 1) # play file "answer.mp3"
        else:
            time.sleep(3)
            speechAnswer.play_music('mp3/answer'+ str(cnt) +'.mp3', volume = 1) # play file "answer.mp3"
