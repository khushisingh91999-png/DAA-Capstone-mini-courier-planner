
import time
import random
import csv
from pathlib import Path
from algorithms.sorting import merge_sort, quick_sort

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULT_FILE = PROJECT_DIR / "results" / "sorting_comparison.csv"

def generate_parcels(size):
    parcels = []

    for i in range(size):
        parcels.append({
            "id": f"P{i}",
            "destination": f"City{i}",
            "weight": random.randint(1, 10),
            "deadline": random.randint(1, 10),
            "priority": random.randint(1, 5),
            "value": random.randint(100, 1000)
        })

    return parcels

def measure_time(sort_function, data):
    start = time.perf_counter()
    sort_function(data)
    end = time.perf_counter()

    return round((end - start) * 1000, 4)

def run_comparison():
    sizes = [100, 500, 1000, 5000]
    results = []

    print("\n========== SORTING PERFORMANCE COMPARISON ==========")

    for size in sizes:
        parcels = generate_parcels(size)

        merge_time = measure_time(merge_sort, parcels)
        quick_time = measure_time(quick_sort, parcels)

        print(f"\nInput Size: {size}")
        print(f"Merge Sort: {merge_time} ms")
        print(f"Quick Sort: {quick_time} ms")

        results.append([size, merge_time, quick_time])

    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(RESULT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input Size",
            "Merge Sort (ms)",
            "Quick Sort (ms)"
        ])
        writer.writerows(results)

    print("\nResults saved successfully!")
    print("File location:", RESULT_FILE)

if __name__ == "__main__":
    run_comparison()
