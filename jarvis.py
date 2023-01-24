""" LIBRARIES """

#project libraries
import libraries.stt as stt
import libraries.ia as ia
import libraries.tts as tts


""" PROGRAM """

def startJARVIS() -> None:
    initSpeech = "Initialisation du système... Système opérationnel... Bonjour, Monsieur."
    tts.createAudioSpeechFromText(initSpeech, 'fr-fr', 'Axel', 'speech.mp3')
    print("\nJARVIS : " + initSpeech)
    tts.playAudioFile('speech.mp3')
    tts.removeAudioFile('speech.mp3')

#JARVIS Program
def runJARVIS() -> None:
    
    startJARVIS()
    
    run = True
    
    while(run):

        #speech to text
        question = ""
        while (question == ""):
            question = stt.getTextFromMicrophoneRecord()
        print("\nMOI : " + question)

        #text recognition and response
        response = ia.getResponseFromGPT3ViaPrompt("text-babbage-001", question)
        print("\nJARVIS : " + response)

        #text to speech
        tts.createAudioSpeechFromText(response, 'fr-fr', 'Axel', 'speech.mp3')
        tts.playAudioFile('speech.mp3')
        tts.removeAudioFile('speech.mp3')

#main
if __name__ == "__main__":
    runJARVIS()
    