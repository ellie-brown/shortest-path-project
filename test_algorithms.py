import random 
from graph_generator import generate_graph
from dijkstra import dijkstra
from shortest_paths import shortest_paths

example_graph = {
    0: [(1, 2), (2, 4)],
    1: [(3, 3)],
    2: [(4, 1)],
    3: [],
    4: []
}

bmssp_result = shortest_paths(example_graph, 0)
dijkstra_result = dijkstra(example_graph, 0)

print("BMSSP", bmssp_result)
print("Dijkstra:", dijkstra_result)
print("Results match:", bmssp_result == dijkstra_result)

test_graph = {
    0: [(1, 3), (2, 7)],
    1: [(2,2), (3,5)],
    2: [(3, 1), (4,4)],
    3: [(4, 2)], 
    4: [(5, 3)],
    5: []
}
bmssp_result = shortest_paths(test_graph, 0)
dijkstra_result = dijkstra(test_graph, 0)

print("BMSSP", bmssp_result)
print("Dijkstra:", dijkstra_result)
print("Results match:", bmssp_result == dijkstra_result)



random.seed(42)
random_graph = generate_graph(10, 20)
print(random_graph)
bmssp_result = shortest_paths(random_graph, 0)
dijkstra_result = dijkstra(random_graph, 0)

print("BMSSP:", bmssp_result)
print("Dijkstra:", dijkstra_result)
print("Results match:", bmssp_result == dijkstra_result)



random.seed(43)
random_graph = generate_graph(20, 60)
print(random_graph)
bmssp_result = shortest_paths(random_graph, 0)
dijkstra_result = dijkstra(random_graph, 0)

print("BMSSP:", bmssp_result)
print("Dijkstra:", dijkstra_result)
print("Results match:", bmssp_result == dijkstra_result)
