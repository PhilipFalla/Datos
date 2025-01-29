

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

print(linear_search(test_arr, test_key)) 