# Raw game file
import pygame
import random

WIN_WIDTH = 500
WIN_HEIGHT = 500


class Snake:
    def __init__(self):
        self.x = 250
        self.y = 250


def draw_window(win, snake):
    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    fps = pygame.time.Clock()
    snake = Snake()
    snake_position = [250, 250]
    snake_body = [[250, 250],
                  [240, 250],
                  [230, 250],
                  [220, 250]
                  ]
    score = 0

    direction = 'RIGHT'
    change_to = direction
    fruit_location = [random.randrange(1, 50) * 10,
                      random.randrange(1, 50) * 10]
    fruit_spawn = True
    frame = 0

    run = True
    while run:
        frame = frame + 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_location[0] and snake_position[1] == fruit_location[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_location = [random.randrange(1, 50) * 10,
                      random.randrange(1, 50) * 10]

        fruit_spawn = True
        win.fill((0, 0, 0))
        for pos in snake_body:
            pygame.draw.rect(win, (0,255,0),
                             pygame.Rect(pos[0], pos[1], 10, 10))

        if fruit_spawn:
            pygame.draw.rect(win, (255, 0, 0),
                             pygame.Rect(fruit_location[0], fruit_location[1], 10, 10))

        draw_window(win, snake)
        fps.tick(10)


main()