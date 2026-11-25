# max words in senentence
class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        count=0
        app=[]
        for sentence in sentences:
            words=sentence.split()
            count=len(words)
            app.append(count)
        return max(app)
s=Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(s.mostWordsFound(["please wait", "continue to fight", "continue to win"]))

# words="helolo","mommy epdi irukel","nahh sowkiyam"
# maxi=0
# for word in words:
#     wor=word.split()
#     count=len(wor)
#     if count>maxi:
#         maxi=count
# print(maxi)

# contains duplicate
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
s=Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# divide until 0
class Solution:
    def numberOfSteps(self, num: int) -> int:
       count=0
       while num>0:
            if num%2==0:
                num= num//2
            elif num%2!=0:
               num=  num-1
            count+=1
       return count

s=Solution()
print(s.numberOfSteps(14))
print(s.numberOfSteps(8))
print(s.numberOfSteps(123))