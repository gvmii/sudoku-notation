"""
Parses the sudoku_fen string in order to display the appropriate board
"""
import numpy


class SudokuBoard:
    def __init__(self, sudoku_fen: str):
        self.sudoku_fen = ""
        self.valid_modifiers = ""
        if sudoku_fen == "":
            raise ValueError

    def get_matrix(self, sudoku_fen: str) -> numpy.ndarray:
        fen_list = sudoku_fen.split("/")
        dimensions = fen_list.pop(0).replace("0", "")
        tuple_dimensions = (int(dimensions[0]), int(dimensions[1]))
        print(f"DIMENSIONS OF THE GRID: {tuple_dimensions}")
        matrix = numpy.reshape(fen_list, tuple_dimensions)
        return matrix
