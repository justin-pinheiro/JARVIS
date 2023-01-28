import sys
sys.path.append("modules")
import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.commands as commands


class Jarvis:

    def __init__(self) -> None:
        self.run : bool = True
        self.command_mode : bool = False
        self.response : str = ""
 
    def listen(self) -> str:
        input : str = ""
        while (input == ""):
            input = stt.getTextFromMicrophoneRecord()
        print("\nUSER : " + input)

    def say(self, text) -> None:
        print("\nJARVIS : " + text)
        tts.createAudioSpeechFromText(text, 'fr-fr', 'Axel', 'audio/speech.mp3')
        tts.playAudioFile('audio/speech.mp3')
        tts.removeAudioFile('audio/speech.mp3')


if __name__ == "__main__":

    jarvis = Jarvis()
    
    jarvis.say("Bonjour Monsieur.")

    while(jarvis.run):
        
        input = jarvis.listen()

        commandLauncher = commands.CommandLauncher(jarvis, input.split()[0], input.partition(' ')[2])
        
        if (commandLauncher.recognizeCommand()):
            jarvis.say(commandLauncher.activate())
            
        else:
            if (jarvis.command_mode):
                jarvis.say("Je suis désolé, la commande demandée n'existe pas.")

            else:
                jarvis.say (ia.getResponseFromGPT3ViaPrompt("text-babbage-001", question))

    