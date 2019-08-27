import pygame
import time
import random


# display dimension
display_width = 800
display_height = 600

# car dimension
car_width = 70
car_height = 140

# colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (53, 115, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
gray = (47, 79, 79)
yellow = (255, 255, 0)

FPS = 15


class cargame():
    def __init__(self):
        self.game_display = pygame.display.set_mode(
            (display_width, display_height))
        self.clock = pygame.time.Clock()
        # game setup
        pygame.init()
        pygame.display.set_caption('Car-Game')
        self.pause = False
        self.main()

    def display(self, count, x, y, message_format='Dodged: %d'):
        """display the score"""
       # max_dodged = 10
        self.font = pygame.font.SysFont("Lucida Sans Roman", 20)
        text = self.font.render(message_format % count, False, black)
        self.game_display.blit(text, (x, y))

    def obs(self, obsX, obsY, obsW, obsH, color):
        """draw random obs (car or anyobs)"""
        pygame.draw.rect(self.game_display, color, [obsX, obsY, obsW, obsH])

    def line(self, lineX, lineY, lineW, lineH, color):
        """draw way lines """
        pygame.draw.rect(self.game_display, color, [
                         lineX, lineY, lineW, lineH])

    def load_image(self, x, y, image_name):
        img = pygame.image.load(image_name)
        self.game_display.blit(img, (x, y))

    def text_object(self, text, font):
        textSurface = font.render(text, False, black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        """display message after crash"""
        largeText = pygame.font.SysFont("Lucida Sans Roman", 115)
        textSurf, textRect = self.text_object(text, largeText)
        textRect.center = ((display_width / 2), (display_height / 2))
        self.game_display.blit(textSurf, textRect)

        pygame.display.update()

        time.sleep(2)

        game_loop()

    def crash(self, x, y):
        car_crash = pygame.image.load('images/carcrash.png')
        self.game_display.blit(car_crash, ((x - 45), (y - 30)))
        largeText = pygame.font.SysFont("comicsansms", 90)
        textSurf, textRect = self.text_object("You Crashed!", largeText)
        textRect.center = ((display_width / 2), (display_height / 4))
        self.game_display.blit(textSurf, textRect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.button("Play Again", 150, 250, 100, 50,
                        green, bright_green, self.game_loop)
            self.button("Quit", 550, 250, 100, 50,
                        red, bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(15)

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        """message, dimension, active/inactive color"""

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.game_display, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                action()

        else:
            pygame.draw.rect(self.game_display, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("Lucida Sans Roman", 20)
        textSurf, textRect = self.text_object(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.game_display.blit(textSurf, textRect)

    def quitgame(self):
        pygame.quit()
        quit()

    def game_unpause(self):
        self.pause = False

    def game_pause(self):
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # gameDisplay.fill(gray)
            largeText = pygame.font.SysFont("Lucida Sans Roman", 90)
            textSurf, textRect = self.text_object("Pause!", largeText)
            textRect.center = ((display_width / 2), (display_height / 4))
            self.game_display.blit(textSurf, textRect)

            self.button("Continue !", 150, 250, 100, 50,
                        green, bright_green, self.game_unpause)
            self.button("Quit", 550, 250, 100, 50,
                        red, bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(FPS)

    def game_intro(self):

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.game_display.fill(gray)

            largeText = pygame.font.SysFont("Lucida Sans Roman", 80)
            textSurf, textRect = self.text_object(
                "Let's Ride !", largeText)
            textRect.center = ((display_width / 2), (display_height / 2))
            self.game_display.blit(textSurf, textRect)

            self.button("GO !", 150, 450, 100, 50,
                        green, bright_green, self.game_loop)
            self.button("Quit", 550, 450, 100, 50,
                        red, bright_red, self.quitgame)

            pygame.display.update()
            self.clock.tick(FPS)

    def game_loop(self):

        x = (display_width * 0.45)
        y = (display_height * 0.75)

        x_change = 0
        y_change = 0
        speed_change = 0

        obs_width = 70
        obs_height = 140

        obs_startx = random.randrange(100, display_width - 200)
        obs_starty = -600
        obs_speed = 4

        lineX = 400
        lineY = 0
        lineW = 20
        lineH = 450
        line_speed = 10

        tree_y_right = 600
        tree_y_left = 300
        tree_h = 600
        tree_speed = 10

        dodged = 0

        gameExit = False

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5

                    if event.key == pygame.K_p:
                        self.pause = True
                        self.game_pause()

                if event.type == pygame.KEYUP:
                    x_change = 0
            x += x_change

            self.game_display.fill(gray)

            self.line(150, 0, 20, display_height, yellow)
            self.line(display_width - 150, 0, 20, display_height, yellow)

            self.load_image(obs_startx, obs_starty, 'images/car.png')
            self.load_image(80, tree_y_left, 'images/trees.jpg')
            self.load_image(700, tree_y_right, 'images/trees.jpg')
            self.load_image(x, y, 'images/car1.png')

            obs_starty += obs_speed
            lineY += line_speed
            tree_y_left += tree_speed
            tree_y_right += tree_speed

            self.display(dodged, 5, 25)
            # display(obs_speed*60 , 5, 50, "Spd: %d px/s")

            if x > display_width - car_width - 150 or x < 150:
                # 100 way background image
                self.crash(x, y)

            if obs_starty > display_height:
                obs_starty = 0 - obs_height  # reset y
                obs_startx = random.randrange(
                    170, display_width - obs_width - 150)
                dodged += 1
                obs_speed += 1 / 20  # accelarate

            if lineY > display_height:
                lineY = 0 - lineH  # reset y
                obs_speed += 1 / 15

            if tree_y_left > display_height:
                tree_y_left = 0 - tree_h  # reset y
                obs_speed += 1 / 15

            if tree_y_right > display_height:
                tree_y_right = 0 - tree_h  # reset y
                obs_speed += 1 / 15

            # check crash
            if y < (obs_starty + obs_height) and y + car_height >= obs_starty + obs_height:
                if x > obs_startx and x < (obs_startx + obs_width) or x + car_width > obs_startx \
                        and x + car_width < obs_startx + obs_width:
                    self.crash(x, y)

            pygame.display.update()
            self.clock.tick(60)

    def main(self):
        self.game_intro()
        self.game_loop()
        pygame.quit()
        self.quit()


if __name__ == '__main__':
    game = cargame()
