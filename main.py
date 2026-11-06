
from algorithms.sorting import load_parcels, merge_sort, quick_sort, display_parcels
from algorithms.knapsack import knapsack, display_dp_table, display_selected_parcels
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import create_distance_matrix, tsp
from utils.graph import create_graph
from pathlib import Path
import csv

PROJECT_DIR = Path(__file__).resolve().parent
RUNTIME_FILE = PROJECT_DIR / "results" / "runtime.csv"

def show_parcels():
    parcels = load_parcels()
    print("\n========== ALL PARCELS ==========")
    display_parcels(parcels)

def run_merge_sort():
    parcels = load_parcels()
    sorted_parcels = merge_sort(parcels)
    print("\n========== MERGE SORT ==========")
    display_parcels(sorted_parcels)

def run_quick_sort():
    parcels = load_parcels()
    sorted_parcels = quick_sort(parcels)
    print("\n========== QUICK SORT ==========")
    display_parcels(sorted_parcels)

def run_knapsack():
    parcels = load_parcels()
    capacity = 10

    maximum_value, selected, dp = knapsack(parcels, capacity)

    display_dp_table(dp, parcels, capacity)
    display_selected_parcels(selected, maximum_value, capacity)

def run_dijkstra():
    graph = create_graph()
    start = "Delhi"

    distances, previous = dijkstra(graph, start)

    print("\n========== SHORTEST DELIVERY ROUTES ==========")
    print("Starting Location:", start)

    for city in graph:
        path = get_path(previous, city)
        print(f"\nDestination: {city}")
        print("Route:", " -> ".join(path))
        print("Distance:", distances[city], "km")

def run_tsp():
    cities, graph = create_distance_matrix()
    start = "Delhi"

    route, distance = tsp(cities, graph, start)

    print("\n========== OPTIMAL DELIVERY TOUR ==========")
    print("Starting Location:", start)
    print("Optimal Route:", " -> ".join(route))
    print("Minimum Total Distance:", distance, "km")

def show_performance():
    print("\n========== PERFORMANCE ANALYSIS ==========")

    if not RUNTIME_FILE.exists():
        print("Performance results not found. Run utils.performance first.")
        return

    with open(RUNTIME_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))

def main():
    while True:
        print("\n========================================")
        print("       MINI-COURIER PLANNER")
        print("========================================")
        print("1. Display All Parcels")
        print("2. Sort Parcels using Merge Sort")
        print("3. Sort Parcels using Quick Sort")
        print("4. Optimize Parcel Loading (Knapsack)")
        print("5. Find Shortest Delivery Routes (Dijkstra)")
        print("6. Find Optimal Delivery Tour (TSP)")
        print("7. View Performance Analysis")
        print("8. Exit")
        print("========================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            show_parcels()
        elif choice == "2":
            run_merge_sort()
        elif choice == "3":
            run_quick_sort()
        elif choice == "4":
            run_knapsack()
        elif choice == "5":
            run_dijkstra()
        elif choice == "6":
            run_tsp()
        elif choice == "7":
            show_performance()
        elif choice == "8":
            print("\nThank you for using Mini-Courier Planner!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
