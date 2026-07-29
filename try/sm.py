from bisect import bisect_left


def binary_search(arr, target):
    index = bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1


# Example usage for binary search
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(data, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")