from gooey import Gooey, GooeyParser
from sudoku_parser import SudokuBoard

@Gooey(footer_bg_color="#789CA4", sidebar_bg_czolor="#789CA4", body_bg_color="#789CA4", header_bg_color="#789CA4")
def parse_args():
    parser = GooeyParser(description="Sudoku Board Parser")
    parser.add_argument("sudoku_fen", help="The FEN string for the Sudoku board")
    return parser.parse_args()

def main():
    args = parse_args()
    sudoku_fen = args.sudoku_fen
    board = SudokuBoard(sudoku_fen)
    print(board.board)

if __name__ == "__main__":
    main()
