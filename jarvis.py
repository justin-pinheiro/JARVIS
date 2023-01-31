import sys
sys.path.append("modules")

import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.commands as commands
import modules.Language as Language
from modules.Language import Language


class Jarvis:
    def __init__(self, lang, GPTmodel : str, commandMode : bool) -> None:
        self.run :  bool = True
        self.command_mode : bool = commandMode
        self.language = Language(lang)
        self.GPTmodel : str = GPTmodel
 
    def listen(self) -> str:
        input : str = ""
        while (input == ""):
            input = stt.getTextFromMicrophoneRecord(self.language.sttCode)
        print("\nUSER : " + input)
        return input

    def say(self, text:str) -> None:
        print("\nJARVIS : " + text)
        tts.play(text, self.language.ttsCode, self.language.voice)

    def process(self, input):
        commandLauncher = commands.CommandLauncher(input.split()[0], input.partition(' ')[2])
        if (commandLauncher.recognizeCommand()):
            self.say(commandLauncher.activate())
        else:
            if (self.command_mode):
                self.say(self.language.unknownCommand)
            else:
                self.say (ia.getResponseFromGPT3ViaPrompt(self.GPTmodel, input, self.language.prompt))



if __name__ == "__main__":

    jarvis = Jarvis("french", ia.Models.BABBAGE, False)

    jarvis.say(jarvis.language.greetings)

    while(jarvis.run):
        jarvis.process(jarvis.listen())
