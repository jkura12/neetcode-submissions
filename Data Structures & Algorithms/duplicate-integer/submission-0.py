class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = [] 
        duplicates = []
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else: 
                seen.append(num)
        if len(duplicates) > 0:
            return True
        else:
            return False
