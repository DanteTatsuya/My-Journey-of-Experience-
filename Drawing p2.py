#Rakhmonjon Karimov
#February 12, 2024
#This is a drawing of 10-sided polygon, 
#---additionally the pointer will have a shape as well as a color with their stamp

import turtle

dante = turtle.Turtle()

dante.color("Red") #This is a color of the polygon and I love Red!
dante.shape("turtle") #this is a shape of a pointer

for i in range(10):
    dante.forward(100)
    dante.stamp() #this is a stamp, meaning it will leave mark on each stamp
    dante.right(360/10) #since a circle is 360 and we are doing 10 side, we will devide it.