import os
import requests
import playsound
import keys
import time
from mutagen.mp3 import MP3

def createAudioSpeechFromText(text, language, voice, path) -> None:
    response = requests.get(f'http://api.voicerss.org/?key={keys.TTS_KEY}&hl={language}&v={voice}&src={text}&r=2&c=mp3')
    with open(path, 'wb') as file:
        file.write(response.content)

def playAudioFile(path) -> None:
    with open(path, 'rb') as file:
        playsound.playsound(path)
        audio = MP3("speech.mp3")
        time.sleep(audio.info.length - 2)
        file.close()

def removeAudioFile(path) -> None:
    os.remove(path)