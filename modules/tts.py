import os
import requests
import playsound
import keys
import time
from mutagen.mp3 import MP3

audioPath = "audio/speech.mp3"

def createAudioSpeechFromText(text, language_code, voice) -> None:
    response = requests.get(f'http://api.voicerss.org/?key={keys.TTS_KEY}&hl={language_code}&v={voice}&src={text}&r=2&c=mp3')
    with open(audioPath, 'wb') as file:
        file.write(response.content)

def playAudioFile() -> None:
    with open(audioPath, 'rb') as file:
        playsound.playsound(audioPath)
        audio = MP3(audioPath)
        time.sleep(audio.info.length-1)
        file.close()

def removeAudioFile() -> None:
    os.remove(audioPath)

def play(text, language_code, voice):
    createAudioSpeechFromText(text, language_code, voice)
    playAudioFile()
    removeAudioFile()