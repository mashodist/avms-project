Autonomous Vehicle Management System (AVMS)

A Python-based implementation of an Autonomous Vehicle management system. This project leverages custom Abstract Data Types (ADTs)—Graph, Hash Table, and Heap—alongside Heapsort and Quicksort algorithms to manage a fleet of autonomous vehicles on a road network. Designed to demonstrate proficiency in Python, data structures, and algorithm design.

Project Overview

The AVMS is a system for managing a fleet of autonomous vehicles, supporting real-time operations like adding vehicles, updating their locations, and recommending vehicles based on proximity to destinations or battery levels. It models a road network as a graph, stores vehicle data in a hash table, and uses sorting algorithms for recommendations, all implemented with custom ADTs to meet the assignment’s requirement of avoiding built-in Python libraries (e.g., collections, heapq).

Key Features





Road Network Management: Represented as a graph, allowing users to add locations (nodes), roads (edges), display the network, and check path existence between locations using Depth-First Search (DFS).



Vehicle Management: Stores vehicles in a hash table with linear probing for collision resolution, supporting insertion, deletion, search, and display of vehicle details (ID, location, destination, distance, battery level).



Vehicle Recommendations:





Heapsort sorts vehicles by distance to destination (ascending) to recommend the nearest vehicle.



Quicksort sorts vehicles by battery level (descending) to recommend the vehicle with the highest battery.



Interactive Menu: A user-friendly interface with robust error handling for invalid inputs (e.g., duplicate IDs, non-existent locations).



Error Fixes: Resolved issues with duplicate vehicle IDs and inconsistent updates by synchronizing data storage and enhancing validation.

Data Structures and Their Role in AVMS

The AVMS relies on three custom ADTs—Graph, Hash Table, and Heap—each chosen for its efficiency in handling specific system requirements. Below, I explain each data structure’s concept, implementation, and application in the AVMS.

1. Graph (Road Network Representation)





Concept: A graph is a data structure consisting of nodes (vertices) connected by edges, ideal for modeling networks like road systems. In AVMS, nodes represent locations (e.g., “Downtown”, “Airport”), and edges represent roads with associated distances (e.g., 10km). Graphs support operations like adding nodes/edges, retrieving neighbors, and path finding.



Implementation: The DSAGraph class uses a dictionary mapping location labels to DSAGraphNode objects. Each node stores a list of adjacent nodes (neighbors) and a dictionary of edge distances. Path existence is checked using DFS, a traversal algorithm that explores as far as possible along each branch before backtracking.



Application in AVMS:





Adding Locations/Roads: Users add locations (e.g., add_node("Downtown")) and roads (e.g., add_edge("Downtown", "Airport", 10)), building the network dynamically.



Displaying Network: The display method prints each location and its neighbors with distances (e.g., Downtown: [('Airport', 10)]).



Path Checking: The is_path("Downtown", "Airport") method uses DFS to confirm if a path exists, returning True if reachable, False otherwise. This ensures vehicles can navigate between locations.



Efficiency:





Adding node/edge: O(1).



DFS path check: O(V + E), where V is the number of vertices and E is the number of edges.



Why Used: Graphs are perfect for modeling real-world road networks, enabling path validation critical for autonomous vehicle routing.

2. Hash Table (Vehicle Storage)





Concept: A hash table is a data structure that maps keys to values using a hash function to compute an index, offering fast insertion, deletion, and search (O(1) average case). Collisions (multiple keys mapping to the same index) are resolved using techniques like linear probing.



Implementation: The VehicleHashTable class uses an array of DSAHashEntry objects (key: vehicle ID, value: Vehicle object). The hash function sums the ASCII values of the ID’s characters modulo the table size. Linear probing resolves collisions by finding the next free slot. The table resizes (doubles) when the load factor exceeds 70%.



Application in AVMS:





Vehicle Management: Vehicles are stored with unique IDs (e.g., put("V1", vehicle)), allowing quick lookup (get("V1")), deletion (remove("V1")), and display of all vehicles.



Duplicate Prevention: The put method checks for existing IDs, preventing duplicates (e.g., adding “V1” twice fails with an error).



Updates: Updating a vehicle’s location or destination modifies the Vehicle object in the hash table, ensuring consistency (fixed from earlier issues).



Efficiency:





Insertion/Deletion/Search: O(1) average, O(n) worst case (many collisions).



Resizing: O(n) when triggered.



Why Used: Hash tables provide fast access to vehicle data by ID, essential for real-time management in a fleet system.

3. Heap (Sorting for Recommendations)





Concept: A heap is a tree-based data structure (typically a binary tree) where each parent node has a priority (e.g., smaller value in a min-heap) compared to its children. It’s used for priority queues and efficient sorting (Heapsort).



