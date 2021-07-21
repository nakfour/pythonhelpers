class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 0
        if k == 0:
            return nums

        # put the pointer at the end of the array or list
        lastPosition = len(nums) - 1

        # iterate k times
        while k > 0:
            # flip first and last
            # get element into temp
            temp = nums[lastPosition]
            # move all elements back once starting from the back
            position = len(nums) - 1
            while position > 0:
                nums[position] = nums[position - 1]
                position -= 1
            nums[0] = temp
            k -= 1

        return nums