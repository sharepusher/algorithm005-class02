#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (40.18%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    94.2K
# Total Submissions: 234.2K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#

# @lc code=start
class Solution(object):

    # Mutable sequences can be grafted, excised, 
    # and otherwise modified in place using slice
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        if N == 1 or k % N <= 0:
            return
        
        # replace N-k and k items
        nums[:N-k], nums[-k:] = nums[-k:], nums[:N-k]
        return

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        if N == 1 or k % N <= 0:
            return
        

        # KEY: move k position
        # The 1st step reverse will apply on the first N-k items
        # The 2nd step reverse will apply on the k items to be moved
        # Therefore, the sequence is reverse N-k first, and then k

        self.reverse(0, N-k-1, nums)
        self.reverse(N-k, N-1, nums)
        self.reverse(0, N-1, nums)
        return

    def reverse(self, start, end, nums):
        if start >= end:
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return

    # brute-force
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k %= N
        if N == 1 or k <= 0:
            return
        
        for i in xrange(k):
            self.moveOneStep(nums)
        
        return
    
    # move forward one step of the nums
    # nums[i] = nums[i-1]

    def moveOneStep(self, nums):
        N = len(nums)
        if N <= 1:
            return
        tmp = nums[-1]
        for i in xrange(N-1,-1,-1):
            nums[i] = nums[i-1]
        nums[0] = tmp
        return

# @lc code=end

