# What is Conway's Game of Life?

Conway's Game of Life is a cellular automaton devised by the mathematician John Conway. It is a simulation of life that evolves in discrete steps (or 'generations') based on simple rules.
Despite having very simple rules, Conway's Game of Life leads to some very interesting and complex emergent behavior.

# Basic Concepts

- The game is played on an infinite 2D grid of cells, each of which can be in one of two states: alive or dead.
- Each cell has eight neighbors (horizontally, vertically, and diagonally adjacent cells).
- The game proceeds in discrete time steps, and the state of each cell is updated simultaneously based on the states of its neighbors.
- It is a 0 player game and it continues until is at least one single cell left alive.
- The initial pattern constitutes the seed of the system. It can be either randomly generated or it can be set by the user.

# The Rules

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

# Interaction

The simulation window can be started by running the _main.py_ file. Initially, the grid will be empty. The user can randomly generate a seed or manually input the initial seed.

- SPACEBAR: pauses/resumes the simulation.
- C: clears the grid when the simulation is paused.
- R: fills the grid with a random seed when the simulation is paused.
- UP: increases FPS.
- DOWN: decreases FPS (min FPS = 5).
- MOUSE CLICK: toggles the state of the cell when the simulation is paused (changes dead cell to alive and vice versa). The mouse pointer can be dragged to toggle multiple cells.
