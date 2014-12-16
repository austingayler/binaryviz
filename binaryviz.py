#! /usr/bin/env python

import sys
import pygame
from pygame.locals import *

pygame.init()

width = 200				# set these to whatever you want
height = 200
ON = (0,0,0)            # BLACK
OFF = (255,255,255)     # WHITE

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill(OFF)

for y in range(height):
        bin_str = bin(y)[2:]	# counter variable to binary string, removes '0b' at beginning
        bin_str_len = len(bin_str) - 1	# string length for loop var, -1 b/c 0 based
        for x in range(bin_str_len):
                cur_bit = bin_str[x]
                if cur_bit == '1':		# if current bit is 1, paint the pixel black
                        offset = width - bin_str_len + x
                        screen.set_at((offset, y), ON)
        pygame.display.flip()
        
pygame.image.save(screen, "out.png")	# save screen to file

while True:	# show the screen until the user closes it
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit(0)
                #else:
                        #print event
