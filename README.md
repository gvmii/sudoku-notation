# Sudoku Notation System

Sudoku Notation © 2023 is licensed under Attribution-NonCommercial-NoDerivatives 4.0 International. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/
This license will change in the future.

## Why?

This was inspired by a conversation based on Cracking The Cryptic's new book that is coming out, and how the last one had a lot of erroneous puzzles. I realized that there's not any standarized sudoku notation to share variant Sudokus reliably.

## What are the goals of the project?

I want something that is:

- Simple
- Easily expandable
- Free
- Not too many characters (You should be able to share a puzzle in the fewest characters possible)

## First revision of the idea:

A clear board looks like this:

000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000

(We can replace 0's with dots, as some people prefer.)

We plan on setting modifiers after each cell, like this:

The symbol (like k for kropki dot) can be changed later

Kropki dot: (K[w/b][r/d])
Clue (For cages and stuff): (C[NUMBER])
Cage: (G([VARIABLE NUMBER]))
Shaded Cell:(S[COLOR])
Line: (L[VARIABLE NUMBER])

We plan on adding some important metadata BEFORE the puzzle. For example:
0909[PUZZLE] would mean that the puzzle is 9x9, and tell the parser to make a new "row" when 9 tokens have been reached.

![Cage Sudoku](https://media.discordapp.net/attachments/1088231082798882836/1088243866274115604/4707-1.jpg)

We could write the first 3 rows of the following puzzle as the following:

0909 0C(25)G(1) 0G(1) 0G(1) 0 0 0C(37)G(2) 0G(2) 0 0C(39)G(3)
0 0 0G(1) 0G(1) 0 0G(2) 0 0 0G(2)
0G(4) 0 0G(1) 0G(2) 0G(2) 0G(2) 0G(3) 0G(3) 0G(3)
No whitespace: 09090C(25)G(1)0G(1)0G(1)000C(37)G(2)0G(2)00C(39)G(3)000G(1)0G(1)00G(2)000G(2)0G(4)00G(1)0G(2)0G(2)0G(2)0G(3)0G(3)0G(3)

Parser could try to find the first 4 characters (0909) to find the size of the puzzle, and then begin looking for "tokens". A token ends where a number starts, be it 0 (Like in this case with no given digits) or the digits 1-9.

Let's decipher the first few tokens.

0909 -> Size of puzzle, 9x9, indicates start of puzzle
0C(25)G(1) -> Let's break it down:
0 -> Indicates that the digit is 0, or not given.
C(25) -> Indicates that the clue of that box is 25.
G(1) -> Indicates that the box has a cage, and that the ID of the cage is 1.

Now we run into another 0, so the parser knows that there's no more modifiers for that box.

Box end indicators could be added, like a -, but that uses unnecessary bits.

![Bismuth, by bellsita](https://media.discordapp.net/attachments/1088231082798882836/1088346065884942356/image.png)

Let's do the same thing with `Bismuth by bellsita`

0909
1 0K(wr) 0 0L(1) 0 0L(1) 0 0 0S
0L(1) 0L(1) 0L(1) 0K(wr) 0K(wr) 0 0L(1) 0L(1) 0L(1)
0 0 0L(2) 0 0 0 0 0K(bd) 0
No whitespace: 090910K(wr)00L(1)00L(1)000S0L(1)0L(1)0L(1)0K(wr)0K(wr)00L(1)0L(1)0L(1)000L(2)00000K(bd)0

0909 -> Size of puzzle, 9x9, indicates start of puzzle
0K(wr) -> There's not any given digit in this cell, but there is a white (w) kropki dot, and it is linked to the tile at the right (r)
0L(1) -> Not any given digit, line with ID 1.
At the end of the notation:
0K(bd) -> No given digit, black (b) kropki dot, pointing down (d)
If we think carefully, we can notice that with just **right** and **down** we can orient all posible kropki dots in the board, even diagonal ones. The only exception is Kropki dots in the border of the grid (which shouldn't ex
