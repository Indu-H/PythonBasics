def left_rotate_array(arr, d):
    #Function to rotate the array to the left by d positions

    #Parameters:
    #arr (list): The input array
    #d (int): Number of positions to rotate

    #Returns:
    #list: Rotated array
    # Calculate the length of the array
    n = len(arr)
    
    # To handle the case when d is greater than n
    d = d % n
    
    # Initialize a temporary array to store elements to be rotated
    temp = []
    
    # Store the first d elements in temp
    for i in range(d):
        temp.append(arr[i])
    
    # Shift the remaining elements to the left by d positions
    for i in range(d, n):
        arr[i-d] = arr[i]
    
    # Copy the elements from temp back to the original array
    for i in range(d):
        arr[n-d+i] = temp[i]
    
    return arr

# Example usage:
arr = [1, 2, 3, 4, 5]
d = 2
rotated_arr = left_rotate_array(arr, d)
print("Original array:", arr)
print("Array rotated to the left by", d, "positions:", rotated_arr)
