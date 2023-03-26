"""
Parses the sudoku_fen string in order to display the appropriate board
"""
import re
import numpy


class SudokuBoard:
    def __init__(self, sudoku_fen):
        # self.board = self.load_board(sudoku_fen)

        VALID_MODIFIERS = ["K", "C", "G", "S", "L"]

    # def load_board(self, sudoku_fen):
    #     # Takes out leading numbers from fen (e.g. 0909)
    #     if len(sudoku_fen < 4) or sudoku_fen[:4] == "0000":
    #         raise ValueError("Input string is too short")
    #         num_of_rows, num_of_cols = [
    #             int(sudoku_fen[:2].lstrip("0")),
    #             int(sudoku_fen[2:4].lstrip("0")),
    #         ]

    def get_matrix(self, sudoku_fen):
        fen_list = sudoku_fen.split("/")
        dimensions = fen_list.pop(0).replace("0", "")
        tuple_dimensions = (int(dimensions[0]), int(dimensions[1]))
        print(f"DIMENSIONS OF THE GRID: {tuple_dimensions}")
        matrix = numpy.reshape(fen_list, tuple_dimensions)
        return matrix

        # # Regex pattern for modifiers
        # pattern = rf"([{self.VALID_MODIFIERS}]\([wbrd]?\d+\))"

        # matches = re.findall(pattern, sudoku_fen)

        # # Ensure that tokens start only with KCGSL
        # for match in matches:
        #     if not match.startswith(self.VALID_MODIFIERS):
        #         raise ValueError(f"Invalid token: {match}")

        # # Replace pattern with 'P' (Placeholder)
        # sudoku_fen = re.sub(pattern, "P", sudoku_fen)
        # parsed_sudoku_fen = []
        # match_counter = 0
        # for i in sudoku_fen[4:]:
        #     if i.isdigit():
        #         parsed_sudoku_fen.append(i)
        #     elif i == "P":
        #         parsed_sudoku_fen.append(matches[match_counter])
        #         match_counter += 1
        #     else:
        #         raise ValueError(f"Invalid character: {i}")
        # if len(parsed_sudoku_fen) != (num_of_rows * num_of_cols):
        #     raise ValueError("Length of string must equal dimensions")

        # board = [
        #     parsed_sudoku_fen[i : i + num_of_cols]
        #     for i in range(0, num_of_rows * num_of_cols, num_of_cols)
        # ]

        # return board


if __name__ == "__main__":
    fen = """0909/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0"""
    board = SudokuBoard(fen)
    print(board.get_matrix(fen))
