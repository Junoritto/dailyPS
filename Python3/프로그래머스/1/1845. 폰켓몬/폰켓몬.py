def solution(nums):
    answer = 0
    set_nums = set(nums)
    answer = min(len(set_nums),(len(nums)//2))
    
    return answer