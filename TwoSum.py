class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the value and its index
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is already in the map, we found our pair!
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the index of the current number
            num_map[num] = i
