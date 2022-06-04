import pygame
import time
import random
import os
import neat

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

# snake_speed = 15
#
# window_x = 720
# window_y = 480
#
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
#
# pygame.init()
#
# pygame.display.set_caption('GeeksforGeeks Snakes')
#
#
# def show_score(choice, color, font, size, score, win):
#     score_font = pygame.font.SysFont(font, size)
#     score_surface = score_font.render('Score : ' + str(score), True, color)
#     score_rect = score_surface.get_rect()
#     win.blit(score_surface, score_rect)
#
#
# def game_over(win, score):
#     my_font = pygame.font.SysFont('times new roman', 50)
#     game_over_surface = my_font.render(
#         'Your Score is : ' + str(score), True, red)
#
#     game_over_rect = game_over_surface.get_rect()
#     game_over_rect.midtop = (window_x / 2, window_y / 4)
#     win.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
#     time.sleep(2)
#     pygame.quit()
#     quit()
#
#
# # Main Function
# def main(genomes, config):
#     nets = []
#     ge = []
#     snakes = []
#
#     for _, g in genomes:
#         net = neat.nn.FeedForwardNetwork.create(g, config)
#         nets.append(net)
#         snakes.append(Snake())
#         g.fitness = 0
#         ge.append(g)
#
#     win = pygame.display.set_mode((window_x, window_y))
#     fps = pygame.time.Clock()
#
#     snake_position = [100, 50]
#
#     snake_body = [
#         [100, 50],
#         [90, 50],
#         [80, 50],
#         [70, 50]
#     ]
#
#     fruit_position = [random.randrange(1, (window_x // 10)) * 10,
#                       random.randrange(1, (window_y // 10)) * 10]
#
#     fruit_spawn = True
#
#     direction = 'RIGHT'
#     change_to = direction
#
#     score = 0
#
#     while True:
#
#         # handling key events
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     change_to = 'UP'
#                 if event.key == pygame.K_DOWN:
#                     change_to = 'DOWN'
#                 if event.key == pygame.K_LEFT:
#                     change_to = 'LEFT'
#                 if event.key == pygame.K_RIGHT:
#                     change_to = 'RIGHT'
#
#         if change_to == 'UP' and direction != 'DOWN':
#             direction = 'UP'
#         if change_to == 'DOWN' and direction != 'UP':
#             direction = 'DOWN'
#         if change_to == 'LEFT' and direction != 'RIGHT':
#             direction = 'LEFT'
#         if change_to == 'RIGHT' and direction != 'LEFT':
#             direction = 'RIGHT'
#
#         # Moving the snake
#         if direction == 'UP':
#             snake_position[1] -= 10
#         if direction == 'DOWN':
#             snake_position[1] += 10
#         if direction == 'LEFT':
#             snake_position[0] -= 10
#         if direction == 'RIGHT':
#             snake_position[0] += 10
#
#         snake_body.insert(0, list(snake_position))
#         if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
#             score += 10
#             fruit_spawn = False
#         else:
#             snake_body.pop()
#
#         if not fruit_spawn:
#             fruit_position = [random.randrange(1, (window_x // 10)) * 10,
#                               random.randrange(1, (window_y // 10)) * 10]
#
#         fruit_spawn = True
#         win.fill(black)
#
#         for pos in snake_body:
#             pygame.draw.rect(win, green,
#                              pygame.Rect(pos[0], pos[1], 10, 10))
#         pygame.draw.rect(win, white, pygame.Rect(
#             fruit_position[0], fruit_position[1], 10, 10))
#
#         # Game Over conditions
#         if snake_position[0] < 0 or snake_position[0] > window_x - 10:
#             game_over(win, score)
#         if snake_position[1] < 0 or snake_position[1] > window_y - 10:
#             game_over(win, score)
#
#         # Touching the snake body
#         for block in snake_body[1:]:
#             if snake_position[0] == block[0] and snake_position[1] == block[1]:
#                 game_over(win, score)
#
#         # displaying score countinuously
#         show_score(1, white, 'times new roman', 20, score, win)
#
#         # Refresh game screen
#         pygame.display.update()
#
#         # Frame Per Second /Refresh Rate
#         fps.tick(snake_speed)
#
#
#
# def run(config_path):
#     config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                                 neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                                 config_path)
#
#     p = neat.Population(config)
#     p.add_reporter(neat.StdOutReporter(True))
#     stats = neat.StatisticsReporter()
#     p.add_reporter(stats)
#     winner = p.run(main, 50)
#
# if __name__ == "__main__":
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, "neat_config.txt")
#     run(config_path)
