import numpy as np

def distance(p1,p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

import scipy.stats as ss
def majority_vote(votes):
    """Return the most common element in votes"""
    mode, count = ss.mstats.mode(votes)
    return int(mode)

def find_nearest_neighbors(p, points, k=5):
    """Find the k-nearest neighbors of point p and return their indices."""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])

def generate_synth_data(n=50):
    np.concatenate((ss.norm(0,1)))

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5,2])
outcomes = np.array([0,0,0,0,1,1,1,1,1])

ind = knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2)
print(ind)

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
#plt.show()