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

    def get_metadata(self, sudoku_fen: str) -> list:
        fen_list = sudoku_fen.split("/")
        puzzle_name = fen_list.pop(0)
        author_name = fen_list.pop(0)
        puzzle_size = fen_list.pop(0).replace("0", "")
        metadata = [
            puzzle_name,
            author_name,
            (int(puzzle_size[0]), int(puzzle_size[1])),
        ]
        return metadata

    def get_matrix(self, sudoku_fen: str) -> numpy.ndarray:
        metadata = self.get_metadata(sudoku_fen)
        fen_list = sudoku_fen.split("/")[3:]
        print(f"DIMENSIONS OF THE GRID: {metadata[2]}")
        matrix = numpy.reshape(fen_list, metadata[2])
        return matrix
