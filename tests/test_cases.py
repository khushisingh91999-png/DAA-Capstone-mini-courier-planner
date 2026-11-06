
import unittest

from algorithms.sorting import merge_sort, quick_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import create_distance_matrix, tsp
from utils.graph import create_graph


class TestMiniCourierPlanner(unittest.TestCase):

    # Sample parcel data for sorting tests
    def setUp(self):
        self.parcels = [
            {"id": "P1", "destination": "Delhi", "weight": 2,
             "deadline": 2, "priority": 3, "value": 100},
            {"id": "P2", "destination": "Gurgaon", "weight": 4,
             "deadline": 1, "priority": 1, "value": 200},
            {"id": "P3", "destination": "Noida", "weight": 3,
             "deadline": 3, "priority": 2, "value": 150},
            {"id": "P4", "destination": "Faridabad", "weight": 2,
             "deadline": 1, "priority": 1, "value": 180},
            {"id": "P5", "destination": "Sohna", "weight": 5,
             "deadline": 4, "priority": 3, "value": 120}
        ]

    # Test Merge Sort
    def test_merge_sort(self):
        result = merge_sort(self.parcels)
        keys = [(p["priority"], p["deadline"]) for p in result]

        self.assertEqual(keys, sorted(keys))

    # Test Quick Sort
    def test_quick_sort(self):
        result = quick_sort(self.parcels)
        keys = [(p["priority"], p["deadline"]) for p in result]

        self.assertEqual(keys, sorted(keys))

    # Test 0/1 Knapsack
    def test_knapsack(self):
        maximum_value, selected, dp = knapsack(self.parcels, 10)

        total_weight = sum(p["weight"] for p in selected)

        self.assertEqual(maximum_value, 530)
        self.assertLessEqual(total_weight, 10)

    # Test Dijkstra's Shortest Path
    def test_dijkstra(self):
        graph = create_graph()
        distances, previous = dijkstra(graph, "Delhi")

        self.assertEqual(distances["Delhi"], 0)
        self.assertEqual(distances["Gurgaon"], 30)
        self.assertEqual(distances["Noida"], 25)
        self.assertEqual(distances["Faridabad"], 65)
        self.assertEqual(distances["Sohna"], 70)

        self.assertEqual(
            get_path(previous, "Faridabad"),
            ["Delhi", "Gurgaon", "Faridabad"]
        )

    # Test Travelling Salesperson Problem
    def test_tsp(self):
        cities, graph = create_distance_matrix()
        route, distance = tsp(cities, graph, "Delhi")

        self.assertEqual(distance, 160)
        self.assertEqual(route[0], "Delhi")
        self.assertEqual(route[-1], "Delhi")
        self.assertEqual(set(route[:-1]), set(cities))
        self.assertEqual(len(route), len(cities) + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
