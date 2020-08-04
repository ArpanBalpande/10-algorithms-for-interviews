
# Given an array containing None values fill in the None values with most recent 
# non None value in the array 
array1 = [1,None,2,3,None,None,5,None]

def solution(nums):
    valid = 0
    temp = []
    for i in nums:
        if i is not None:
            temp.append(i)
            valid = i
        else:
            temp.append(valid)
    return temp

print(solution(array1))