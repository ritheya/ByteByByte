#       my bruteforce
# import numpy as np
# class Solution:
#     def getConcatenation(self, nums: list[int]) -> list[int]:
#         ans=np.array([nums])
#         answer=np.tile(ans,2)
#         return list(answer)
# s=Solution()
# print(s.getConcatenation([1,2,1]))
# print(s.getConcatenation([1,3,2,1]))
#       optimised
# class Solution:
#     def getConcatenation(self, nums: list[int]) -> list[int]:
#         ans=nums
#         result=ans*2
#         return result
# s=Solution()
# print(s.getConcatenation([1,2,1]))
# print(s.getConcatenation([1,3,2,1]))


# 2 BF
# class Solution:
#     def maximumWealth(self, accounts: list[list[int]]) -> int:
#         wealth=[]
#         for i in range(len(accounts)):
#             total=sum(accounts[i])
#             wealth.append(total)
#         return max(wealth)
# s=Solution()
# print(s.maximumWealth([[1,2,3],[3,2,1]]))
# print(s.maximumWealth([[1,5],[7,3],[3,5]]))
# print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))


# 3
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
s=Solution()
print(s.numIdenticalPairs([1,2,3,1,1,3]))
print(s.numIdenticalPairs([1,1,1,1]))
print(s.numIdenticalPairs([1,2,3]))