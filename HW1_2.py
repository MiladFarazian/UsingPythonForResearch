import math
print(math.pi/4)

import random

random.seed(1) # Fixes the see of the random number generator.

def rand():
   
    return random.uniform(-1,1)

rand()

def distance(x, y):
    (x1, x2) = x
    (y1, y2) = y
    return math.sqrt((y2 - x2)**2 + (y1 - x1)**2)

distance((0,0),(1,1))

def in_circle(x, origin = [0,0]):
   return distance(x, origin) < 1

in_circle((1,1))

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

print(- sum(inside)/R + (math.pi/4))