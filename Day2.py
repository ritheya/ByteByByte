class Solution:
 def runningSum(self, nums: list[int]) -> list[int]:
       runnsum=0
       total=[]
       for i in range(len(nums)):
            runnsum+=nums[i]
            total.append(runnsum)
       return total
s=Solution()
print(s.runningSum([1,2,3,4]))    
nums=[1,2,3,4]
summs=0
total=[]

for i in range(len(nums)):
     summs+=nums[i]
     total.append(summs)
     
print(total)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
      ans=[]
      for i in range(1,n+1):
        if i%3==0 and i%5==0:
         ans.append('FizzBuzz')
        elif i%3==0:
         ans.append('Fizz')
        elif i%5==0:
         ans.append('Buzz')
        else:
          ans.append(str(i))
      return ans
a=Solution()
print(a.fizzBuzz(3))
print(a.fizzBuzz(5))
print(a.fizzBuzz(15))