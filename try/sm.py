def binary_search(arr, target):
   left, right = 0, len(arr) - 1
   while left <= right:
       mid = (left + right) // 2
       if arr[mid] == target:
           return mid # Target found
       elif arr[mid] < target:
           left = mid + 1 # Search right half
       else:
           right = mid - 1 # Search left half
   return -1 # Target not found
# Example usage
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search(data, target)
if result != -1:
   print(f"Element found at index {result}")
else:
   print("Element not found")