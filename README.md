# Conway-Game-Of-Life

Simple implementation of Conway's Game of Life made with Python(numpy)
## Rules 
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square _cells_, each of which is in one of two possible states, _live_ or _dead_.Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbors dies, as if by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The initial pattern constitutes the _seed_ of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a _tick_

## How its implemented (at the moment)
The seed is hard coded and the representation of each generation occurs in the terminal.
