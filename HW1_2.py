"""Exercise 2
Consider a circle inscribed in a square. The ratio of their 
areas (the ratio of the area of the circle to the area of the
square) is  π4 . In this six-part exercise, we will find a way
to approximate this value.

Exercise 2a
Using the math library, calculate and print the value of  π4"""

import math
print(math.pi/4)

"""
0.7853981633974483

Exercise 2b
Using random.uniform(), create a function rand() that generates
a single float between −1 and 1.

Call rand() once. For us to be able to check your solution, 
we will use random.seed() to fix the seed value of the random 
number generator."""

import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   
    return random.uniform(-1,1)

rand()

"""
-0.7312715117751976

Exercise 2c
The distance between two points x and y is the square root of the
sum of squared differences along each dimension of x and y. Write
a functiondistance(x, y) that takes two vectors as its input and 
outputs the distance between them. Use your function to find the 
distance between x=(0,0) and y=(1,1).
"""

def distance(x, y):
    (x1, x2) = x
    (y1, y2) = y
    return math.sqrt((y2 - x2)**2 + (y1 - x1)**2)

distance((0,0),(1,1))

"""
1.4142135623730951

Exercise 2d
Write a function in_circle(x, origin) that determines whether a 
point in a two dimensional plane falls within a unit circle 
surrounding a given origin.

Your function should return a boolean True if the distance between
x and origin is less than 1 and False otherwise.

Use distance(x, y) as defined in 2c.
Use your function to determine whether the point (1,1) lies within 
the unit circle centered at (0,0).
"""

def in_circle(x, origin = [0,0]):
   return distance(x, origin) < 1

in_circle((1,1))

"""
False

Exercise 2e
Create a list inside of R=10000 booleans that determines whether
or not a point falls within the unit circle centered at (0,0).
Use the rand function from 2b to generate R randomly located 
points.

Use the function in_circle to test whether or not a given pint 
falls within the unit circle.

Find the proportion of points that fall within the circle by 
summing all True values in the inside list; then divide the answer
by R to obtain a proportion.
Print your answer. This proportion is an estimate of the ratio of 
the two areas!
"""

random.seed(1) 

R = 10000
inside = []
points = []
for i in range(R):
    point = [rand(), rand()]
    points.append(point)

for point in points:
    if (in_circle(point)):
        inside.append(1)
    else:
        inside.append(0)


print(sum(inside)/R)

"""
0.779

Exercise 2f
Find the difference between your estimate from part 2e and 
math.pi / 4. Note: inside and R are defined as in Exercise 2e.
"""

print(- sum(inside)/R + (math.pi/4))

"""
0.006398163397448253
"""