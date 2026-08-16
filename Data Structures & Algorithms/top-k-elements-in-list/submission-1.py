class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)): 
            key = nums[i]

            if key in seen: 
                seen[key] += 1
            else: 
                seen[key] = 1
        arr = [] 
        for num, cnt in seen.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res