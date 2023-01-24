""" LIBRARIES """

#project libraries

import stt
import ia
import tts
import MusicPlayer


""" PROGRAM """

def startJARVIS() -> None:

    initSpeech = "Initialisation du système... Système opérationnel... Bonjour, Monsieur."
    tts.createAudioSpeechFromText(initSpeech, 'fr-fr', 'Axel', 'speech.mp3')

    print("\nJARVIS : " + initSpeech)

    tts.playAudioFile('speech.mp3')
    tts.removeAudioFile('speech.mp3')

#JARVIS Program
def runJARVIS() -> None:

    print("Jarvis enabled")

    startJARVIS()
    
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

        """ (A faire)
        #Lecteur de commandes
        if(response[0]=='/'):
            print(response[0:10])
            if(response[0:10] == "/playMusic/"):
                MusicPlayer.playMusic(response.split("/")[1])
        """

        #text to speech
        tts.createAudioSpeechFromText(response, 'fr-fr', 'Axel', 'speech.mp3')
        tts.playAudioFile('speech.mp3')
        tts.removeAudioFile('speech.mp3')


#main
if __name__ == "__main__":
    runJARVIS()