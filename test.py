import sys
import os
import requests
import wave
import dotenv
import uuid
import urllib
# import pocketsphinx as ps
import speech_recognition as sr
import pyaudio


class Command():
    def __init__(self, content):
        self.content = content
        self.action = self.detectAction()
        self.length = 0

    def detectAction(self):
        # if self.content.sta
        pass

class TTSContext():

    def __init__(self, key, voice='Axel', lang='en-us', rate=140):
        self.__key = key
        self.voice = voice
        self.lang = lang
        self.rate = rate
        self.path = ""

    def __getUrl(self, text):
        text = urllib.parse(text)
        self.url = f'http://api.voicerss.org/?key={self.__key}&hl={self.lang}&v={self.voice}&r=2&c=wav&src={text}'

    def playCommand(self, text, remove=True):
        CHUNK = 1024
        res = requests.get(self.__getUrl(text))
        self.path = f"./audiosamples/{uuid.uuid4()}.wav"
        with open(self.path, 'wb') as f:
            f.write(res.content)
        with wave.open(self.path, 'rb') as wf:
            p = pyaudio.PyAudio()
            waveformat = p.get_format_from_width(wf.getsampwidth())
            wavechannels = wf.getnchannels()
            waverate = wf.getframerate()
            stream = p.open(format=waveformat,
                            channels=wavechannels, rate=waverate, output=True)
            while len(data := wf.readframes(CHUNK)):
                stream.write(data)
            stream.close()
            p.terminate()
        if (remove):
            os.remove(self.path)
            return None
        else:
            return self.path


class MicContext():
    def __init__(self):
        self.reco = sr.Recognizer()
        self.mic = sr.Microphone()
        self.sentence

    def getCommand(self):
        with self.mic as source:
            self.reco.adjust_for_ambient_noise(source)
            audio = self.reco.listen(source)
            try:
                return Command(self.reco.recognize_sphinx(audio))
            except:
                raise

class AiContext():
    def __init__():
        pass
#         # text recognition and response
#         response = ia.getResponseFromGPT3ViaPrompt(
#             "text-babbage-001", question)
#         print("\nJARVIS : " + response)


class Jarvis():
    def __init__(self):
        dotenv.load_dotenv()
        self.voiceID = None
        self.voiceRate = 150
        self.key_openAI = os.environ.get('OPENAI_KEY')
        self.ttsctx = TTSContext(os.environ.get('TTS_KEY'), 'Axel', 'fr-fr')
        self.micctx = MicContext()
        self.running = True
        self.say("Initialisation du système")
        self.say("Système opérationnel")
        self.say("Bonjour, Monsieur")
        self.say("Je suis à votre écoute")
        while self.running:
            try:
                question = self.listen()
                # if question.isCmd:
                #     pass
                # gerer si la fonction est une commande on appelle le gestionnaire etc 
                answer = self.processAnswer(question)
                self.say(answer)
            except: pass # on passe au Q&A suivant
        self.say("Arrêt du système")
            

    def say(self, text):
        print(f"JARVIS \t: {text}")
        self.ttsctx.playCommand(text)

    def listen(self):
        print(f"YOU \t: ...", end='\b')
        try:
            return self.micctx.getCommand()
        except sr.UnknownValueError:
            self.say("Je n'ai pas compris votre requete, je vous prie de reformuler votre requête Monsieur")
            raise
        except sr.RequestError:
            self.say("Je n'ai pas pu vous comprendre car la requète sphinx à rencontré une erreur. Vous pouvez réessayer Monsieur")
            raise

    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        self.running = False
    
    def cmdManager(self, cmd):
        pass
        # if()


if __name__ == "__main__":
    jarvis = Jarvis()
