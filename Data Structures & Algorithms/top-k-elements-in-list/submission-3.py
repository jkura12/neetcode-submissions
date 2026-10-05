class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} 

        # iterate thru nums and keep track of count 
        for i in range(len(nums)): 
            key = nums[i]

            if key in seen: 
                seen[key] += 1
            else: 
                seen[key] = 1

        # arrange seen items by num and count then sort
        arr = [] 
        for num, cnt in seen.items(): 
            arr.append([cnt, num])

        arr.sort() 
        
        # pop out top k values and return the result
        res = [] 
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res