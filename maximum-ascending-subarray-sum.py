# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
import numpy as np
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums_asc = []
        index = 0 
        nums_for_iter = nums
        array_attempt = 0
        nums_asc_list = []
        sums_list = []
        while len(nums_for_iter) >= 1:
            index = 0 
            nums_asc = []
            for i in nums_for_iter:
                if index >= 1:
                    if i > nums_for_iter[index-1]:
                        nums_asc.append(i)
                    else:
                        break
                else:
                    nums_asc.append(i)
                index+=1
            nums_asc_list.append(nums_asc)
            sums_list.append(np.sum(nums_asc))
            array_attempt +=1
            nums_for_iter = nums_for_iter[index:] 
        if len(sums_list) > 0:
            max_len = np.max(sums_list)
        else:
            max_len = 0
        return max_len
