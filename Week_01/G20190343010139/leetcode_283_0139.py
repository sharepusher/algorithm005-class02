#!/usr/bin/python 
#coding=utf-8
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def testMoveZeroes(self):
        nums1 = []
        moveZeroes(nums1)
        if nums1 != []:
            return False

        nums2 = [0]
        self.moveZeroes(nums2)
        if nums2 != [0]:
            return False
        
        nums3 = [0,1,0,3,12]
        res3 = [1,3,12,0,0]
        self.moveZeroes(nums3)
        if nums3 != res3:
            return False
        return True

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :keep original order !!!
        """
        # move the zeros
        # another way to think
        # stick the zero pointer and wait for non-zero pointer to walk through
        N = len(nums)
        if N <= 1:
            return
        zero = 0
        for i in range(N):
            if nums[i]== 0:
                continue
            if zero != i:
                nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
        return
                


    # do not keep the same order
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # key: in-place -> O(1)space; O(N)time
        # bi-direction two pointers
        # left: start, right:end
        # left++ and exchange with right when there's zero
        # after the exchange, right --
        # corner case: 1 item or no item
        # if left >= right: return; 
        N = len(nums)
        if N <= 1:
            return
        left, right = 0, N-1
        while left < right:
            if left != 0:
                left += 1
                continue
            if right == 0:
                right -= 1
                continue
            # exchange
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return
        
# @lc code=end

