from gui import DisplayMatrix
import argparse


def main():
    parser = argparse.ArgumentParser(
        "prog=Sudoku FEN",
        description="Turns sudoku fen notation into a sudoku board image",
    )
    parser.add_argument("--fen", required=True)
    args = parser.parse_args()
    d = DisplayMatrix(args.fen)
    d.draw_matrix()


if __name__ == "__main__":
    raise SystemExit(main())
