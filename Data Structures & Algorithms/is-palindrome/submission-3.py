class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = list("".join(char for char in s if char.isalnum()).lower())

        left, right = 0, len(clean) - 1 

        while left < right: 
            if clean[left] != clean[right]: 
                return False 

            left += 1
            right -= 1

        return True 