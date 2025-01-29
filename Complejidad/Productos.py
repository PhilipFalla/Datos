
def product_in_list(arr, product): #receives an array and a product to look for

    for i in range(len(arr)): #for every element in the array, check if, when multiplied, it equals the product
        for j in range(len(arr)):
            if arr[i] * arr[j] == product:
                return True
            
    return False

'''
Testing how fast O(n^2) time complexity grows...
'''


test_n = 100
test_arr = [1] * test_n
test_product = 7

print(product_in_list(test_arr, test_product))