import pygame
from pygame import gfxdraw
import math
import sys

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

def bresenham_line(x1, y1, x2, y2):
	xin = x1
	yin = y1
	xin1 = x2
	xin1 = y2

	dx = abs(x2 - x1)
	dy = abs(y2 - y1)

	decision_var = dx - 2*dy

	if dx == dy: # For case when slope = 1
		if xin < yin:
			for x in range(dx):
				gfxdraw.pixel(screen, xin, yin, red)
				xin += 1
				yin -= 1
				pygame.display.update()
		elif xin > yin:
			for x in range(dx):
				gfxdraw.pixel(screen, xin, yin, red)
				xin -= 1
				yin += 1
				pygame.display.update()	
		elif xin == yin:
			if xin < xin1:
				for x in range(dx):
					gfxdraw.pixel(screen, xin, yin, red)
					xin += 1
					yin += 1
					pygame.display.update()
			elif xin > xin1:
				for x in range(dx):
					gfxdraw.pixel(screen, xin, yin, red)
					xin -= 1
					yin -= 1
					pygame.display.update()	

	else: # For case when slop != 1
		for x in range(dx):
			if decision_var > 0:
				gfxdraw.pixel(screen, xin, yin, red)
				xin = xin + 1
				yin = yin
				decision_var = decision_var - 2*dy
				pygame.display.update()

			elif decision_var < 0:
				gfxdraw.pixel(screen, xin, yin, red)
				xin = xin + 1
				yin = yin + 1
				decision_var = decision_var -2*(dy - dx)
				pygame.display.update()

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 600]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

bresenham_line(x1,y1,x2,y2)

done = False
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()