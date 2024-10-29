## Implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

## Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

## Compare Performance
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

## Implement Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

## Create a Main Function
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()

            ### Exercises for Students

## Modify the linear search function to return all indices where the target appears, not just the first one.
def linear_search_to_return_all_indices(arr, vlaue):
    indice = []
    for i in range(len(arr)):
        if arr[i] == vlaue:
            indice.append(i)
    return indice if indice else -1  

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
outcome = linear_search_to_return_all_indices(test_list, 5)
print(f"Linear Search (All Indices): Indices of 5 are {outcome}")

## Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
def binary_insertion_point_search(arr, value):
    leftside, rightside = 0, len(arr) - 1
    while leftside <= rightside:
        middle = (leftside + rightside) // 2
        if arr[middle] == value:
            return mid
        elif arr[middle] < value:
            leftside = middle + 1
        else:
            rightside = middle - 1
    return leftside 

# Test the function
test_list = [1, 3, 4, 5, 6, 8, 9]
insertion = binary_insertion_point_search(test_list, 2)
print(f"Insertion for 2 in sorted list is {insertion}")

## Create a function that counts the number of comparisons made in each search algorithm.
def linear_count_number_of_comparisons(arr, value):
    num = 0
    for i in range(len(arr)):
        num += 1
        if arr[i] == value:
            return i, num  
    return -1, num  

def binary_count_number_of_comparisons(arr, value):
    leftside, rightside = 0, len(arr) - 1
    num = 0
    while leftside <= rightside:
        num += 1
        middle = (leftside + rightside) // 2
        if arr[middle] == value:
            return middle, num 
        elif arr[middle] < value:
            leftside = middle + 1
        else:
            rightside = middle - 1
    return -1, num 

# Test the functions
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(test_list)
value = 9

# Linear search with count
index, comparisons = linear_count_number_of_comparisons(test_list, value )
print(f"Linear Search: Index of {value} is {index}, Comparisons made: {comparisons}")

# Binary search with count
index, comparisons = binary_count_number_of_comparisons(sorted_list, value)
print(f"Binary Search: Index of {value} is {index}, Comparisons made: {comparisons}")

## Implement a jump search algorithm and compare its performance with linear and binary search.
def find_integer(x):
    apppeox_root = 0
    while (apppeox_root + 1) * (apppeox_root + 1) <= x:
        apppeox_root += 1
    return apppeox_root

def jump_search(arr, value):
    length = len(arr)
    jump_distance = find_integer(length)  
    initial_position = 0

    while initial_position < length and arr[min(jump_distance, length) - 1] < value:
        initial_position = jump_distance
        jump_distance += jump_search(length)
        if initial_position >= length:
            return -1  

    for current_position in range(initial_position, min(jump_distance, length)):
        if arr[current_position] == value:
            return current_position
    return -1  

# Test the function
clean_list = [1, 3, 5, 6, 8, 12, 14, 18, 20, 22, 25]
vlaue = 18
outcome = jump_search(clean_list, value)
print(f"Jump Search: Index of {vlaue} is {outcome}")

