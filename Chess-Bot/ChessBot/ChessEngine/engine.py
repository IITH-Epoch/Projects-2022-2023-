from stockfish import Stockfish

class board():
    def __init__(self, display = True):
        self.Board = Stockfish()
        if (display):
            self.Board.get_board_visual()

    def move_piece(self, move, display = True):
        """
        Moves chess piece(s)

        Args:
            move: string
            Eg. move = "e2e4"
            => Move piece at e2 to e4
        """
        self.Board.make_moves_from_current_position([move])
        if (display):
            print(self.Board.get_board_visual())

    def get_best(self):
        best_move = self.Board.get_best_move()
        # self.Board.make_moves_from_current_position([best_move])
        return best_move