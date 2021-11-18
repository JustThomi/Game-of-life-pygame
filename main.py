import pygame
import tile

pygame.init()
pygame.display.set_caption("Game of life")

WIDTH = 800
HEIGHT = 800
ROWS = 50
FPS = 10

GREY = (200, 200, 200)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def cycle(grid):
    for row in grid:
        for tile in row:
            tile.get_neighbors(grid)

    for row in grid:
        for tile in row:
            if len(tile.neighbors) < 2 and tile.is_alive():
                tile.unalive()
            elif len(tile.neighbors) > 3 and tile.is_alive():
                tile.unalive()
            elif len(tile.neighbors) == 3 and tile.is_dead():
                tile.resurrect()

    for row in grid:
        for tile in row:
            tile.reset_neighbors()


def grid_generator():
    grid = []
    gap = WIDTH // ROWS

    for i in range(WIDTH):
        grid.append([])
        for j in range(ROWS):
            cell = tile.Cell(i, j, gap, ROWS)
            grid[i].append(cell)

    return grid


def clear_board(grid):
    for row in grid:
        for tile in row:
            tile.unalive()


def get_clicked_cell(pos):
    gap = WIDTH // ROWS
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


def draw_grid_lines():
    gap = WIDTH // ROWS
    for i in range(ROWS):
        pygame.draw.line(WIN, GREY, (0, i * gap), (WIDTH, i * gap))
        for j in range(ROWS):
            pygame.draw.line(WIN, GREY, (j * gap, 0), (j * gap, WIDTH))


def draw(grid):
    for row in grid:
        for tile in row:
            tile.draw(WIN)
    draw_grid_lines()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    grid = grid_generator()

    start_cycle = False

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    start_cycle = True
                if event.key == pygame.K_s:
                    start_cycle = False
                if event.key == pygame.K_c and not start_cycle:
                    clear_board(grid)

        if pygame.mouse.get_pressed()[0] and not start_cycle:
            cursor_pos = pygame.mouse.get_pos()
            row, col = get_clicked_cell(cursor_pos)

            clicked_cell = grid[row][col]
            clicked_cell.resurrect()

        if pygame.mouse.get_pressed()[2] and not start_cycle:
            cursor_pos = pygame.mouse.get_pos()
            row, col = get_clicked_cell(cursor_pos)

            clicked_cell = grid[row][col]
            clicked_cell.unalive()

        if start_cycle:
            cycle(grid)

        draw(grid)

    pygame.quit()


if __name__ == "__main__":
    main()
