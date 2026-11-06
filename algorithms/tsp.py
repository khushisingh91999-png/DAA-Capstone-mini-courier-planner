
import json
from pathlib import Path
from functools import lru_cache

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "distances.json"

def load_distances():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def create_distance_matrix():
    distances = load_distances()
    cities = sorted(set(
        [item["from"] for item in distances] +
        [item["to"] for item in distances]
    ))

    graph = {city: {} for city in cities}

    for item in distances:
        source = item["from"]
        destination = item["to"]
        distance = item["distance"]

        graph[source][destination] = distance
        graph[destination][source] = distance

    return cities, graph

def tsp(cities, graph, start):
    n = len(cities)
    start_index = cities.index(start)

    @lru_cache(None)
    def solve(current, visited):
        if visited == (1 << n) - 1:
            return graph[cities[current]].get(start, float("inf"))

        minimum_cost = float("inf")

        for next_city in range(n):
            if not (visited & (1 << next_city)):
                city_name = cities[next_city]
                distance = graph[cities[current]].get(
                    city_name, float("inf")
                )

                cost = distance + solve(
                    next_city,
                    visited | (1 << next_city)
                )

                minimum_cost = min(minimum_cost, cost)

        return minimum_cost

    @lru_cache(None)
    def get_route(current, visited):
        if visited == (1 << n) - 1:
            return [start] if start in graph[cities[current]] else []

        best_route = []
        best_cost = float("inf")

        for next_city in range(n):
            if not (visited & (1 << next_city)):
                city_name = cities[next_city]
                distance = graph[cities[current]].get(
                    city_name, float("inf")
                )

                cost = distance + solve(
                    next_city,
                    visited | (1 << next_city)
                )

                if cost < best_cost:
                    best_cost = cost
                    best_route = [city_name] + get_route(
                        next_city,
                        visited | (1 << next_city)
                    )

        return best_route

    initial_visited = 1 << start_index
    minimum_distance = solve(start_index, initial_visited)
    route = [start] + get_route(start_index, initial_visited)

    return route, minimum_distance

if __name__ == "__main__":
    cities, graph = create_distance_matrix()
    starting_city = "Delhi"

    route, distance = tsp(cities, graph, starting_city)

    print("\n========== TSP OPTIMAL ROUTE ==========")
    print("Starting Location:", starting_city)
    print("Optimal Route:", " -> ".join(route))
    print("Minimum Total Distance:", distance, "km")
