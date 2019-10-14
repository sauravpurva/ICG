import pygame
from pygame import gfxdraw
import math
import sys
import time

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (176, 224, 230)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

def bouncing_ball():

	r = 100 

	for i in range(5):
		radius = r+(4*i)
		pygame.draw.circle(screen, black, [350,400-(30*i)], radius, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)

	for i in range(4):
		radius1 = radius+(4*i)
		pygame.draw.circle(screen, black, [350,280+(30*i)], radius1, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)
		
	for i in range(5):
		radius2 = radius1+(4*i)
		pygame.draw.circle(screen, black, [350,330-(30*i)], radius2, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)

	for i in range(5):
		radius3 = radius2+(4*i)
		pygame.draw.circle(screen, black, [350,220+(30*i)], radius3, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)

	for i in range(6):
		radius4 = radius3+(8*i)
		pygame.draw.circle(screen, black, [350,330-(30*i)], radius4, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)

	for i in range(3):
		radius5 = radius4+(12*i)
		pygame.draw.circle(screen, black, [350,220+(30*i)], radius5, 1) 
		pygame.display.update()
		pygame.time.delay(100)
		screen.fill(white)

	for i in range(1): # final 
		radius6 = radius5+(25*i)
		pygame.draw.circle(screen, black, [350,200-(30*i)], radius6, 1) 
		pygame.display.update()
		pygame.time.delay(100)

bouncing_ball()

done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()



