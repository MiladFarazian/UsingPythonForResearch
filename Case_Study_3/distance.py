import numpy as np
def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

p1 = np.array([1,1])
p2 = np.array([4,4])
print(distance(p1,p2))