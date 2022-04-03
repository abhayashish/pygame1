import pygame
import random
pygame.init()

#color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_hight = 600



#Creating window
gameWindow = pygame.display.set_mode((screen_width,screen_hight))

pygame.display.set_caption("snakes game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def  plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((200,220,229))
        text_screen("Welcame to Snake" , black, 260, 250)
        text_screen("Press Space Bar To Play", black, 230, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
# game loop
def gameloop():
    # Game specific veriables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_hight / 2)
    score = 0
    fps = 30  # frame pre sec


    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game over! press enter to continue", red, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # direct quit the game
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RETURN:
                        gameloop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # direct quit the game
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - 5
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 5
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                       velocity_y = 5
                       velocity_x = 0

                    if event.key == pygame.K_a:    #cheat code
                        score+=10
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            #abs() gives absolute value
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score+=10


                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_hight / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score" + str(score) +"  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y>screen_hight:
                game_over = True

            #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)    # update frams

    pygame.quit()
    quit()


welcome()
