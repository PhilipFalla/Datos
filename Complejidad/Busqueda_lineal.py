

from memory_profiler import profile

from time import time

@profile

def linear_search(arr, key): #receives an array and a value to search for
    
    for i in range(len(arr)): #for every element in the array, see if it's the value
        if arr[i] == key:
            return True
    
    return False

'''
Testing how fast O(n) time complexity grows...
'''

test_n = 100
test_arr = [7] * test_n
test_key = 8

start_time = time()  # Record the start time
result = linear_search(test_arr, test_key)  # Call the function
end_time = time()  # Record the end time

# Output results
print(f"Result: {result}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(linear_search(test_arr, test_key)) 
