import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.commands as commands


class Jarvis:

    run : bool = True
    command_mode : bool = False
    response : str = ""

    def startJARVIS(self) -> None:
        print("\nJARVIS : Bonjour, Monsieur.")
 

    def launch(self) -> None:

        jarvis.startJARVIS()

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
                self.response = commandLauncher.activate()
                print(self.response)
                
            else:
                if (self.command_mode):
                    self.response = "Je suis désolé, la commande demandée n'existe pas."

                else:
                    #text recognition and response
                    self.response = ia.getResponseFromGPT3ViaPrompt("text-babbage-001", question)
                    print("\nJARVIS : " + self.response)

            #text to speech
            tts.createAudioSpeechFromText(self.response, 'fr-fr', 'Axel', 'speech.mp3')
            tts.playAudioFile('speech.mp3')
            tts.removeAudioFile('speech.mp3')

#main
if __name__ == "__main__":

    jarvis = Jarvis()
    jarvis.launch()