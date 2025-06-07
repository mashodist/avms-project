class DSAGraphNode:
    def __init__(self, label):
        self.label = label
        self.adjacent = []
        self.visited = False
        self.distance = {}  # Stores distances to neighbors

    def add_edge(self, node, distance):
        if node not in self.adjacent:
            self.adjacent.append(node)
            self.distance[node.label] = distance
            node.adjacent.append(self)
            node.distance[self.label] = distance

    def __str__(self):
        return self.label

class DSAGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = DSAGraphNode(label)
            return True
        return False

    def add_edge(self, label1, label2, distance):
        if label1 in self.nodes and label2 in self.nodes:
            self.nodes[label1].add_edge(self.nodes[label2], distance)
            return True
        return False

    def get_neighbors(self, label):
        if label in self.nodes:
            return [(node.label, self.nodes[label].distance[node.label]) 
                    for node in self.nodes[label].adjacent]
        return []

    def display(self):
        if not self.nodes:
            print("Road Network is empty.")
            return
        print("Road Network Graph:")
        for label in sorted(self.nodes.keys()):
            neighbors = self.get_neighbors(label)
            if neighbors:
                print(f"{label}: {neighbors}")
            else:
                print(f"{label}: No connections")

    def is_path(self, source, destination):
        if source == destination:
            return True
            
        if source not in self.nodes or destination not in self.nodes:
            return False
            
        self._reset_visited()
        stack = [self.nodes[source]]
        self.nodes[source].visited = True
        
        while stack:
            current = stack.pop()
            if current.label == destination:
                return True
            for neighbor in current.adjacent:
                if not neighbor.visited:
                    neighbor.visited = True
                    stack.append(neighbor)
        return False

    def _reset_visited(self):
        for node in self.nodes.values():
            node.visited = False

class DSAHashEntry:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.state = 0  # 0: free, 1: used, 2: previously used

class VehicleHashTable:
    def __init__(self, size=100):
        self.table = [DSAHashEntry() for _ in range(size)]
        self.count = 0
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        return sum(ord(char) for char in str(key)) % len(self.table)

    def _probe(self, key, index):
        original_index = index
        while True:
            if self.table[index].state == 0 or (self.table[index].state == 2 and self.table[index].key != key):
                return index
            if self.table[index].state == 1 and self.table[index].key == key:
                return index
            index = (index + 1) % len(self.table)
            if index == original_index:
                raise RuntimeError("Hash table is full")

    def _resize(self, new_size):
        old_table = self.table
        self.table = [DSAHashEntry() for _ in range(new_size)]
        self.count = 0
        for entry in old_table:
            if entry.state == 1:
                self.put(entry.key, entry.value)

    def put(self, key, value):
        if self.count / len(self.table) > self.load_factor_threshold:
            self._resize(len(self.table) * 2)

        index = self._hash(key)
        index = self._probe(key, index)

        if self.table[index].state == 1 and self.table[index].key == key:
            return False  # Prevent duplicates

        if self.table[index].state != 1:
            self.count += 1

        self.table[index] = DSAHashEntry(key, value)
        self.table[index].state = 1
        return True

    def get(self, key):
        index = self._hash(key)
        index = self._probe(key, index)

        if self.table[index].state == 1 and self.table[index].key == key:
            return self.table[index].value
        return None

    def remove(self, key):
        index = self._hash(key)
        index = self._probe(key, index)

        if self.table[index].state == 1 and self.table[index].key == key:
            self.table[index].state = 2
            self.count -= 1
            return True
        return False

    def display_all(self):
        if self.count == 0:
            print("Hash table is empty.")
            return
        print("Vehicle Hash Table Contents:")
        for i, entry in enumerate(self.table):
            if entry.state == 1:
                print(f"Index {i}: {entry.key} => {entry.value}")

class Vehicle:
    def __init__(self, vehicle_id, location=None, destination=None, battery_level=100):
        self.vehicle_id = vehicle_id
        self._location = location
        self._destination = destination
        self._distance_to_destination = 0
        self._battery_level = battery_level

    def set_location(self, location):
        self._location = location

    def set_destination(self, destination):
        self._destination = destination

    def set_distance_to_destination(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        self._distance_to_destination = distance

    def set_battery_level(self, level):
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            raise ValueError("Battery level must be between 0 and 100")

    def get_location(self):
        return self._location

    def get_destination(self):
        return self._destination

    def get_distance_to_destination(self):
        return self._distance_to_destination

    def get_battery_level(self):
        return self._battery_level

    def __str__(self):
        return (f"Vehicle {self.vehicle_id}: Location={self._location}, "
                f"Destination={self._destination}, Distance={self._distance_to_destination}km, "
                f"Battery={self._battery_level}%")

class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

class DSAHeap:
    def __init__(self, max_size=100):
        self.heap = []
        self.count = 0
        self.max_size = max_size

    def add(self, priority, value):
        if self.count >= self.max_size:
            raise OverflowError("Heap is full")
        entry = DSAHashEntry(priority, value)
        self.heap.append(entry)
        self.count += 1
        self._trickle_up(self.count - 1)

    def remove(self):
        if self.count == 0:
            raise IndexError("Heap is empty")
        root = self.heap[0]
        self.heap[0] = self.heap[self.count - 1]
        self.heap.pop()
        self.count -= 1
        self._trickle_down(0)
        return root

    def _trickle_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index].priority < self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _trickle_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < self.count and self.heap[left].priority < self.heap[smallest].priority:
                smallest = left
            if right < self.count and self.heap[right].priority < self.heap[smallest].priority:
                smallest = right

            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

def heap_sort_vehicles_by_distance(vehicles):
    heap = DSAHeap(len(vehicles))
    for vehicle in vehicles:
        heap.add(vehicle.get_distance_to_destination(), vehicle)
    
    sorted_vehicles = []
    while heap.count > 0:
        sorted_vehicles.append(heap.remove().value)
    return sorted_vehicles

def find_nearest_vehicle(vehicles):
    if not vehicles:
        return None
    return heap_sort_vehicles_by_distance(vehicles)[0]

def partition(arr, low, high):
    pivot = arr[high].get_battery_level()
    i = low - 1
    for j in range(low, high):
        if arr[j].get_battery_level() >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_vehicles_by_battery(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_vehicles_by_battery(arr, low, pi - 1)
        quick_sort_vehicles_by_battery(arr, pi + 1, high)

def find_vehicle_with_highest_battery(vehicles):
    if not vehicles:
        return None
    arr = vehicles.copy()  # Create a copy to avoid modifying original list
    quick_sort_vehicles_by_battery(arr, 0, len(arr) - 1)
    return arr[0]