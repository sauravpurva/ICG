import pygame
from pygame import gfxdraw
import math
import sys

x0 = int(input("x: "))
y0 = int(input("y: "))
r = int(input("r: "))

def create_circle(x0 ,y0 ,r):

	list = []
	for i in range(0,360):
		x = x0 + r*math.cos(math.degrees(i/10))
		y = y0 + r*math.sin(math.degrees(i/10))
		list.append([x,y])

	for i in range(len(list)):
		gfxdraw.pixel(screen, int(list[i][0]), int(list[i][1]),red)
		pygame.display.update()

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

create_circle(x0,y0,r)

done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()
