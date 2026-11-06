
import csv
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "results" / "sorting_comparison.csv"

sizes = []
merge_times = []
quick_times = []

with open(CSV_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sizes.append(int(row["Input Size"]))
        merge_times.append(float(row["Merge Sort (ms)"]))
        quick_times.append(float(row["Quick Sort (ms)"]))

plt.figure(figsize=(9, 6))

plt.plot(sizes, merge_times, marker="o", label="Merge Sort")
plt.plot(sizes, quick_times, marker="s", label="Quick Sort")

plt.title("Merge Sort vs Quick Sort Performance")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()

CHART_DIR = PROJECT_DIR / "results" / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

chart_path = CHART_DIR / "sorting_comparison.png"

plt.savefig(chart_path, dpi=300)
plt.show()

print("Sorting comparison graph saved at:", chart_path)
