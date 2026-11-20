# shortest-path-project
Comparing Dijkstra's algorithm with a newer shortest-path algorithm

## Project Overview
Dijkstra's algorithm is a well known method for finding shortest paths in graphs with nonnegative edge weights. This project explores a newer shortest-path algorithm called BMSSP and compares the distance it calculates with Dijkstra's results. The purpose is to understand how the newer approach works and test whether the two implementations produce matching answers. 

## Files
graph_generator.py - This file generates random directed graphs with weighted edges.
dijkstra.py - Uses Dijkstra's algorithm to calculate shortest-path distances
find_pivots.py - The purpose of this file is to identify pivot vertices used by the newer algorithm. 
base_case.py - This file handles smaller subproblems in the recursive algorithm.
bmssp.py - Combines pivot finding, recursion, and distance updates.
shortest_paths.py - This file sets up and runs the BMSSP-based algorithm.
test_algorithms.py - Tests whether both implementations produce matching distances.

## How to Run
To run this project, you must have Python installed. Then, download the project files and make sure all seven Python files are saved in the same folder. Open a terminal in that folder and enter the command: 
python test_algorithms.py
This runs the test graphs through both Dijkstra's algorithm and the BMSSP-based algorithm. The program displays the shortest-path distances calculated by each algorithm and prints Results match: True when both algorithms produce the same results. 

## Testing
I used four different graphs to test the shortest path algorithms. I started with two smaller graphs containing 5 and 6 vertices. After that, I generated two random graphs with 10 and 20 vertices. For each of the graphs, I ran both Dijkstra's algorithm and my BMSSP-based implementation using vertex 0 as the starting point. I compared the shortest path distances returned by each algorithm. All four tests produced matching results, suggesting that my implementation works correctly for these examples. 

## Implementation Differences and Limitations 
My implementation uses a Python dictionary that stores vertices and their distances instead of the specialized data structure that is described in the original BMSSP paper. I chose a simpler approach because it was easier to implement and understand while learning how the recursive algorithm works. This implementation skips the degree-reduction step, this limits the number of incoming and outgoing edges for each vertex. When multiple vertices have the same shortest-path distance, the recursive boundary handling may temporarily leave some vertices out of the completed set.

## AI Assistance 
GitHub Copilot Autocompletion was used during the for loops and other parts of this project. 
