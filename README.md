# 🚚 Mini-Courier Planner

A Python-based **Design and Analysis of Algorithms (DAA) Capstone Project** that helps optimize parcel delivery operations using sorting, dynamic programming, and graph algorithms.

The project simulates a courier delivery system where parcels are prioritized, loading capacity is optimized, and efficient delivery routes are calculated.

## 📌 Project Overview

Mini-Courier Planner is designed to solve common courier management problems using fundamental algorithms.

It provides features such as:
- Displaying parcel information.
- Sorting parcels based on priority and delivery deadlines.
- Selecting valuable parcels within a limited vehicle capacity.
- Finding the shortest delivery route between cities.
- Calculating an optimal delivery tour.
- Comparing algorithm performance through execution-time analysis and graphs.

## 🎯 Project Objectives

- Apply DAA concepts to a real-world delivery problem.
- Understand and implement different algorithmic techniques.
- Optimize parcel selection based on vehicle capacity.
- Minimize delivery distances using graph algorithms.
- Analyze and compare algorithm execution times.
- Perform automated testing to verify correctness.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Concepts:** Data Structures and Algorithms
- **Libraries:** Matplotlib, JSON, CSV, unittest
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## 🧠 Algorithms Implemented

### 1. Merge Sort

Used to sort parcels based on priority and delivery deadline.

- Technique: Divide and Conquer
- Time Complexity: O(n log n)
- Space Complexity: O(n)

### 2. Quick Sort

Used to arrange parcels based on priority and delivery deadline using a pivot-based partitioning technique.

- Technique: Divide and Conquer
- Average Time Complexity: O(n log n)
- Worst-case Time Complexity: O(n²)

### 3. 0/1 Knapsack

Used to select the most valuable parcels without exceeding the vehicle's maximum carrying capacity.

- Technique: Dynamic Programming
- Time Complexity: O(nW)
- Space Complexity: O(nW)

### 4. Dijkstra's Algorithm

Used to calculate the shortest delivery distances from a starting city to other cities.

- Technique: Greedy Algorithm
- Time Complexity: O((V + E) log V), using an adjacency list and binary heap.

### 5. Travelling Salesman Problem (TSP)

Used to calculate an optimal delivery tour that visits every city and returns to the starting location.

- Technique: Dynamic Programming with Bitmasking
- Time Complexity: O(n² × 2ⁿ)
- Space Complexity: O(n × 2ⁿ)

## ✨ Key Features

- Interactive command-line menu.
- Parcel sorting using Merge Sort and Quick Sort.
- Optimal parcel selection using Knapsack.
- Shortest-path calculation using Dijkstra's Algorithm.
- Optimal delivery tour using TSP.
- Performance comparison of algorithms.
- Graph generation using Matplotlib.
- Automated unit testing.
- JSON-based parcel and distance data.

## 📂 Project Structure

```text
DAA-Capstone-mini-courier-planner/
│
├── algorithms/
│   ├── __init__.py
│   ├── sorting.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
│
├── data/
│   ├── parcels.json
│   └── distances.json
│
├── utils/
│   ├── __init__.py
│   ├── graph.py
│   ├── performance.py
│   ├── performance_chart.py
│   ├── sorting_performance.py
│   └── sorting_chart.py
│
├── tests/
│   ├── __init__.py
│   └── test_cases.py
│
├── results/
│   ├── runtime.csv
│   ├── sorting_comparison.csv
│   └── charts/
│       ├── performance_comparison.png
│       └── sorting_comparison.png
│
├── screenshots/
│
├── main.py
├── README.md
└── requirements.txt
```


## 📊 Sample Results

### 1. Knapsack Algorithm

Vehicle Capacity: 10 kg

Selected Parcels:

| Parcel | Weight | Value |
|---|---:|---:|
| P2 | 4 kg | ₹200 |
| P3 | 3 kg | ₹150 |
| P4 | 2 kg | ₹180 |
| **Total** | **9 kg** | **₹530** |

Maximum Value: ₹530

Remaining Capacity: 1 kg

### 2. Dijkstra's Algorithm

Starting Location: Delhi

| Destination | Shortest Distance |
|---|---:|
| Delhi | 0 km |
| Gurgaon | 30 km |
| Noida | 25 km |
| Faridabad | 65 km |
| Sohna | 70 km |

Example Route:

Delhi → Gurgaon → Faridabad

Total Distance: 65 km

### 3. Travelling Salesman Problem

Optimal Delivery Tour:

Delhi → Gurgaon → Sohna → Faridabad → Noida → Delhi

Minimum Total Distance: **160 km**

## ⏱️ Performance Analysis

The project measures algorithm execution time and stores the results in CSV files.

### Overall Algorithm Execution Time

| Algorithm | Execution Time |
|---|---:|
| Sorting (Merge Sort + Quick Sort) | 143.4381 ms |
| 0/1 Knapsack | 142.0084 ms |
| Dijkstra | 185.4385 ms |
| TSP | 156.3588 ms |

*Note: These measurements include Python process startup and module import overhead. They are not pure algorithm execution times.*

### Merge Sort vs Quick Sort

The following results were obtained during testing:

| Input Size | Merge Sort | Quick Sort |
|---:|---:|---:|
| 100 | 0.221 ms | 0.104 ms |
| 500 | 1.3722 ms | 0.5149 ms |
| 1000 | 2.4021 ms | 1.1763 ms |
| 5000 | 21.5738 ms | 8.7714 ms |

Quick Sort was faster in these particular test runs. Actual performance may vary depending on input data and execution conditions.

### Performance Graphs

The project generates two performance graphs:

- `results/charts/performance_comparison.png`
- `results/charts/sorting_comparison.png`

## 🧪 Testing

Automated testing is implemented using Python's `unittest` framework.

The project includes five test cases:

1. Merge Sort
2. Quick Sort
3. Knapsack Algorithm
4. Dijkstra's Algorithm
5. Travelling Salesman Problem

Run the following command to execute the tests:

```bash
python -m unittest tests.test_cases -v
```

**Test Result:** All 5 test cases passed successfully.

## 🚀 Future Scope

- Develop a graphical user interface.
- Integrate real-time GPS tracking.
- Add more delivery locations and parcel records.
- Include vehicle fuel and delivery cost optimization.
- Implement real-world traffic-based route planning.
- Extend the system to support multiple delivery vehicles.

## 👩‍💻 Author

**Khushi Singh**

B.Tech – Computer Science and Engineering

GitHub: [khushisingh91999-png](https://github.com/khushisingh91999-png)

---