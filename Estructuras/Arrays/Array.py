
arr = [1, 2, 3, 4, 5]

for i in range(5): # Example of how we can see the address of an array's elements in python.
    print('Element {} is in address: {}'.format(arr[i], id(arr[i]))) # Huh, formato print similar a C.