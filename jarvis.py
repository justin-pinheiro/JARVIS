""" LIBRARIES """

#project libraries

import stt
import ia
import tts
import MusicPlayer


""" PROGRAM """

def startJARVIS() -> None:
    
    print("\nJARVIS : " + "Initialisation du système... Système opérationnel. Bonjour, Monsieur.")
    tts.playAudioFile('initSpeech.mp3')

#JARVIS Program
def runJARVIS() -> None:

    print("Jarvis enabled")

    #startJARVIS()
    
    run = True
    
    while(run):

        #speech to text
        question : str
        question = ""
        while (question == ""):
            question = stt.getTextFromMicrophoneRecord()

        print("\nMOI : " + question)

        #text recognition and response
        response : str
        response = ia.getResponseFromGPT3ViaPrompt("text-babbage-001", question)

        print("\nJARVIS : " + response)

        #text to speech
        tts.createAudioSpeechFromText(response, 'fr-fr', 'Axel', 'speech.mp3')
        tts.playAudioFile('speech.mp3')
        tts.removeAudioFile('speech.mp3')

        #Lecteur de commandes
        if "Je lance la musique" in response:
            MusicPlayer.playMusic(response.replace("Je lance la musique", ""))


#main
if __name__ == "__main__":
    runJARVIS()