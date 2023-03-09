import sys
sys.path.append("modules")

import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.news as news
import modules.chess as chess
import modules.Language as Language
from modules.Language import Languages
import nlp 

class Jarvis:
    def __init__(self, language, GPTmodel : str, commandMode : bool) -> None:
        self.run :  bool = True
        self.chessMode : bool = False
        self.language = language
        self.GPTmodel : str = GPTmodel
        self.chess = chess.Chess(1,False)
 
    def listen(self) -> str:
        inp = ""
        while (inp == ""):
            inp = stt.getTextFromMicrophoneRecord(Language.getSTTCode(self.language))
        print("\nUSER : " + inp)
        return inp

    def say(self, text:str) -> None:
        print("\nJARVIS : " + text)
        tts.play(text, Language.getTTScode(self.language), Language.getVoice(self.language))

    def process(self, inp):
        inp = inp.lower()
        if self.chessMode:
            move = "a"
            for entity in nlp.getChessMove(inp):
                print(entity)
                move = self.chess.getPlayerMove(entity[1], entity[0])
                print(move)
            return move
                
        else:
            for entity in nlp.getEntitiesFromSentence(inp):
                print(entity)
                if entity[1] == "GREETING":
                    self.say(Language.greetings(jarvis.language))
                if entity[1] == "NEWS":
                    self.say(news.getHeadlines())
                if entity[1] == "CHESS":
                    self.say("Sure, let's play chess. I will play as white.")
                    self.chessMode = True
                    self.chess = chess.Chess(1,False)
            return ""


if __name__ == "__main__":

    jarvis = Jarvis(Languages.ENGLISH, ia.Models.BABBAGE, False)

    jarvis.say(Language.greetings(jarvis.language))

    while(jarvis.run):
        if(jarvis.chessMode):
            while (not jarvis.chess.isCheckmate()):
                #white to move
                if (jarvis.chess.player_is_white):
                    move = "a"
                    while (not jarvis.chess.isMoveLegal(move)):
                        move = jarvis.process(jarvis.listen())
                else:
                    move = jarvis.chess.getAIMove()
                    jarvis.say("i play " + move)
                jarvis.chess.playMove(move)
                #black to move
                if (not jarvis.chess.player_is_white):
                    move = "a"
                    while (not jarvis.chess.isMoveLegal(move)):
                        move = jarvis.process(jarvis.listen())
                else:
                    move = jarvis.chess.getAIMove()
                    jarvis.say("i play " + move)
                jarvis.chess.playMove(move)
        else:
            jarvis.process(jarvis.listen())
