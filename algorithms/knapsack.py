
import json
from pathlib import Path


# Load parcel data from JSON file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "parcels.json"


def load_parcels():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# 0/1 Knapsack using Dynamic Programming
def knapsack(parcels, capacity):

    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            if weight <= w:

                # Maximum of including or excluding parcel
                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )

            else:

                # Cannot include parcel
                dp[i][w] = dp[i - 1][w]

    # Find selected parcels using backtracking
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected.append(parcels[i - 1])
            w -= parcels[i - 1]["weight"]

    selected.reverse()

    return dp[n][capacity], selected, dp


# Display complete DP table
def display_dp_table(dp, parcels, capacity):

    print("\n========== DYNAMIC PROGRAMMING TABLE ==========\n")

    print(f"{'Parcel':<12}", end="")

    for w in range(capacity + 1):
        print(f"{w:>5}", end="")

    print("\n" + "-" * (12 + 5 * (capacity + 1)))

    print(f"{'None':<12}", end="")

    for value in dp[0]:
        print(f"{value:>5}", end="")

    print()

    for i in range(1, len(dp)):

        print(f"{parcels[i - 1]['id']:<12}", end="")

        for value in dp[i]:
            print(f"{value:>5}", end="")

        print()


# Display selected parcels
def display_selected_parcels(selected, total_value, capacity):

    print("\n========== SELECTED PARCELS ==========\n")

    total_weight = 0

    for parcel in selected:

        print(
            f"{parcel['id']} | "
            f"{parcel['destination']} | "
            f"Weight: {parcel['weight']} kg | "
            f"Value: Rs. {parcel['value']}"
        )

        total_weight += parcel["weight"]

    print("\nTotal Weight:", total_weight, "kg")
    print("Vehicle Capacity:", capacity, "kg")
    print("Remaining Capacity:", capacity - total_weight, "kg")
    print("Maximum Total Value: Rs.", total_value)


# Main testing section
if __name__ == "__main__":

    parcels = load_parcels()

    capacity = 10

    maximum_value, selected, dp = knapsack(parcels, capacity)

    display_dp_table(dp, parcels, capacity)

    display_selected_parcels(selected, maximum_value, capacity)
