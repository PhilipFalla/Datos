#include <stdio.h>

int main() 
{
    int arr[5] = {1, 2, 3, 4, 5};
    int i; // Initialize to understand where i is located.

    printf("Counter i is in address: %d\n", (int) &i); 

    for (i = 0; i < 5; i++) // For loop to understand data size in RAM using the address for elements in an array.
    {
        printf("Element %d is in address: %d\n", arr[i], (int) &arr[i]); 
    }
}