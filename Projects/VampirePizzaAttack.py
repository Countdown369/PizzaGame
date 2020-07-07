#Game setup

#Import libraries
import pygame
from pygame import *
#Initialize pygame
pygame.init()

#Define constants
#Game window parameters
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 400
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Load assets

#Create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas')

#Setup enemy image
#Load image
pizza_img = image.load('vampire.png')
#Convert image to a surface (pygame usable image)
pizza_surf = Surface.convert_alpha(pizza_img)
#The 'convert_alpha' function converts images with an alpha channel (transparency), while 'convert' will do it for opaque images
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (150, 150))
#The 'blit' function shows a surface on screen.

#Start Main Game Loop
game_running = True
#Game Loop
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    display.update()
#End of main game loop
    
#Clean up game
pygame.quit()
