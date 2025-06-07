from avms_main import DSAGraph, VehicleHashTable, Vehicle, heap_sort_vehicles_by_distance, find_nearest_vehicle, quick_sort_vehicles_by_battery, find_vehicle_with_highest_battery

class AVMSMenu:
    def __init__(self):
        self.road_network = DSAGraph()
        self.vehicle_table = VehicleHashTable()
        
    def run(self):
        while True:
            print("\nAutonomous Vehicle Management System")
            print("1. Manage Road Network")
            print("2. Manage Vehicles")
            print("3. Vehicle Recommendations")
            print("4. Exit")
            
            choice = input("Enter choice (1-4): ").strip()
            
            if choice == "1":
                self.manage_road_network()
            elif choice == "2":
                self.manage_vehicles()
            elif choice == "3":
                self.vehicle_recommendations()
            elif choice == "4":
                print("Exiting AVMS. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    
    def manage_road_network(self):
        while True:
            print("\nRoad Network Management")
            print("1. Add Location")
            print("2. Add Road")
            print("3. Display Network")
            print("4. Check Path")
            print("5. Back to Main Menu")
            
            choice = input("Enter choice (1-5): ").strip()
            
            if choice == "1":
                location = input("Enter location name: ").strip()
                if not location:
                    print("Error: Location name cannot be empty.")
                elif location in self.road_network.nodes:
                    print(f"Error: Location {location} already exists.")
                else:
                    self.road_network.add_node(location)
                    print(f"Location {location} added successfully.")
            elif choice == "2":
                loc1 = input("Enter first location: ").strip()
                loc2 = input("Enter second location: ").strip()
                if loc1 not in self.road_network.nodes:
                    print(f"Error: Location {loc1} does not exist.")
                    continue
                if loc2 not in self.road_network.nodes:
                    print(f"Error: Location {loc2} does not exist.")
                    continue
                if loc1 == loc2:
                    print("Error: Locations must be different.")
                    continue
                try:
                    distance = int(input("Enter distance between them (km): "))
                    if distance <= 0:
                        print("Error: Distance must be a positive integer.")
                        continue
                    self.road_network.add_edge(loc1, loc2, distance)
                    print(f"Road between {loc1} and {loc2} added with distance {distance}km.")
                except ValueError:
                    print("Error: Distance must be a valid integer.")
            elif choice == "3":
                if not self.road_network.nodes:
                    print("Error: Road network is empty.")
                else:
                    self.road_network.display()
            elif choice == "4":
                loc1 = input("Enter source location: ").strip()
                loc2 = input("Enter destination location: ").strip()
                if loc1 not in self.road_network.nodes:
                    print(f"Error: Location {loc1} does not exist.")
                    continue
                if loc2 not in self.road_network.nodes:
                    print(f"Error: Location {loc2} does not exist.")
                    continue
                if self.road_network.is_path(loc1, loc2):
                    print(f"Path exists between {loc1} and {loc2}.")
                else:
                    print(f"No path exists between {loc1} and {loc2}.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    
    def manage_vehicles(self):
        while True:
            print("\nVehicle Management")
            print("1. Add Vehicle")
            print("2. Update Vehicle Location")
            print("3. Update Vehicle Destination")
            print("4. View All Vehicles")
            print("5. Remove Vehicle")
            print("6. Back to Main Menu")
            
            choice = input("Enter choice (1-6): ").strip()
            
            if choice == "1":
                self.add_vehicle()
            elif choice == "2":
                self.update_vehicle_location()
            elif choice == "3":
                self.update_vehicle_destination()
            elif choice == "4":
                self.view_all_vehicles()
            elif choice == "5":
                self.remove_vehicle()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    
    def add_vehicle(self):
        vid = input("Enter vehicle ID: ").strip()
        if not vid:
            print("Error: Vehicle ID cannot be empty.")
            return
            
        if self.vehicle_table.get(vid):
            print(f"Error: Vehicle {vid} already exists.")
            return
            
        location = input("Enter current location: ").strip()
        if not location:
            print("Error: Location cannot be empty.")
            return
        if location not in self.road_network.nodes:
            print(f"Error: Location {location} does not exist in road network.")
            return
            
        destination = input("Enter destination: ").strip()
        if not destination:
            print("Error: Destination cannot be empty.")
            return
        if destination not in self.road_network.nodes:
            print(f"Error: Destination {destination} does not exist in road network.")
            return
            
        try:
            battery = int(input("Enter battery level (0-100): "))
            if not 0 <= battery <= 100:
                print("Error: Battery level must be between 0 and 100.")
                return
                
            vehicle = Vehicle(vid, location, destination, battery)
            try:
                distance = int(input(f"Enter distance from {location} to {destination} (km): "))
                if distance <= 0:
                    print("Error: Distance must be a positive integer.")
                    return
                vehicle.set_distance_to_destination(distance)
            except ValueError:
                print("Error: Distance must be a valid integer.")
                return
                
            self.vehicle_table.put(vid, vehicle)
            print(f"Vehicle {vid} added successfully.")
        except ValueError:
            print("Error: Battery level must be a valid integer.")
    
    def update_vehicle_location(self):
        vid = input("Enter vehicle ID: ").strip()
        if not vid:
            print("Error: Vehicle ID cannot be empty.")
            return
        vehicle = self.vehicle_table.get(vid)
        if not vehicle:
            print(f"Error: Vehicle {vid} not found.")
            return
            
        new_loc = input("Enter new location: ").strip()
        if not new_loc:
            print("Error: Location cannot be empty.")
            return
        if new_loc not in self.road_network.nodes:
            print(f"Error: Location {new_loc} does not exist in road network.")
            return
            
        vehicle.set_location(new_loc)
        try:
            dist = int(input(f"Enter distance from {new_loc} to {vehicle.get_destination()} (km): "))
            if dist <= 0:
                print("Error: Distance must be a positive integer.")
                return
            vehicle.set_distance_to_destination(dist)
            print(f"Updated location for {vid} to {new_loc} with distance {dist}km.")
        except ValueError:
            print("Error: Distance must be a valid integer.")
    
    def update_vehicle_destination(self):
        vid = input("Enter vehicle ID: ").strip()
        if not vid:
            print("Error: Vehicle ID cannot be empty.")
            return
        vehicle = self.vehicle_table.get(vid)
        if not vehicle:
            print(f"Error: Vehicle {vid} not found.")
            return
            
        new_dest = input("Enter new destination: ").strip()
        if not new_dest:
            print("Error: Destination cannot be empty.")
            return
        if new_dest not in self.road_network.nodes:
            print(f"Error: Destination {new_dest} does not exist in road network.")
            return
            
        vehicle.set_destination(new_dest)
        try:
            dist = int(input(f"Enter distance from {vehicle.get_location()} to {new_dest} (km): "))
            if dist <= 0:
                print("Error: Distance must be a positive integer.")
                return
            vehicle.set_distance_to_destination(dist)
            print(f"Updated destination for {vid} to {new_dest} with distance {dist}km.")
        except ValueError:
            print("Error: Distance must be a valid integer.")
    
    def view_all_vehicles(self):
        if self.vehicle_table.count == 0:
            print("No vehicles in system.")
            return
        print("\nAll Vehicles:")
        self.vehicle_table.display_all()
    
    def remove_vehicle(self):
        vid = input("Enter vehicle ID to remove: ").strip()
        if not vid:
            print("Error: Vehicle ID cannot be empty.")
            return
            
        if self.vehicle_table.remove(vid):
            print(f"Vehicle {vid} removed successfully.")
        else:
            print(f"Error: Vehicle {vid} not found.")
    
    def vehicle_recommendations(self):
        if self.vehicle_table.count == 0:
            print("No vehicles in system.")
            return
            
        vehicles = [entry.value for entry in self.vehicle_table.table if entry.state == 1]
        
        while True:
            print("\nVehicle Recommendations")
            print("1. Find Nearest Vehicle to Destination")
            print("2. Find Vehicle with Highest Battery")
            print("3. Back to Main Menu")
            
            choice = input("Enter choice (1-3): ").strip()
            
            if choice == "1":
                nearest = find_nearest_vehicle(vehicles)
                if nearest:
                    print(f"\nNearest vehicle to its destination:\n{nearest}")
                else:
                    print("No vehicles available.")
            elif choice == "2":
                highest_bat = find_vehicle_with_highest_battery(vehicles)
                if highest_bat:
                    print(f"\nVehicle with highest battery:\n{highest_bat}")
                else:
                    print("No vehicles available.")
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    menu = AVMSMenu()
    menu.run()