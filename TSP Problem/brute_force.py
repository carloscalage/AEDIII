import numpy as np

file = open('/Users/carlosaugustocalage/Documents/Code/AEDIII/TSP Problem/data/tsp1_253.txt')

lines = list()

for line in file:
  lines.append(line.split())

file.close()

lines = np.array(lines)
