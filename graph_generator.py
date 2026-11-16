import random 
def generate_graph(n,m):
  if n < 1 or m < 0 or m >n * (n-1):
    raise ValueError("Invalid number of vertices or edges")
  graph ={i: [] for i in range(n)}
  possible_edges = [
    (u,v)
    for u in range(n)
    for v in range(n)
    if u != v
  ]
  chosen_edges = random.sample(possible_edges, m)
  for u, v in chosen_edges:
    weight = random.randint(1,10)
    graph[u].append((v, weight))
  return graph
if __name__ =="__main__":
  graph = generate_graphs(5, 8)
  for vertex, neighbors in graph.items():
    print(f"{vertex}: {neighbors}")

