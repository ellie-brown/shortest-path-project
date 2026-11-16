import heapq
def dijkstra(graph, start):
  distances = {vertex: float("inf") for vertex in graph}
  distances[start]=0
  priority_queue=[(0, start)]
  while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)
    if current_distance > distances[current_vertex]:
      continue 
    for neighbor, weight in graph[current_vertex]: 
      new_distance = current_distance + weight 
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heapq.heappush(priority_queue, (new_distance, neighbor))
    return distances

if __name__ == "__main__":
  example_graph = {
    0: [(1,4), (2,2)], 
    1: [(3,1)],
    2: [(1,1), (3,5)],
    3: []
  }
  print(dijkstra(example_graph, 0))
  


    
