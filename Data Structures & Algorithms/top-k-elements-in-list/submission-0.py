class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)): 
            key = nums[i]

            if key in seen: 
                seen[key] += 1
            else: 
                seen[key] = 1

        return sorted(seen.keys(), key=lambda x: seen[x], reverse=True)[:k]