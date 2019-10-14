import pygame
from pygame import gfxdraw
import math
import sys

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

pygame.draw.lines(screen,black,False,[(150,200),(150,300)], 1)
pygame.draw.lines(screen,black,False,[(250,200),(250,300)], 1)
pygame.draw.lines(screen,black,False,[(150,200),(250,200)], 1)

pygame.draw.lines(screen,black,False,[(150,300),(250,300)], 1)
pygame.draw.lines(screen,black,False,[(150,200),(200,125)], 1)
pygame.draw.lines(screen,black,False,[(250,200),(200,125)], 1)

pygame.draw.lines(screen,black,False,[(200,125),(350,125)], 1)
pygame.draw.lines(screen,black,False,[(250,200),(400,200)], 1)
pygame.draw.lines(screen,black,False,[(250,300),(400,300)], 1)

pygame.draw.lines(screen,black,False,[(350,125),(400,200)], 1)
pygame.draw.lines(screen,black,False,[(400,200),(400,300)], 1)

x1 = 200
x2 = 250

#inclined lines
for i in range(0,10):
	pygame.draw.lines(screen,black,False,[(x1,125),(x2,200)], 1)
	x1 += 15
	x2 += 15

#window
pygame.draw.lines(screen,black,False,[(290,230),(360,230)], 1)
pygame.draw.lines(screen,black,False,[(290,270),(360,270)], 1)
pygame.draw.lines(screen,black,False,[(290,230),(290,270)], 1)
pygame.draw.lines(screen,black,False,[(360,230),(360,270)], 1)
pygame.draw.lines(screen,black,False,[(325,230),(325,270)], 1)

#gate
pygame.draw.lines(screen,black,False,[(180,240),(180,300)], 1)
pygame.draw.lines(screen,black,False,[(220,240),(220,300)], 1)
pygame.draw.lines(screen,black,False,[(180,240),(220,240)], 1)

#circle
pygame.draw.circle(screen, black, (200, 175), 15, 1)

pygame.display.update() #nothing is drawn


done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()