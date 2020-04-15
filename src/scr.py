import pygame
from copy import deepcopy
from options import colors, framerate, cellSize
from grid import Grid
from lifecell import Cell


def life_screen(display):
    resolution = display.get_size()

    clock = pygame.time.Clock()


    # objects
    grid = Grid([0, 0], [resolution[1], resolution[0]], cellSize,
                colors['emptyCell'], colors['emptyCellBorder'])
    for row in grid:
        for cell in row:
            Cell(grid, cell.gridPosition, cellSize,
                 colors['cell'], colors['cellBorder'], alive=False)
    gridBackup = deepcopy(grid)

    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    pausedText = font.render('space to unpause', True, colors['pausedText'])
    liveText = font.render('space to pause', True, colors['liveText'])

    # main loop
    run = True
    live = False
    while run:
        # event loop
        skip_turn = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # keyboard events
            if event.type == pygame.KEYDOWN:
                # pause/unpause
                if(event.key == pygame.K_RETURN or
                   event.key == pygame.K_SPACE):
                    live = not(live)

                # reset grid
                if(event.key == pygame.K_r or
                   event.key == pygame.K_ESCAPE):
                    grid = deepcopy(gridBackup)

                # move forward a step
                if event.key == pygame.K_RIGHT and not(live):
                    skip_turn = True
                    live = True

        # repeated events
        # mouse
        mousePos = pygame.mouse.get_pos()
        mouseButtonsClicked = pygame.mouse.get_pressed()
        if not(live):
            for row in grid:
                for cell in row:
                    if is_mouse_on_cell(cell, mousePos):
                        # fill cell
                        if mouseButtonsClicked[0]:
                            cell.resurrect()
                        # clear cell
                        elif mouseButtonsClicked[2]:
                            cell.die()
        # keyboard
        keysPressed = pygame.key.get_pressed()

        # move forward a step repeatedly
        if keysPressed[pygame.K_RIGHT]:
            skip_turn = True
            live = True


        # do stuff
        if live:
            shownText = liveText

            live = play_life(grid)
            if skip_turn:
                live = False
        else:
            shownText = pausedText

        # draw stuff
        grid.draw_grid(display)
        display.blit(shownText, [0, 0])
        pygame.display.update()


        clock.tick(framerate)


def play_life(grid: Grid) -> bool:
    """
    Plays a single turn of the Game of Life and
    returns whether the grid is empty or not.
    """
    oldGrid = deepcopy(grid)

    live = False
    for row in grid:
        for cell in row:
            cell.live(oldGrid)
            if cell.alive:
                live = True

    return live


def is_mouse_on_cell(cell: Cell, mousePos: list) -> bool:
    if((mousePos[0] > cell.position[0] and mousePos[0] <= cell.position[0] + cell.size[0]) and
       (mousePos[1] > cell.position[1] and mousePos[1] <= cell.position[1] + cell.size[1])):
        return True
    else:
        return False
