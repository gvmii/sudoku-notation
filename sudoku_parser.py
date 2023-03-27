"""
Parses the sudoku_fen string in order to display the appropriate board
"""
import numpy


class SudokuBoard:
    def __init__(self, sudoku_fen: str):
        self.sudoku_fen = sudoku_fen
        self.valid_modifiers = ""
        if sudoku_fen == "":
            raise ValueError

    def get_metadata(self) -> list:
        fen_list = self.sudoku_fen.split("/")
        puzzle_name = fen_list.pop(0)
        author_name = fen_list.pop(0)
        puzzle_size = fen_list.pop(0).replace("0", "")
        metadata = [
            puzzle_name,
            author_name,
            (int(puzzle_size[0]), int(puzzle_size[1])),
        ]
        return metadata

    def get_matrix(self) -> numpy.ndarray:
        metadata = self.get_metadata()
        fen_list = self.sudoku_fen.split("/")[3:]
        print(f"DIMENSIONS OF THE GRID: {metadata[2]}")
        matrix = numpy.reshape(fen_list, metadata[2])
        return matrix

# Use this code when testing the parser:
# fen = 'The path/Megumi/0909/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0'
# board = SudokuBoard(fen)
# print(board.get_metadata())
# print(board.get_matrix())
