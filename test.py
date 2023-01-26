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


class Sentence():
    def __init__(self, content):
        self.content = content
        self.isCmd = self.checkForCmd()
        self.length = 0

    def checkForCmd(self):
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

    def playSentence(self, sentence: Sentence, remove=True):
        CHUNK = 1024
        res = requests.get(self.__getUrl(sentence.content))
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

    def getSentence(self):
        with self.mic as source:
            self.reco.adjust_for_ambient_noise(source)
            audio = self.reco.listen(source)
            try:
                return Sentence(self.reco.recognize_sphinx(audio))
            except:
                raise


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
            prompt = self.listen()
            if prompt.isCmd:
                pass
            answer = self.processAnswer(prompt)
            self.say(answer)
        self.say("Arrêt du système")
            

    def say(self, sentence: Sentence):
        print(f"JARVIS \t: {sentence.text}")
        self.ttsctx.playSentence(sentence)

    def listen(self):
        print(f"YOU \t: ...", end='\b')
        try:
            question = self.micctx.getSentence()

        except sr.UnknownValueError as e:

        except sr.RequestError as e:
            raise e

    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        self.running = False


if __name__ == "__main__":
    jarvis = Jarvis()
