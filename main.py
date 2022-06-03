import pygame

WIN_WIDTH = 500
WIN_HEIGHT = 500



def draw_window(win):
    pygame.display.update()

def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    color2 = (50,50,50)
    square, line = 0, 0
    while square < 10 or line < 10:
        print(str(square) + " - " + str(line))
        color = (55,55,55)
        if ((square % 2) == 0 and (line % 2) != 0) or ((line % 2) == 0 and (square % 2) != 0):
            color = color2

        pygame.draw.rect(win, color, pygame.Rect(square * 50, line * 50, 50, 50))
        if square >= 10:
            square = 0
            line = line + 1
        else:
            square = square + 1


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        draw_window(win)

main()