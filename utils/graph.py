
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "distances.json"


def create_graph():

    graph = {}

    with open(DATA_FILE, "r") as file:
        distances = json.load(file)

    for item in distances:

        source = item["from"]
        destination = item["to"]
        distance = item["distance"]

        # Create vertices if they do not exist
        if source not in graph:
            graph[source] = {}

        if destination not in graph:
            graph[destination] = {}

        # Add undirected edges
        graph[source][destination] = distance
        graph[destination][source] = distance

    return graph


def display_graph(graph):

    print("\n========== COURIER DELIVERY GRAPH ==========")

    for location, neighbours in graph.items():

        print(f"\n{location}:")

        for destination, distance in neighbours.items():

            print(f"  -> {destination}: {distance} km")


if __name__ == "__main__":

    delivery_graph = create_graph()

    display_graph(delivery_graph)
