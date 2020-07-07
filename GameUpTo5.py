#Game setup

#Import libraries
import pygame
from pygame import *
#Initialize pygame
pygame.init()

#Define constants
#Game window parameters
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

#Tile parameters
WIDTH = 100
HEIGHT = 100
#Define colors
WHITE = (225, 225, 225)

#Load assets

#Create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas')

#Setup background
background_img = image.load("restaurant.jpg")
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)

#Setup enemy image - load, then convert to surface
pizza_img = image.load("vampire.png")
pizza_surf = Surface.convert_alpha(pizza_img)
#Scale image
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH, HEIGHT))
#Initialize and draw background grid
tile_color = WHITE
for row in range(6):
    draw.rect(BACKGROUND, tile_color, (0, HEIGHT * row, WIDTH, HEIGHT), 1)
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)

#Display
GAME_WINDOW.blit(BACKGROUND, (0,0))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))

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
