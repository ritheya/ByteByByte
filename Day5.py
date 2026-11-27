# Build Array from Permutation
# iven a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
# Example 1:
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
# Example 2:
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3] 
# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in nums:  
            lst.append(nums[i])           
        return lst   
s=Solution()
print(s.buildArray([0,2,1,5,3,4]))
print(s.buildArray([5,0,1,2,3,4]))

# How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
     lst=[]
     for i in range(len(nums)):
         count=0
         for j in range(len(nums)):
            if nums[j]<nums[i]:
                count+=1
         lst.append(count)
     return lst
s=Solution()
print(s.smallerNumbersThanCurrent([6,5,4,8]))
print(s.smallerNumbersThanCurrent([7,7,7,7]))

# Maximum Product of Two Elements in an Array
# You are given an array of integers nums.
# Choose two different indices i and j of that array.
# Return the maximum value of (nums[i] - 1) * (nums[j] - 1).
# Example 1:
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
# Example 2:
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
# Example 3:
# Input: nums = [3,7]
# Output: 12
# Constraints:
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans=(nums[i]-1)*(nums[j]-1)
                lst.append(ans)
        return max(lst)
s=Solution()
print(s.maxProduct([3,4,5,2]))
print(s.maxProduct([1,5,4,5]))
print(s.maxProduct([3,7]))