# imports for pygame
import pygame, sys
from pygame.locals import *

# canvas variables
width = <SET WIDTH OF SCREEN (INT)> # adjust for width of canvas
height = <SET HEIGHT OF SCREEN (INT)> # adjust for height of canvas

# colors
background_color = <SET BACKGROUND COLOR HERE IN R,G,B (TUPLE OF INTS)>

# initializing pygame, setting up the surface (canvas)
pygame.init()
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("<YOUR DISPLAY CAPTION GOES HERE (STRING)>") # add a caption for your canvas

# import assets
sprite_sheet = pygame.image.load("<YOUR FILE AND PATH GO HERE (STRING)>").convert_alpha() # add the path/name of your sprite sheet file

# get details about individual sprites
total_sprites = <ENTER NUMBER OF SPRITES HERE (INT)> # code the number of sprite images your sprite sheet has
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height

# adjust sprite size
sprite_scale_factor = <INSERT YOUR SCALE FACTOR HERE (DECIMAL)>
sprite_sheet_width = sprite_sheet_width * sprite_scale_factor
sprite_sheet_height = sprite_sheet_height * sprite_scale_factor
sprite_sheet = pygame.transform.scale(sprite_sheet, (sprite_sheet_width, sprite_sheet_height))
sprite_sheet_width = sprite_sheet.get_rect().width
sprite_sheet_height = sprite_sheet.get_rect().height
sprite_width = sprite_sheet_width // total_sprites
sprite_height = sprite_sheet_height

# define initial x and y position of sprite
sprite_x_pos = 0
sprite_y_pos = 0
sprite_x_delta = <INSERT HOW MUCH YOU WANT YOUR SPRITE TO MOVE HORIZONTALLY (INT)>
sprite_y_delta = <INSERT HOW MUCH YOU WANT YOUR SPRITE TO MOVE VERTICALLY (INT)>

# load sprite sheet into list
sprite_list = []
for i in range(total_sprites):
    rect = pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height)
    image = sprite_sheet.subsurface(rect)
    sprite_list.append(image)

# sprite picker function for animation
sprite_index = 0
counter = 0
def spritePicker():
    global sprite_index
    if counter % 20 == 0:
        if sprite_index == total_sprites - 1:
            sprite_index = 0
        else:
            sprite_index += 1

# clock to set FPS
clock = pygame.time.Clock()

# variable to control state of entire game
running = True

# main game loop
while running:
    # paint the canvas with background color
    canvas.fill(background_color)

    # poll for events
    for event in pygame.event.get():
        # if 'X' is clicked on the canvas
        if event.type == QUIT:
            running = False

    # get all keys that are currently pressed    
    keys = pygame.key.get_pressed()

    # check to see if any of the keys are w, a, s, or d
    # and perform an action
    if keys[pygame.K_w]:
        sprite_y_pos -= sprite_y_delta
    if keys[pygame.K_s]:
        sprite_y_pos += sprite_y_delta
    if keys[pygame.K_a]:
        sprite_x_pos -= sprite_x_delta
    if keys[pygame.K_d]:
        sprite_x_pos += sprite_x_delta

    canvas.blit(sprite_list[sprite_index], (sprite_x_pos, sprite_y_pos))
    spritePicker()
    pygame.display.update()
    counter += 1
    clock.tick(60)

# close pygame down
pygame.quit()
sys.exit()