import pygame
import sys
import os
import random
import math
pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

#we will declsre global constant definitions


speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE    #we will keep both food and size of snake same
SEPARATION =10             #separation betwwen two pixels
SCREEN_HIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP","DOWN","LEFT","RIGHT"}

#



