#Game setup

#Import libraries
import pygame
from pygame import *
from random import randint
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
#Establish rates
SPAWN_RATE = 360

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

#Set up classes

#Create subclass of Sprite called VampireSprite
class VampireSprite(sprite.Sprite):
    #Define VampirePizza setup method
    def __init__(self):
        #Take behavior from Sprite class and use it for VampireSprite with the "super" function
        super().__init__()
        #Set default speed of VampireSprites
        self.speed = 2
        #Choose random lane for VampireSprite from 0-4
        self.lane = randint(0,4)
        #Add VampireSprites to a group called all_vampires
        all_vampires.add(self)
        #Use VAMPIRE_PIZZA as the sprite's image
        self.image = VAMPIRE_PIZZA.copy()
        #Set VampireSprite y coordinate (vertical location) in the middle of the lane selected by randint
        y = 50 + self.lane * 100
        #Create a rect object for each sprite and place it just off the right side of the screen in the correct lane such that Vampire Pizzas spawn from the right. (In Pygame, adding a rect to an object allows it to more easily interact with other game objects. An invisible rectangle is created to act on behalf of the image.)
        self.rect = self.image.get_rect(center = (1100, y))
    def update(self, game_window):
        game_window.blit(self.image, (self.rect.x, self.rect.y))

#Create class instances and groups
#Create a group for all VampireSprite instances
all_vampires = sprite.Group()

#Initialize and draw background grid
tile_color = WHITE
for row in range(6):
    draw.rect(BACKGROUND, tile_color, (0, HEIGHT * row, WIDTH, HEIGHT), 1)
    for column in range(11):
        draw.rect(BACKGROUND, tile_color, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 1)

#Display
GAME_WINDOW.blit(BACKGROUND, (0,0))

#Start Main Game Loop
game_running = True
#Game Loop
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    #Spawn Vampire Pizzas
    if randint(1, SPAWN_RATE) == 1:
        VampireSprite()
    #Update the display
    for vampire in all_vampires:
        vampire.update(GAME_WINDOW)
    display.update()
#End of main game loop
    
#Clean up game
pygame.quit()
