"""
Exercise 3
A list of numbers representing measurements obtained from a
system of interest can often be noisy. One way to deal with
noise to smoothen the values by replacing each value with 
the average of the value and the values of its neighbors.

Exercise 3a
Write a function moving_window_average(x, n_neighbors) that
takes a list x and the number of neighbors n_neighbors on 
either side of a given member of the list to consider.

For each value in x, moving_window_average(x, n_neighbors) 
computes the average of the value and the values of its
neighbors.

moving_window_average should return a list of averaged values
that is the same length as the original list.
If there are not enough neighbors (for cases near the edge), 
substitute the original value for a neighbor for each missing
neighbor.
Use your function to find the moving window sum of 
x=[0,10,5,3,1,5] and n_neighbors=1.
"""

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    return [sum(x[i:(i+width)]) / width for i in range(n)]

x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))
print(sum(moving_window_average(x, 1)))


"""
[3.3333333333333335, 5.0, 6.0, 3.0, 3.0, 3.6666666666666665]
24.000000000000004

Exercise 3b
Compute and store R=1000 random values from 0-1 as x.
Compute the moving window average for x for values of 
n_neighbors ranging from 1 to 9 inclusive.

Store x as well as each of these averages as consecutive lists
in a list called Y
"""

random.seed(1) 
# This line fixes the value called by your function,
# and is used for answer-checking.
    
R = 1000
x = [random.uniform(0, 1) for i in range(0, 1000)] #Return a random floating point number N such that
   #a <= N <= b for a <= b 
   #and b <= N <= a for b < a.
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]
#print(len(Y))

print(([x] + moving_window_average(x, 5))[10])

"""
0.45325045824763405

Exercise 3c
For each list in Y, calculate and store the range (the maximum minus
the minimum) in a new list ranges.

Print your answer. As the window width increases, does the range of
each list increase or decrease? Why do you think that is?
"""

ranges = [max(x)-min(x) for x in Y]
print(ranges)

"""
[0.9973152343362711, 0.9128390185520854, 0.801645771909397,
0.7137391224212468, 0.6230146948375028, 0.5042284086774562,
0.5071013753101629, 0.4590090496908159, 0.44659549539083265,
0.4433696944090051]
"""