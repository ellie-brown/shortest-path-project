def find_pivots(graph, B, S, k, distances):
  W=set(S)
  W0=set(S)
  
  for i in range(1, k+1):
    W1=set()
   
    for u in W0:
      for v, weight in graph[u]:
        new_distance = distances[u] + weight
        
        if new_distance <= distances[v]:
          distances[v] = new_distance

        if new_distance < B:
            W1.add(v)
  
    W.update(W1)
    
    if len(W) > k * len(S):
      P = set(S)
      print("Stopping early!")
      print("Pivots:", P)
      print("Discovered vertices:", W)
      return P, W
   
    W0 = W1
    print("Round:", i)
    print("Distances:", distances)
    print("Discovered vertices:", W)
  
  F=[]
  for u in W:
    for v, weight in graph[u]:
      if v in W:
        if distances[u] + weight == distances[v]:
          F.append((u, v))
  print("Forest edges:", F)
  incoming = set()

  for u,v in F:
    incoming.add(v)
  roots = S - incoming
  print("Roots:", roots)
 
  P = set()
  for root in roots:
    visited = set()
    stack = [root]

    while stack:
      current = stack.pop()

      if current not in visited:
        visited.add(current)

        for u, v in F:
          if u == current:
            stack.append(v)
    print("Root:", root)
    print("Tree size:", len(visited))

    if len(visited) >= k:
      P.add(root)
  
  print("Finished all rounds!")
  print("Dicovered vertices:", W)
  
  print("Pivots:", P)
  return P, W



example_graph = {
    0: [(1,2), (2,4)],
    1: [(3,3)],
    2: [(4,1)],
    3: [],
    4: []
}

distances = {
    0: 0,
    1: float("inf"),
    2: float("inf"),
    3: float("inf"),
    4: float("inf"),
}
find_pivots(example_graph, 10, {0}, 6, distances)

