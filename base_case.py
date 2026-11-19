import heapq

def base_case(graph, B, S, k, distances):
  x = next(iter(S))
  U0 = set(S)
  H = [(distances[x],x)]

  print("Starting vertex:", x)
  print("Initial set:", U0)
  print("Initial heap:", H)

  while H and len(U0) < k + 1:
    distance, u = heapq.heappop(H)

    if distance != distances[u]:
      continue

    U0.add(u)

    for v, weight in graph[u]:
      new_distance = distances[u] + weight 

      if new_distance <= distances[v] and new_distance < B:
        distances[v] = new_distance
        heapq.heappush(H, (new_distance, v))
  print("Exploring vertex:", u)
  print("Updated distances:", distances)
  print("Updated heap:", H)
  print("Explored vertices:", U0)
  if len(U0) <= k:
    B_prime = B
  else:
    B_prime = max(distances[v] for v in U0)

  print("New boundry:", B_prime)
  U = set()
  for v in U0:
    if distances[v] < B_prime:
      U.add(v)
  print("Completed vertices:", U)
  return B_prime, U
