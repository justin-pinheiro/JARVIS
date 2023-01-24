import os
import requests
import playsound
import keys

def createAudioSpeechFromText(text, language, voice, path) -> None:
    response = requests.get(f'http://api.voicerss.org/?key={keys.TTS_KEY}&hl={language}&v={voice}&src={text}&r=2&c=mp3')
    with open(path, 'wb') as file:
        file.write(response.content)

def playAudioFile(path) -> None:
    with open(path, 'rb') as file:
        playsound.playsound(path)
        file.close()

def removeAudioFile(path) -> None:
    os.remove(path)