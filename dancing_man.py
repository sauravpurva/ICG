import pygame
from pygame import gfxdraw
import math
import sys
import time

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
size = [700, 500]
screen = pygame.display.set_mode(size) #Opens a window of size 700,500, and stores it in a variable called screen
screen.fill(white)

def fig_1():
	pygame.draw.circle(screen, black, [300,160], 40, 1) # head

	pygame.draw.lines(screen,black,False,[(300,200),(300,270)], 1) #upper body

	pygame.draw.lines(screen,black,False,[(300,270),(260,330)], 1) #right leg
	pygame.draw.lines(screen,black,False,[(300,270),(340,330)], 1) #left leg

	pygame.draw.lines(screen,black,False,[(300,230),(340,260)], 1) #right hand_1
	pygame.draw.lines(screen,black,False,[(300,230),(260,260)], 1) #left hand_1

def fig_2():
	pygame.draw.circle(screen, black, [300,160], 40, 1) # head

	pygame.draw.lines(screen,black,False,[(300,200),(300,270)], 1) #upper body

	pygame.draw.lines(screen,black,False,[(300,270),(250,300)], 1) #right leg
	pygame.draw.lines(screen,black,False,[(250,300),(280,330)], 1) #right leg

	pygame.draw.lines(screen,black,False,[(300,270),(350,300)], 1) #left leg
	pygame.draw.lines(screen,black,False,[(350,300),(320,330)], 1) #left leg

	pygame.draw.lines(screen,black,False,[(300,230),(340,200)], 1) #right hand_1
	pygame.draw.lines(screen,black,False,[(300,230),(260,200)], 1) #left hand_1


def change_person(flag):
	if flag == 0:
		fig_1()
	elif flag == 1:
		fig_2()

done = False
flag = 0
while True:
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			pygame.quit()
			sys.exit()

	change_person(flag)
	pygame.display.update()
	pygame.time.delay(500)
	screen.fill(white)

	flag = 1 if flag == 0 else 0
