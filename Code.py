class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        t = []
        for x in nums:
            if nums.count(x) == 1:
                t.append(x)
        return t
        
        