Implementation: The DSAHeap class implements a min-heap as an array, where the parent at index i has children at 2i+1 and 2i+2. The add method inserts an element and “trickles up” to maintain the heap property, while remove extracts the root and “trickles down.” Heapsort uses this heap to sort vehicles by distance.



Application in AVMS:





Heapsort for Distance: The heap_sort_vehicles_by_distance function builds a min-heap with vehicle distances as priorities, extracting the smallest distance repeatedly to sort in ascending order. The find_nearest_vehicle method returns the first vehicle (closest to destination).



Recommendation: For a vehicle list [V1: 10km, V2: 5km], Heapsort outputs [V2, V1], and find_nearest_vehicle selects V2.



Efficiency:





Heapsort: O(n log n) for building and extracting.



Add/Remove: O(log n).



Why Used: Heapsort ensures efficient sorting for recommendations, and the heap’s priority queue nature suits dynamic updates (though not used here).

Additional Algorithm: Quicksort





Concept: Quicksort is a divide-and-conquer sorting algorithm that partitions an array around a pivot, recursively sorting sub-arrays. It’s used in AVMS to sort vehicles by battery level in descending order.



Implementation: The quick_sort_vehicles_by_battery function uses the last element as the pivot, partitioning vehicles so higher battery levels are on the left. The find_vehicle_with_highest_battery method returns the first vehicle after sorting.



Application: For [V1: 80%, V2: 90%], Quicksort outputs [V2, V1], selecting V2 as the highest battery.



Efficiency: O(n log n) average, O(n²) worst case (rare with random data).



Why Used: Quicksort complements Heapsort, providing an alternative sorting method as required by the assignment.

How to Run





Prerequisites:





Python 3.8+ (python3 --version to check).



No external libraries required, as per assignment rules.



Clone the Repository:

git clone https://github.com/mashodist/avms-project.git
cd avms_project





Requires access (private repository). Contact me for permissions.



Run the Program:

python3 avms_menu.py



Use the Menu:





Road Network: Add locations (e.g., “Downtown”), roads (e.g., Downtown to Airport, 10km), display network, or check paths.



Vehicles: Add vehicles (e.g., ID “V1”, location “Downtown”, destination “Airport”, battery 80%, distance 10km), update location/destination, view all, or remove.



Recommendations: Find the nearest vehicle or highest battery vehicle.

Project Structure





avms_menu.py: Interactive menu and main program logic for user interaction.



avms_main.py: Core classes (DSAGraph, VehicleHashTable, Vehicle, DSAHeap) and sorting algorithms (Heapsort, Quicksort).



.gitignore: Excludes Python cache files (*.pyc, __pycache__/).



README.md: This file, detailing the project and data structures.



report.pdf (submission only): Technical report with implementation strategy and UML diagram.



test_cases.pdf (submission only): Test cases for all components.

Implementation Details





Graph: Uses adjacency lists for efficient neighbor retrieval (O(1) per neighbor). DFS ensures path checks handle disconnected graphs.



Hash Table: Linear probing resolves collisions, with a custom hash function (ASCII sum modulo table size). Resizing prevents performance degradation.



Heap: Min-heap array implementation for Heapsort, avoiding Python’s heapq.



Quicksort: In-place partitioning with descending order for battery levels.



Error Handling: Validates inputs (e.g., non-empty IDs, positive distances, existing locations). Fixed issues with duplicate IDs and inconsistent updates by using a single VehicleHashTable for storage.



Challenges Overcome:





Prevented duplicate vehicles by enhancing hash table checks.



Ensured update consistency by removing a redundant vehicle list.

Efficiency Analysis





Graph: DFS path check is O(V + E), suitable for sparse road networks.



Hash Table: O(1) average case for vehicle operations, O(n) worst case with many collisions (mitigated by resizing).



Heapsort: O(n log n), optimal for sorting small to medium vehicle lists.



Quicksort: O(n log n) average, with pivot choice minimizing worst-case scenarios.



Potential Improvements:





Implement Dijkstra’s algorithm for shortest path routing (O((V + E) log V) with a priority queue).



Use quadratic probing to reduce clustering in the hash table.



Parallelize sorting for large vehicle fleets.

Future Improvements





Routing: Add shortest path calculations using Dijkstra’s or A* algorithms to optimize vehicle navigation.



Persistence: Implement file I/O to save/load road networks and vehicle data for scalability.



UI: Develop a graphical interface using Tkinter or Flask for enhanced user experience.



Real-Time Updates: Simulate vehicle movement with periodic location updates based on road distances.


License

This project is for academic purposes and not licensed for public use. 
