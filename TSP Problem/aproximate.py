import numpy as np
import time
from datetime import timedelta

start_time = time.monotonic()

class MST:
  def __init__(self, adj_matrix):
    """Movimento Sem Terra"""
    self.matrix = adj_matrix
    self.size = self.matrix.shape[0]
    self.mst_set = np.empty(0)
    self.visited = np.zeros(self.size)
    self.expanded = np.empty(0)

    self.curr = 0
    self.end = 1
    self.total_cost = 0

  def remove(self, arr, elem):
    index = np.where(arr == elem)[0]
    return np.delete(arr, index)

  def lowest_cost(self, arr, starting_point):
    """Return the lowest cost path given a starting point"""
    cost = 0

    for elem in arr:
      if elem['start'] == starting_point:
        if cost == 0:
          cost = elem
        elif cost['cost'] > elem['cost']:
          cost = elem
      
    return cost

  def edge(self, start, end, cost):
    """Return formated dict for storing all attributes necessaries"""
    return {'start': start, 'end': end, 'cost': cost}

  def next_iteration(self, lowest_cost):
    """Append lowest cost to mst_set, remove it from expanded set, set and reset start and end point"""
    self.mst_set = np.append(self.mst_set, lowest_cost)
    self.expanded = self.remove(self.expanded, lowest_cost)

    self.curr = lowest_cost['end']
    self.end = 0

  def start(self):
    self.visited[0] = 1
    self.mst_set = np.append(self.mst_set, 0)

    for vertices in self.matrix[0]:
      if vertices == 0:
        pass
      else:
        self.expanded = np.append(self.expanded, self.edge(self.curr, self.end, vertices))
        self.end += 1
    
    self.next_iteration(self.lowest_cost(self.expanded, 0))

  def generate(self):
    self.start()

    for i in range(int(self.size) - 2):

      self.visited[self.curr] = 1

      for v in self.matrix[self.curr]:
        if not self.visited[self.end] and self.end != 0:
          self.expanded = np.append(self.expanded, self.edge(self.curr, self.end, v))
        
        self.end += 1

      self.next_iteration(self.lowest_cost(self.expanded, self.curr))

    last = self.mst_set[-1]
    self.mst_set = np.append(self.mst_set, self.edge(last['end'], 0, self.matrix[last['end']][0]))

    print(self.mst_set)



#Read file and organize lines in a matrice
file = open('/Users/carlosaugustocalage/Documents/Code/AEDIII/TSP Problem/data/tsp1_253.txt')

lines = list()

for line in file:
  lines.append(line.split())

file.close()

lines = np.array(lines).astype(int)

mst = MST(lines)

mst.generate()

end_time = time.monotonic()

print(timedelta(seconds=end_time - start_time))