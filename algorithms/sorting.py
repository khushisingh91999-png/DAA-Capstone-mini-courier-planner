
import json
from pathlib import Path


# Get the location of the parcel dataset
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "parcels.json"


# Function to compare parcel priority and deadline
def parcel_key(parcel):
    return (parcel["priority"], parcel["deadline"])


# MERGE SORT ALGORITHM
def merge_sort(parcels):

    # Base condition
    if len(parcels) <= 1:
        return parcels

    # Divide the list into two halves
    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    # Merge both sorted halves
    return merge(left, right)


# Function to merge two sorted lists
def merge(left, right):

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if parcel_key(left[i]) <= parcel_key(right[j]):
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# QUICK SORT ALGORITHM
def quick_sort(parcels):

    if len(parcels) <= 1:
        return parcels

    pivot = parcels[-1]
    pivot_key = parcel_key(pivot)

    smaller = []
    equal = []
    greater = []

    for parcel in parcels:

        key = parcel_key(parcel)

        if key < pivot_key:
            smaller.append(parcel)

        elif key == pivot_key:
            equal.append(parcel)

        else:
            greater.append(parcel)

    return quick_sort(smaller) + equal + quick_sort(greater)


# Load parcel data from JSON
def load_parcels():

    with open(DATA_FILE, "r") as file:
        parcels = json.load(file)

    return parcels


# Display sorted parcels
def display_parcels(parcels):

    print("\n========== SORTED PARCELS ==========")

    print(f"{'ID':<10}{'DESTINATION':<15}{'PRIORITY':<12}{'DEADLINE':<10}")

    for parcel in parcels:

        print(
            f"{parcel['id']:<10}"
            f"{parcel['destination']:<15}"
            f"{parcel['priority']:<12}"
            f"{parcel['deadline']:<10}"
        )


# Main testing section
if __name__ == "__main__":

    parcels = load_parcels()

    print("\nOriginal Parcel List:")
    display_parcels(parcels)

    print("\nUsing Merge Sort:")
    sorted_parcels = merge_sort(parcels)
    display_parcels(sorted_parcels)

    print("\nUsing Quick Sort:")
    quick_sorted = quick_sort(parcels)
    display_parcels(quick_sorted)
