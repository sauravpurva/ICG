import pygame
from pygame import gfxdraw
import math
import sys

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

def create_line(x1, y1, x2, y2):
	dx = x1 - x2
	dy = y1 - y2

	steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

	Xinc = dx/math.floor(steps)
	Yinc = dy/math.floor(steps)

	X0 = x1
	Y0 = y1

	for x in range(0,steps+1):
		gfxdraw.pixel(screen, int(X0), int(Y0), red)
		X0 = X0 + Xinc
		Y0 = Y0 + Yinc
		pygame.display.update()


pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

create_line(x1,y1,x2,y2)

done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()
