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


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
R = 1000
x = [random.uniform(0, 1) for i in range(0, 1000)] #Return a random floating point number N such that
   #a <= N <= b for a <= b 
   #and b <= N <= a for b < a.
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]
#print(len(Y))

print(([x] + moving_window_average(x, 5))[10])

ranges = [max(x)-min(x) for x in Y]
print(ranges)