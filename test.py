# #even_odd
# a=int(input("Enter a number:"))
# if a%2==0:
#     print("a is even")
# else:
#     print("the num is not even")
# #to caluculate varience
# def caluculate_var(num):
#     mean =sum(num)/len(num)
#     square_diff=[]
#     for x in num:
#         diff=x-mean
#         square=diff**2
#         square_diff.append(square)
#         varience=sum(square_diff)/len(num)
#         return varience
# print(caluculate_var([1,2,3,4]))
        
class Solution:
    def sum(self, num1: int, num2:int) -> int:
         self.num1=num1
         self.num2=num2
    def display(self):
         total=self.num1+self.num2
         return total
s=Solution()
s.sum(num1=int,num2=int)
print(s.display())
# class Sum:
#      def sum(self,num1:int,num2:int):
#           self.num1=num1
#           self.num2=num2
#      def display(self):
#           total=self.num1+self.num2
#           return f'Total sum:{total}'
# s=Sum()
# s.sum(2,3)
# print(s.display())