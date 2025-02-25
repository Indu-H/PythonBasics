def find_sublists(nums,target):
    result=[]
    n=len(nums)
    for start in range(n):
        current_sum=0
        for end in range(start,n):
            current_sum+=nums[end]
            if current_sum==target:
                result.append(nums[start:end+1])
    return result            
        
nums=[1,2,3,4,5]
target=5
print(find_sublists(nums,target))
