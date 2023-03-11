import chess
import keyboard
from stockfish import Stockfish
import random
from enum import Enum

class ChessLevel (Enum):
    # A complete beginner who is just starting to learn the rules of chess. 
    # They may not understand basic tactics or strategies and may make frequent blunders.
    NOOB = "NOOB"

    # A player who understands the basic rules of chess and can play a game without making many rules violations, 
    # but still has a limited understanding of tactics and strategy.
    BEGINNER = "BEGINNER"

    # A player who has a solid grasp of the rules, basic tactics, and some strategies. 
    # They can play decent games and may have some experience in tournament play.
    INTERMEDIATE = "INTERMEDIATE"

    # A player who has a good understanding of tactics, strategies, and opening principles. 
    # They are able to calculate variations and make plans, but may lack experience or consistency at a higher level.
    ADVANCED = "ADVANCED"

    # A player who has significant experience in tournament play and has achieved a high rating. 
    # They have a deep understanding of tactics, strategy, and opening theory, and are able to analyze complex positions.
    EXPERT = "EXPERT"

    # A player who has achieved a high rating and has significant experience in tournament play at a professional level. 
    # They have a deep understanding of chess strategy, opening theory, and endgame techniques.
    MASTER = "MASTER"

    # The highest level of achievement in chess. 
    # A grandmaster has reached the pinnacle of the game, with a deep understanding of chess strategy 
    # and the ability to analyze complex positions at a world-class level. 
    # They have achieved the highest rating in chess and have significant experience in top-level tournament play.
    GRANDMASTER = "GRANDMASTER"


class ChessAI:

    def getSkillLevelFromChessLevel(self, level : ChessLevel) -> int:
        match level:
            case ChessLevel.NOOB: return 1
            case ChessLevel.BEGINNER: return 2
            case ChessLevel.INTERMEDIATE: return 1
            case ChessLevel.ADVANCED: return 3
            case ChessLevel.EXPERT: return 5
            case ChessLevel.MASTER: return 7
            case ChessLevel.GRANDMASTER: return 9
        return 0
        
    def getMoveDepthFromChessLevel(self, level : ChessLevel) -> int:
        match level:
            case ChessLevel.NOOB: return 3
            case ChessLevel.BEGINNER: return 3
            case ChessLevel.INTERMEDIATE: return 1
            case ChessLevel.ADVANCED: return 1
            case ChessLevel.EXPERT: return 1
            case ChessLevel.MASTER: return 1
            case ChessLevel.GRANDMASTER: return 1
        return 1
        
    def __init__(self, level : ChessLevel) -> None:
        self.stockfish = Stockfish(path="./stockfish/stockfish-windows-2022-x86-64-avx2.exe", depth=10)
        self.stockfish.set_skill_level(self.getSkillLevelFromChessLevel(level))
        self.move_depth = self.getMoveDepthFromChessLevel(level)

    def getAIMoveFromPosition(self, fen_positon : str):
        move = "error"
        if (self.stockfish.is_fen_valid(fen_positon)):
            self.stockfish.set_fen_position(fen_positon)
            move = self.stockfish.get_top_moves(random.randint(1, self.move_depth))[-1]['Move']
        return move


    
