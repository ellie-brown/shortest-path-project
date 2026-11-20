import math
from bmssp import bmssp
def shortest_paths(graph, source):
  distances = {v: float("inf") for v in graph}
  distances[source] = 0
  n = len(graph)
  log_n = math.log2(n)
  k = max(1, math.floor(log_n ** (1/3)))
  t = max(1, math.floor(log_n ** (2/3)))
  l = math.ceil(log_n / t)
  print("k:", k)
  print("t:", t)
  print("Level:", l)
  bmssp(graph, l, float("inf"), {source}, k, t, distances)
  return distances
