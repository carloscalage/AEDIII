import numpy as np
import itertools
import time
from datetime import timedelta

start_time = time.monotonic()

#Read file and organize lines in a matrice
file = open('/Users/carlosaugustocalage/Documents/Code/AEDIII/TSP Problem/data/tsp2_1248.txt')

lines = list()

for line in file:
  lines.append(line.split())

file.close()

lines = np.array(lines)

#Size of input
n = lines.shape[0]

pathIndex = np.arange(n)

result = {'path': pathIndex, 'cost': 0}

#First cost
cost = 0

for i in range(n-1):
  cost += int(lines[i][i+1])

cost += int(lines[n-1][0])

result['cost'] = cost 

#Iteration over permutations to find out wich is the lowest cost path
permutations = itertools.permutations(pathIndex)

for possibility in permutations:
  cost = 0

  for i in range(n - 1):
    cost += int(lines[possibility[i]][possibility[i+1]])

  cost += int(lines[possibility[n-1]][possibility[0]])

  if cost < result['cost']:
    result['cost'] = cost
    result['path'] = possibility

print(result)

end_time = time.monotonic()

print(timedelta(seconds=end_time - start_time))