class ChessGame:

    def __init__(self, AIelo : ChessLevel, playerColor : chess.Color) -> None:
        self.AI = ChessAI(AIelo)
        self.playerColor = playerColor
        self.board = chess.Board(chess.STARTING_BOARD_FEN)

    def setBoardWithFEN(self, fen : str) -> None:
        self.board = chess.Board(fen)

    def pieceExists(self, piece_type : str, piece : Stockfish.Piece, color : str) :
        match (piece_type):
            case "pawn": 
                return piece == Stockfish.Piece.WHITE_PAWN and color == "white" or piece == Stockfish.Piece.BLACK_PAWN and color == "black" 
            case "knight": 
                return piece == Stockfish.Piece.WHITE_KNIGHT and color == "white" or piece == Stockfish.Piece.BLACK_KNIGHT and color == "black" 
            case "bishop": 
                return piece == Stockfish.Piece.WHITE_BISHOP and color == "white" or piece == Stockfish.Piece.BLACK_BISHOP and color == "black" 
            case "rook": 
                return piece == Stockfish.Piece.WHITE_ROOK and color == "white" or piece == Stockfish.Piece.BLACK_ROOK and color == "black" 
            case "queen": 
                return piece == Stockfish.Piece.WHITE_QUEEN and color == "white" or piece == Stockfish.Piece.BLACK_QUEEN and color == "black" 
            case "king": 
                return piece == Stockfish.Piece.WHITE_KING and color == "white" or piece == Stockfish.Piece.BLACK_KING and color == "black" 
        return False

    def isPlayerTurn(self) -> bool:
        return self.board.turn == self.playerColor

    def isPlayerWhite(self) -> bool:
        return self.playerColor == chess.WHITE

    def isMoveLegal(self, uci_move : str):
        if uci_move[:2] == uci_move[-2:] or len(uci_move)>5:
            return False
        return chess.Move.from_uci(uci_move) in self.board.legal_moves

    def isEnPassant(self, uci_move : str):
        return self.board.is_en_passant(chess.Move.from_uci(uci_move))

    def isOver(self):
        return self.isCheckmate() or self.isStalemate()

    def isCheckmate(self):
        return self.board.is_checkmate()

    def isStalemate(self):
        return self.board.is_stalemate()

    def getPieceName(self, uci_square : str) -> str:
        return chess.piece_name(self.board.piece_type_at(chess.parse_square(uci_square)))

    def isTherePromotion(self, uci_move : str) -> bool:
        return chess.Move.from_uci(uci_move).promotion != None

    def getPieceNameAfterPromotion(self, uci_move : str):
        if self.isTherePromotion(uci_move) :
            name = "error"
            self.board.push(chess.Move.from_uci(uci_move))
            name = self.getPieceName(uci_move[-3:-1])
            self.board.pop()
            return name

    def isCheck(self):
        return self.board.is_check()

    def isMoveCheck(self, uci_move : str) -> bool:
        is_check = False
        self.board.push(chess.Move.from_uci(uci_move))
        is_check = self.isCheck()
        self.board.pop()
        return is_check

    def isMoveCheckmate(self, uci_move : str) -> bool:
        is_checkmate = False
        self.board.push(chess.Move.from_uci(uci_move))
        is_checkmate = self.isCheckmate()
        self.board.pop()
        return is_checkmate

    def isMoveStalemate(self, uci_move : str) -> bool:
        is_stalemate = False
        self.board.push(chess.Move.from_uci(uci_move))
        is_stalemate = self.isStalemate()
        self.board.pop()
        return is_stalemate

    def isCapture(self, uci_move : str) -> bool:
        return self.board.is_capture(chess.Move.from_uci(uci_move))

    def makeMove(self, uci_move : str):
        self.board.push(chess.Move.from_uci(uci_move))

    def getAImove(self) -> str:
        return self.AI.getAIMoveFromPosition(self.board.fen())

    def getMoveInNaturalLanguage(self, uci_move : str) -> str:
        if (self.isMoveLegal(uci_move)):
            square_from = uci_move[:2]
            natural_move = self.getPieceName(square_from) + " "
            
            if len(self.getLegalMovesCorrespondingToMove(self.getPieceName(square_from), uci_move)) > 1:
                natural_move += square_from + " "

            if (self.isCapture(uci_move)):
                natural_move += "takes" + " "
                if(not self.isEnPassant(uci_move)):
                    if(self.isTherePromotion(uci_move)):
                        natural_move += self.getPieceName(uci_move[-3:-1]) + " "
                    else:
                        natural_move += self.getPieceName(uci_move[-2:]) + " "
                else:
                    natural_move += "pawn" + " "
            
            if(self.isTherePromotion(uci_move)):
                natural_move += uci_move[-3:-1] + " " + "promotes to" + " " + self.getPieceNameAfterPromotion(uci_move) + " "
            else:
                natural_move += uci_move[-2:] + " "

            if self.isEnPassant(uci_move):
                natural_move += "en passant" + " "

            if (self.isMoveCheck(uci_move)):
                natural_move += "check"

            if (self.isMoveCheckmate(uci_move)):
                natural_move += "mate"

            if (self.isMoveStalemate(uci_move)):
                natural_move += "stalemate"

            return natural_move
        return "error"


    def getPlayerMove(self, promotion : bool, piece : str, col_from, row_from, col_to, row_to):
        aliases = {
            "a": ["alpha"],
            "b": ["bravo", "level", "travel", "brother"],
            "c": ["charlie", "charlie's", "charlotte", "shirley", "charly"],
            "d": ["delta", "deltas", "dentist", "data"],
            "e": ["echo", "eco", "eagle", "pico", "seiko"],
            "f": ["foxtrot", "fox", "box", "oxford"],
            "g": ["golf" , "girl", "god"],
            "h": ["hotel", "hotels"],
            "1": ["one"],
            "2": ["two"],
            "3": ["three", "tree"],
            "4": ["four", "for", "ford"],
            "5": ["five", "flight", "site", "fire", "size", "south"],
            "6": ["six", "sex"],
            "7": ["seven"],
            "8": ["eight"],
            "pawn": ["phone", "pawns", "phones"],
            "knight": ["add", "nike", "nice","night", "nights", "light", "lights", "knights", "white"],
            "bishop": ["chip", "bishops", "bishop's", "show"],
            "rook": ["took", "book", "room"],
            "queen": ["queens"],
            "king": ["kings", "kink"],
        }

        for key, values in aliases.items():
            if piece.lower() in values: piece = key
            if col_from.lower() in values: col_from = key
            if row_from.lower() in values: row_from = key
            if col_to.lower() in values: col_to = key
            if row_to.lower() in values: row_to = key

        if (row_from != "" and col_from != ""):
            if (promotion):
                return col_from + row_from + col_to + row_to + piece[:1]
            else:
                return col_from + row_from + col_to + row_to
        else:
            return self.getLegalMoveCorrespondingToDestinationSquare(piece, col_to+row_to, promotion)


    def getLegalMoveCorrespondingToDestinationSquare(self, piece : str, destination_square : str, promotion : bool):
        chess_tiles = [f"{col}{row}" for col in "abcdefgh" for row in range(1, 9)]
        
        print("searching move " + piece + " to " + destination_square + "[promoting? " + str(promotion) + "]")

        for chess_tile in chess_tiles:
            if (self.board.piece_at(chess.parse_square(chess_tile)) != None):
                if (promotion):
                    if (self.getPieceName(chess_tile) == "pawn" and self.isMoveLegal(chess_tile + destination_square)):
                        return chess_tile+destination_square+piece[:1]
                else:
                    if (self.getPieceName(chess_tile) == piece and self.isMoveLegal(chess_tile + destination_square)):
                        return chess_tile+destination_square
        return "0000"   


    def getLegalMovesCorrespondingToMove(self, piece : str, uci_move : str):
        chess_tiles = [f"{col}{row}" for col in "abcdefgh" for row in range(1, 9)]
        moves = []
        
        for chess_tile in chess_tiles:
            if (self.board.piece_at(chess.parse_square(chess_tile)) != None):
                if (self.isTherePromotion(uci_move)):
                    if (self.getPieceName(chess_tile) == piece and self.isMoveLegal(chess_tile + uci_move[-3:])):
                        moves.append(chess_tile + uci_move[-3:])
                else:
                    if (self.getPieceName(chess_tile) == piece and self.isMoveLegal(chess_tile + uci_move[-2:])):
                        moves.append(chess_tile + uci_move[-2:])
        
        return moves

# game = ChessGame(ChessLevel.INTERMEDIATE, chess.WHITE)
# print(game.board)

# while not game.isOver():
#     keyboard.wait('a')
#     move : str = game.getAImove()
#     print(move)
#     print(str(game.board.fullmove_number) + " : " + game.getMoveInNaturalLanguage(str(move)))
#     game.makeMove(move)