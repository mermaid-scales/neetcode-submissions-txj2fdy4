class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_map = {}
        
        for i, num in enumerate(nums):
            my_map[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_map and i != my_map.get(diff):
                return [i, my_map.get(diff)]
        
        return []

        

