from turtle import *

def rainbow1():
	width = 30
	radius = 200
	y_start = radius
	pensize(width+1)
	# Draw red half-circle
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('red')
	circle(radius,-180)
	# Draw orange half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('orange')
	circle(radius,-180)
	# Draw yellow half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('yellow')
	circle(radius,-180)
	# Draw green half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('green')
	circle(radius,-180)
	# Draw blue half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('blue')
	circle(radius,-180)
	# Draw pink half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('pink')
	circle(radius,-180)
	# Draw violet half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('violet')
	circle(radius,-180)

def rainbow2():
	width = 30
	radius = 200
	y_start = -radius
	pensize(width+1)
	# Draw red half-circle
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('red')
	circle(radius,180)
	# Draw orange half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('orange')
	circle(radius,180)
	# Draw yellow half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('yellow')
	circle(radius,180)
	# Draw green half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('green')
	circle(radius,180)
	# Draw blue half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('blue')
	circle(radius,180)
	# Draw pink half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('pink')
	circle(radius,180)
	# Draw violet half-circle
	radius -= width
	penup()
	setposition(radius, y_start)
	setheading(90)
	pendown()
	pencolor('violet')
	circle(radius,180)

rainbow1()
rainbow2()
# Finish
hideturtle()