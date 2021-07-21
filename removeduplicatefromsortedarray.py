class Solution(object):
    def shuffleForward(self, nums, position):
        currentValue = nums[position]
        """ Function to move one int to the back and shuffle all numbers forward"""
        for currentPosition in range(len(nums) - position - 1):
            nums[position] = nums[position + 1]
            position += 1
        nums[position] = currentValue

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        focal = nums[0]
        # range=len(nums)
        # for num in nums:
        for num in range(len(nums) - 2):
            if nums[num] == nums[i + 1]:
                # Copy nums[i+1]
                # move all ints forward one spot
                self.shuffleForward(nums, i + 1)
                i += 1

# Another answer
# Here we have two runners, i and j.
# We compare when its not equal, because the array is sorted and it signals the end of the duplicate patch
# When they are different we pull in the new different number to replace the first duplicate
class Solution(object):
    def __init__(self):
        print("Instantiating Solution Object")
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 0
        i=0
        for i in range(len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i]!=nums[j]:
                    i +=1
                    nums[i]=nums[j]
        return 