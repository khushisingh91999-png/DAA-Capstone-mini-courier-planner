
import heapq

from utils.graph import create_graph


def dijkstra(graph, start):

    # Initialize all distances as infinity
    distances = {
        node: float("inf")
        for node in graph
    }

    # Starting location distance is zero
    distances[start] = 0

    # Store previous nodes for path reconstruction
    previous = {
        node: None
        for node in graph
    }

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        # Ignore outdated entries
        if current_distance > distances[current_node]:
            continue

        # Visit neighbouring locations
        for neighbour, weight in graph[current_node].items():

            new_distance = current_distance + weight

            # Update if a shorter path is found
            if new_distance < distances[neighbour]:

                distances[neighbour] = new_distance
                previous[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distances, previous


# Reconstruct shortest path
def get_path(previous, destination):

    path = []

    current = destination

    while current is not None:

        path.append(current)
        current = previous[current]

    path.reverse()

    return path


# Display shortest paths
def display_shortest_paths(graph, start):

    distances, previous = dijkstra(graph, start)

    print("\n========== DIJKSTRA SHORTEST PATH ==========")

    print("\nStarting Location:", start)

    for destination in graph:

        path = get_path(previous, destination)

        print(f"\nDestination: {destination}")

        if distances[destination] == float("inf"):
            print("No available route")
            continue

        print("Shortest Path:", " -> ".join(path))
        print("Total Distance:", distances[destination], "km")


if __name__ == "__main__":

    graph = create_graph()

    display_shortest_paths(graph, "Delhi")
