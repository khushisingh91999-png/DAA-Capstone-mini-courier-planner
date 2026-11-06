
import csv
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "results" / "runtime.csv"

algorithms = []
execution_times = []

with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        algorithms.append(row["Algorithm"])
        execution_times.append(float(row["Execution Time (ms)"]))

plt.figure(figsize=(10, 6))
plt.bar(algorithms, execution_times)

plt.title("Algorithm Execution Time Comparison")
plt.xlabel("Algorithms")
plt.ylabel("Execution Time (milliseconds)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

chart_folder = PROJECT_DIR / "results" / "charts"
chart_folder.mkdir(parents=True, exist_ok=True)

chart_path = chart_folder / "performance_comparison.png"
plt.savefig(chart_path, dpi=300)
plt.show()

print("Performance chart saved at:", chart_path)
