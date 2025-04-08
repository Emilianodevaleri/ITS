def find_disappeared_numbers(nums: list[int]) -> list[int]:
    
    n=len(nums)
    
    return [i for i in range(1, n + 1) if i not in nums]