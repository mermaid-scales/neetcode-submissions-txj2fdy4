class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #two pass - 2 loops
        #one pass - checking previous element
        #len of set
        #below is hash table

        my_map = {}

        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
            if my_map[num] > 1:
                return True
        return False