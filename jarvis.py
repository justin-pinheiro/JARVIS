import sys
sys.path.append("modules")

import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.commands as commands
import modules.Language as Language
from modules.Language import Languages

 
class Jarvis:
    def __init__(self, language, GPTmodel : str, commandMode : bool) -> None:
        self.run :  bool = True
        self.command_mode : bool = commandMode
        self.language = language
        self.GPTmodel : str = GPTmodel
 
    def listen(self) -> str:
        input : str = ""
        while (input == ""):
            input = stt.getTextFromMicrophoneRecord(Language.getSTTCode(self.language))
        print("\nUSER : " + input)
        return input

    def say(self, text:str) -> None:
        print("\nJARVIS : " + text)
        tts.play(text, Language.getTTScode(self.language), Language.getVoice(self.language))

    def process(self, input):
        commandLauncher = commands.CommandLauncher(input.split()[0], input.partition(' ')[2])
        if (commandLauncher.recognizeCommand()):
            self.say(commandLauncher.activate())
        else:
            if (self.command_mode):
                self.say(Language.unknownCommand(self.language))
            else:
                self.say (ia.getResponseFromGPT3ViaPrompt(self.GPTmodel, input, Language.getPrompt(self.language)))



if __name__ == "__main__":

    jarvis = Jarvis(Languages.FRENCH, ia.Models.BABBAGE, False)

    jarvis.say(Language.greetings(jarvis.language))

    while(jarvis.run):
        jarvis.process(jarvis.listen())
