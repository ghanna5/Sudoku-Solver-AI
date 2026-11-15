## Description
A Fork of Dhruv Panchal's Sudoku Solver that uses A* algorithm to solve Sudoku instead of a backtracking algorithm. Built for CPSC 481 Artifical Intelligence course project at California State University, Fullerton.

## Features:
- Generates a random, solvable Sudoku board
- Easy-to-use GUI for inputting and solving puzzles
- Visualizer feature shows progress of algorithm
- Can shows hints with 'h' and restart board with 'r'

## How to Use:
1. Download the repository and run the SudokuGUI.py file.
2. Use the left-click to select the box you want to fill, then enter your value and confirm it by pressing the Enter key.
3. Get hints with 'h' and restart the board with 'r'.
4. Solve the puzzle with the space bar.

## Input:

| Keys              | Actions                                                         |
|-------------------|-----------------------------------------------------------------|
| `Left Click`      | Selects the Box to enter a value into that cell.                |
| `Enter`           | Confirms the Value written on the board.     |
| `Backspace/Delete`| Deletes the value in that cell.                                 |
| `Space`           | Solves the Board using the Algorithm.                           |
| `H`               | Gives a Hint. Displays a random correct value on the board.     |
| `R`               | Restarts the current Board and timer                            |
| `Escape`          | Quit the program.                                               |

## Requirements:
To run Sudoku Solver, you'll need to have Python and PyGame installed on your system. You can install the necessary requirements using pip:
```
pip install -r requirements.txt
```

## Execution:
- Clone this repository using
```
git clone https://github.com/JulianMatu/Sudoku-Solver-AI.git
```
- Now run the [SudokuGUI](https://github.com/dhhruv/Sudoku-Solver/blob/master/SudokuGUI.py) file directly in your Terminal using
```
python SudokuGUI.py
```
**OR**
```
python3 SudokuGUI.py
```

## Conclusion:
