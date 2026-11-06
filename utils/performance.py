
import csv
import subprocess
import sys
import time
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RESULT_FILE = PROJECT_DIR / "results" / "runtime.csv"

algorithms = [
    ("Sorting (Merge Sort + Quick Sort)", "algorithms.sorting"),
    ("0/1 Knapsack", "algorithms.knapsack"),
    ("Dijkstra", "algorithms.dijkstra"),
    ("TSP", "algorithms.tsp")
]

def measure_execution_time(module_name):
    start_time = time.perf_counter()

    result = subprocess.run(
        [sys.executable, "-m", module_name],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    end_time = time.perf_counter()

    if result.returncode != 0:
        print("Error running:", module_name)
        print(result.stderr)
        return None

    return round((end_time - start_time) * 1000, 4)

def save_results():
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)

    results = []

    print("\n========== ALGORITHM PERFORMANCE ANALYSIS ==========")

    for name, module in algorithms:
        execution_time = measure_execution_time(module)

        if execution_time is not None:
            print(f"{name}: {execution_time} ms")
            results.append([name, execution_time])

    with open(RESULT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Algorithm", "Execution Time (ms)"])
        writer.writerows(results)

    print("\nResults saved successfully!")
    print("File location:", RESULT_FILE)

if __name__ == "__main__":
    save_results()
