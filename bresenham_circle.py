import pygame
from pygame import gfxdraw
import math
import sys

xc = int(input("xc: "))
yc = int(input("yc: "))
r = int(input("r: "))

def draw_circle(xc, yc, x, y): 
	gfxdraw.pixel(screen, xc + x, yc + y, red)
	gfxdraw.pixel(screen, xc - x, yc + y, red)
	gfxdraw.pixel(screen, xc + x, yc - y, red)
	gfxdraw.pixel(screen, xc - x, yc - y, red)
	gfxdraw.pixel(screen, xc + y, yc + x, red)
	gfxdraw.pixel(screen, xc + y, yc - x, red)
	gfxdraw.pixel(screen, xc - y, yc + x, red)
	gfxdraw.pixel(screen, xc - y, yc - x, red)
	pygame.display.update()


def bresenham_circle(xc, yc ,r):
	x = 0
	y = r
	decision_var = 3 - 2*r
	draw_circle(xc, yc, x, y)
	while y >= x:
		x += 1

		if decision_var > 0:
			y -= 1
			decision_var = decision_var + 4 * (x - y) + 10
		else:
			decision_var = decision_var + 4 * x + 6
		draw_circle(xc, yc, x, y)

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 600]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

bresenham_circle(xc, yc ,r)

done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()