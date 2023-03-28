from PIL import Image, ImageDraw, ImageFont
from sudoku_parser import SudokuBoard
import getpass


class DisplayMatrix:
    def __init__(self, sudoku_fen: str):
        self.sudoku_board = SudokuBoard(sudoku_fen).get_matrix()
        metadata = SudokuBoard(sudoku_fen).get_metadata()
        self.HEIGHT, self.WIDTH = 1080, 1080

        self.num_of_rows = metadata[2][0]
        self.num_of_cols = metadata[2][1]

    def draw_matrix(self):
        # calculate the optimal cell size based on the image dimensions and the number of rows/columns
        if self.num_of_rows > self.num_of_cols:
            cell_size = self.HEIGHT // self.num_of_rows
            width = cell_size * self.num_of_cols
        else:
            cell_size = self.WIDTH // self.num_of_cols  # fixed
            width = cell_size * self.num_of_cols  # added

        # create a blank image
        image = Image.new("RGB", (self.WIDTH, self.HEIGHT), color="white")

        # get the font to use for the numbers
        font = ImageFont.truetype(
            f"/Users/{getpass.getuser()}/sudoku-notation/fonts/LiberationSans-Regular.ttf",
            cell_size // 2,
        )

        # create an ImageDraw object
        draw = ImageDraw.Draw(image)

        # draw the grid lines
        line_thickness = max(
            1, cell_size // 20
        )  # adjust line thickness based on cell size
        for i in range(self.num_of_rows + 1):
            # horizontal lines
            y = i * cell_size
            draw.line([(0, y), (self.WIDTH, y)], fill=(0, 0, 0), width=line_thickness)

        for j in range(self.num_of_cols + 1):
            # vertical lines
            x = j * cell_size
            draw.line([(x, 0), (x, self.HEIGHT)], fill=(0, 0, 0), width=line_thickness)

        # draw the numbers on the image
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                num = self.sudoku_board[row][col]
                if num != 0:
                    # center the number in the cell
                    x_center = col * cell_size + cell_size // 2
                    y_center = row * cell_size + cell_size // 2
                    x, y = draw.textsize(str(num), font=font)
                    draw.text(
                        (x_center - x // 2, y_center - y // 2),
                        str(num),
                        font=font,
                        fill=(0, 0, 0),
                    )
        image.show()
