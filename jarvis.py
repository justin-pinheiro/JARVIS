""" LIBRARIES """

#pyhton libraries
import os

#project libraries
import stt
import ia
import tts


""" PROGRAM """

#JARVIS Program
def runJARVIS() -> None:
    run = True
    
    while(run):

        #speech to text
        question = ""
        while (question == ""):
            question = stt.getTextFromMicrophoneRecord()
        print("\nMOI : " + question)

        #text recognition and response
        response = ia.getResponseFromGPT3ViaPrompt("text-davinci-003", question)
        print("\nJARVIS : " + response)

        #text to speech
        tts.createAudioSpeechFromText(response, 'fr-fr', 'Axel', 'speech.mp3')
        tts.playAudioFile('speech.mp3')
        tts.removeAudioFile('speech.mp3')

#main
if __name__ == "__main__":
    runJARVIS()
    