from find_pivots import find_pivots
from base_case import base_case
def bmssp(graph, l, B, S, k, t, distances):
  if l == 0:
    return base_case(graph, B, S, k, distances)
  P, W = find_pivots(graph, B, S, k, distances)
  print("Pivots:", P)
  print("Discovered vertices:", W)
  D = {}
  for p in P:
    D[p] = distances[p]
  print("Initial frontier:", D)
  U = set()
  M = 2 ** ((l - 1) * t)

  limit = k * 2 ** (l * t)

  Bi_prime = B

  while D and len(U) <= limit:
      Si = set(sorted(D, key=D.get)[:M])

      print("Group size:", M)
      print("Selected vertices:", Si)

      for p in Si:
        del D[p]
      if D:
        Bi = min(D.values())
      else:
        Bi = B
      print("Group boundary:", Bi)

      Bi_prime, Ui = bmssp(graph, l - 1, Bi, Si, k, t, distances)
      U.update(Ui)

      print("Returned boundary:", Bi_prime)
      print("Completed vertices:", U)

      K = {}

      for u in Ui:
        for v, weight in graph[u]:
          new_distance = distances[u] + weight
          if new_distance <= distances[v]:
            distances[v] = new_distance
            if Bi <= new_distance < B:
              D[v] = new_distance
            elif Bi_prime <= new_distance < Bi:
              K[v] = new_distance
      print("Updated frontier:", D)
      print("K:", K)
      for v in Si:
        if Bi_prime <= distances[v] < Bi:
          K[v] = distances[v]
      D.update(K)
      print("Refilled frontier:", D)

  if not D:
      B_prime = B
  else:
      B_prime = min(B, Bi_prime)
  for v in W:
      if distances[v] < B_prime:
        U.add(v)
  print("Final boundary:", B_prime)
  print("Final completed vertices:", U)

  return B_prime, U
