import sys
import pygame

from simulation import Simulation

pygame.init()

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
FPS = 12
CELL_SIZE = 10

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

mouse_drag = False
toggled_cells = set()

# For KEYDOWN

def increase_fps():
    global FPS
    FPS += 1

def decrease_fps():
    global FPS
    if FPS > 5:
        FPS -= 1

def create_random_state():
    if not simulation.is_running():
        simulation.create_random_state()
        toggled_cells.clear()

def clear_grid():
    if not simulation.is_running():
        simulation.clear()
        toggled_cells.clear()

key_actions = {
    pygame.K_SPACE: lambda: simulation.stop() if simulation.is_running() else simulation.start(),
    pygame.K_UP: lambda: increase_fps(),
    pygame.K_DOWN: lambda: decrease_fps(),
    pygame.K_r: lambda: create_random_state(),
    pygame.K_c: lambda: clear_grid(),
}

# Simulation Loop
while True:

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_drag = True
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            col = pos[0] // CELL_SIZE

            simulation.toggle_cell(row, col)

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_drag = False
            toggled_cells.clear()

        if event.type == pygame.MOUSEMOTION and mouse_drag:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            col = pos[0] // CELL_SIZE
            if (row, col) not in toggled_cells:
                simulation.toggle_cell(row, col)
                toggled_cells.add((row, col))

        if event.type == pygame.KEYDOWN:

            action = key_actions.get(event.key)
            if action:
                action()

    # Updating State
    simulation.update_state()

    # Displaying Graphics
    window.fill((100, 100, 100))
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)