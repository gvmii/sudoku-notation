from PIL import Image, ImageDraw, ImageFont
import SudokuBoard

class DisplayMatrix:
    def __init__(self, matrix):
        # TODO: Fix this mess lol
        self.sudoku_board = SudokuBoard('0909/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0')
        self.HEIGHT, self.WIDTH = 1080, 1080
        self.num_of_rows = num_of_rows 
        self.num_of_cols = num_of_cols 

    def draw_matrix(self):
        # calculate the optimal cell size based on the image dimensions and the number of rows/columns
        if self.num_of_rows > self.num_of_cols:
            cell_size = self.HEIGHT // num_of_rows
            width = cell_size * self.num_of_cols
        else:
            cell_size = self.WIDTH // self.num_of_cols  # fixed
            width = cell_size * self.num_of_cols  # added


        # create a blank image
        image = Image.new("RGB", (self.WIDTH, self.HEIGHT), color="white")

        # get the font to use for the numbers
        font = ImageFont.truetype("Arial.ttf", cell_size // 2)

        # create an ImageDraw object
        draw = ImageDraw.Draw(image)

        # draw the grid lines
        line_thickness = max(1, cell_size // 20) # adjust line thickness based on cell size
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
                    x = col * cell_size + cell_size // 4
                    y = row * cell_size
                    draw.text((x, y), str(num), font=font, fill=(0, 0, 0))
        image.show()

x = DisplayMatrix([[1 for i in range(9)] for j in range(9)])
x.draw_matrix()
