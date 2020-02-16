#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (42.61%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    114.4K
# Total Submissions: 267.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution(object):

    # insert the carrier
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []
        
        num = 1
        self.plusNum(digits, num)
        return digits
    def plusNum(self, digits, num):
        if num == 0:
            return
        N = len(digits)
        for i in xrange(N-1, -1, -1):
            current = digits[i]+num
            carrier = current//10
            digits[i] = current % 10
            if carrier == 0:
                break
        if carrier > 0:
            digits.insert(0, carrier)
        return
            

    # reverse and count
    def plusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # reverse the digits, then it would be easier to calculate
        digits.reverse()
        
        # add 1 on the nums
        self.incrementOne(digits)

        digits.reverse()
        return digits
    
    def incrementOne(self, nums):
        carrier = 0
        for i in xrange(len(nums)):
            if i == 0:
                current = nums[i]+1
            else:
                if carrier == 0:
                    break
                current = nums[i]+carrier
            carrier = current//10
            nums[i] = current % 10
        if carrier > 0:
            nums.append(carrier)
        return
 

    # key: each postion only store one number
    # Solution: 
    # brute-force, 1) iterate the array and get number
    # 2) calculate and assign back
    # The most important is how to handle carries; and 
    # how about when the size should be increase
    # 
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        if N == 0:
            return []

        num = self.convertArrayToNum(digits)
        num += 1
        return self.convertNumToArray(num)

    def convertArrayToNum(self, digits):
        num = 0
        j = 0
        for i in xrange(len(digits)-1,-1,-1):
            num += digits[i]*(10**j)
            j += 1
        return num
    def convertNumToArray(self, nums):
        digits = []
        while nums != 0:
            digits.append(nums%10)
            nums //= 10
        digits.reverse()
        return digits

        
# @lc code=end

