from stockfish import Stockfish


class Chess:

    def __init__(self, skill : int, isPlayerWhite : bool) -> None:
        self.stockfish = Stockfish(path="./stockfish/stockfish-windows-2022-x86-64-avx2.exe", depth=10, parameters={"Threads": 1, "Minimum Thinking Time": 10})
        self.stockfish.set_skill_level(skill)
        self.stockfish.set_position([""])
        self.player_is_white = isPlayerWhite

    def pieceCorrespondToMoveTypeAndColor(self, move_type : str, piece : Stockfish.Piece, color) :
        match (move_type):
            case "PAWN_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_PAWN and color == "white" or piece == Stockfish.Piece.BLACK_PAWN and color == "black" 
            case "PAWN_CAPTURE": 
                return piece == Stockfish.Piece.WHITE_PAWN and color == "white" or piece == Stockfish.Piece.BLACK_PAWN and color == "black" 
            case "KNIGHT_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_KNIGHT and color == "white" or piece == Stockfish.Piece.BLACK_KNIGHT and color == "black" 
            case "BISHOP_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_BISHOP and color == "white" or piece == Stockfish.Piece.BLACK_BISHOP and color == "black" 
            case "ROOK_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_ROOK and color == "white" or piece == Stockfish.Piece.BLACK_ROOK and color == "black" 
            case "QUEEN_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_QUEEN and color == "white" or piece == Stockfish.Piece.BLACK_QUEEN and color == "black" 
            case "KING_MOVEMENT": 
                return piece == Stockfish.Piece.WHITE_KING and color == "white" or piece == Stockfish.Piece.BLACK_KING and color == "black" 
        return False

    def isCheckmate(self):
        return "mate" in self.stockfish.get_evaluation()["type"]

    def getPlayerMove(self, move_type : str, tile : str):
        chess_tiles = [f"{col}{row}" for col in "abcdefgh" for row in range(1, 9)]
        color = "black"
        if (self.player_is_white):
            color = "white"
        for chess_tile in chess_tiles:
            if (self.pieceCorrespondToMoveTypeAndColor(move_type, self.stockfish.get_what_is_on_square(chess_tile), color) and self.stockfish.is_move_correct(chess_tile+tile)):
                return chess_tile+tile

    def getAIMove(self):
        top_moves = self.stockfish.get_top_moves(3)
        if top_moves[2]:
            return top_moves[2]['Move']
        elif top_moves[1]:
            return top_moves[1]['Move']
        else:
            return top_moves[0]['Move']

    def isMoveLegal(self, move : str):
        return self.stockfish.is_move_correct(move)

    def playMove(self, move : str):
        self.stockfish.make_moves_from_current_position([move])
        self.stockfish.get_board_visual(self.player_is_white)
