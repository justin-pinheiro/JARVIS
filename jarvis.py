import sys
import keyboard
sys.path.append("modules")

import modules.stt as stt
import modules.ia as ia
import modules.tts as tts
import modules.news as news
import modules.chess_logic as chess_logic
import modules.Language as Language
from modules.Language import Languages
import nlp 

class Jarvis:
    def __init__(self, language, GPTmodel : str, commandMode : bool) -> None:
        self.run :  bool = True
        self.chessMode : bool = False
        self.language = language
        self.GPTmodel : str = GPTmodel
        self.chessGame = chess_logic.ChessGame(chess_logic.ChessLevel.INTERMEDIATE, chess_logic.chess.BLACK)
 
    def listen(self) -> str:
        # Wait for the user to press space
        keyboard.wait('a')

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
            move = "0000"
            promotion = False
            entities = nlp.getChessMove(inp, Language.getNLPchessModel(self.language))
            for entity in entities:
                print(entity)
                if (entity[1]=="CHESS_PROMOTION"): 
                    promotion = True
            
            if(len(entities)==2 and entities[0][1]=="CHESS_COL_TO" and entities[1][1]=="CHESS_ROW_TO"):
                move = self.chessGame.getPlayerMove(promotion, "pawn", "", "", entities[0][0], entities[1][0])
            if(len(entities)==3 and entities[0][1]=="CHESS_PIECE" and entities[1][1]=="CHESS_COL_TO" and entities[2][1]=="CHESS_ROW_TO"):
                move = self.chessGame.getPlayerMove(promotion, entities[0][0], "", "", entities[1][0], entities[2][0])
            if(len(entities)==5 and entities[0][1]=="CHESS_PIECE" and entities[1][1]=="CHESS_COL_FROM" and entities[2][1]=="CHESS_ROW_FROM" and entities[3][1]=="CHESS_COL_TO" and entities[3][1]=="CHESS_ROW_TO"):
                move = self.chessGame.getPlayerMove(promotion, entities[0][0], entities[1][0], entities[2][0], entities[3][0], entities[4][0])
            

            print("move " + move)
            return move
                
        else:
            for entity in nlp.getEntitiesFromSentence(inp, Language.getNLPmodel(self.language)):
                print(entity) 
                if entity[1] == "GREETING":
                    self.say(Language.greetings(jarvis.language))
                if entity[1] == "ACKNOWLEDGMENT":
                    self.say(Language.acknowledgment(jarvis.language))
                if entity[1] == "WELLBEING":
                    self.say(Language.wellbeing(jarvis.language))
                if entity[1] == "PURPOSE":
                    self.say(Language.purpose(jarvis.language))
                if entity[1] == "NEWS":
                    self.say(Language.news(jarvis.language))
                    for sentence in news.getHeadlines(Language.getNewsAPICode(self.language)):
                        self.say(sentence)
                if entity[1] == "CHESS":
                    self.say("Sure, let's play chess. I will play as white.")
                    self.chessMode = True
            return ""


if __name__ == "__main__":

    jarvis = Jarvis(Languages.ENGLISH, ia.Models.BABBAGE, False)

    jarvis.say(Language.greetings(jarvis.language))

    while(jarvis.run):
        if(jarvis.chessMode):
            jarvis.chessGame = chess_logic.ChessGame(chess_logic.ChessLevel.NOOB, chess_logic.chess.BLACK)
            while (not jarvis.chessGame.isOver()):
                if (jarvis.chessGame.isPlayerTurn()):
                    move = "0000"
                    while (not jarvis.chessGame.isMoveLegal(move)):
                        move = jarvis.process(jarvis.listen())
                else:
                    move = jarvis.chessGame.getAImove()
                    jarvis.say("i play " + jarvis.chessGame.getMoveInNaturalLanguage(move))
                jarvis.chessGame.makeMove(move)
        else:
            jarvis.process(jarvis.listen())
