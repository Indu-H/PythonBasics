def find_missing_elements(arr):
    min_val, max_val = min(arr), max(arr)
    full_range = set(range(min_val, max_val + 1))
    missing_elements = list(full_range - set(arr))
    return sorted(missing_elements)

# Example usage
input_list = [1, 2, 4, 6, 7]
output_list = find_missing_elements(input_list)
print(output_list)  # Output: [3, 5]
