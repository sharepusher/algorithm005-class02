#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    # 1) find two num in nums, and the sum of the two num
    # is the target
    # 2) the two num should be different item
    # but they can be same value(different index)

    # Solution:
    # 1. brute-force, O(N^2) O(1)space
    # 2. O(N) space to record the value and index 
    # O(N) time to find the sum target
    # 3. O(NlogN) time, O(1) space? Sort first
    # Then two pointers

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        # sort has to remember the index
        # or it will mess the index up
        start, end = 0, len(nums)-1
        while start < end:


    # O(N)time O(N)space
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
           
        visited = {}
        # nums to dict set
        for i in xrange(len(nums)):
            if (target - nums[i]) in visited:
                return [visited[target - nums[i]][-1], i]

            if nums[i] not in visited:
                visited[nums[i]] = [i]
            else:
                visited[nums[i]].append(i)
        return []
        

    # O(N^2) time
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return []    


        
# @lc code=end

