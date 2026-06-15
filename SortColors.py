class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap current with low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Element is in correct relative position
                mid += 1
            else:
                # Swap current with high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
