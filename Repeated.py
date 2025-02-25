from collections import Counter
def filter_repeated_numbers(input_list):
    counts=Counter(input_list)
    repeated_numbers=[num for num,count in counts.items()if count>1]
    return repeated_numbers
my_list=[44,33,3,49,54,77,999,44,77]
output_list=filter_repeated_numbers(my_list)
print(output_list)
