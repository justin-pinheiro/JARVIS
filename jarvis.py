import stt
import ia
import tts
import commands


class Jarvis:

    run : int = True

    def startJARVIS(self) -> None:

        print("\nJARVIS : " + "Initialisation du système... Système opérationnel. Bonjour, Monsieur.")
        tts.playAudioFile('initSpeech.mp3')


    def launch(self) -> None:

        while(self.run):
            #speech to text
            question : str
            question = ""
            while (question == ""):
                question = stt.getTextFromMicrophoneRecord()

            print("\nMOI : " + question)

            #Commands
            commandLauncher = commands.CommandLauncher(self, question.split()[0], question.partition(' ')[2])
            
            if (commandLauncher.recognizeCommand()):
                commandLauncher.activate()
                
            else:
                #text recognition and response
                response : str
                response = ia.getResponseFromGPT3ViaPrompt("text-babbage-001", question)
                print("\nJARVIS : " + response)

                #text to speech
                tts.createAudioSpeechFromText(response, 'fr-fr', 'Axel', 'speech.mp3')
                tts.playAudioFile('speech.mp3')
                tts.removeAudioFile('speech.mp3')

#main
if __name__ == "__main__":

    jarvis = Jarvis()
    jarvis.launch()