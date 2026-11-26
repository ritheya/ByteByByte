# 1470. Shuffle the Array
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn]
# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for i in range(n):
             lst.append(nums[i])
             lst.append(nums[i+n])
        return lst
s=Solution()
print(s.shuffle([2,5,1,3,4,7],3))
print(s.shuffle([1,2,3,4,4,3,2,1],4))
print(s.shuffle([1,1,2,2],2))

# 1108. Defanging an IP Address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
# Constraints:
# The given address is a valid IPv4 address.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr=address.replace('.','[.]') 
        return addr
s=Solution()
print(s.defangIPaddr("1.1.1.1"))
print(s.defangIPaddr( "255.100.50.0"))



# 1678. Goal Parser Interpretation
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
# Given the string command, return the Goal Parser's interpretation of command.
# Example 1:
# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
# Example 2:
# Input: command = "G()()()()(al)"
# Output: "Gooooal"
# Example 3:
# Input: command = "(al)G(al)()()G"
# Output: "alGalooG"
# Constraints:
# 1 <= command.length <= 100
# command consists of "G", "()", and/or "(al)" in some order.
class Solution:
    def interpret(self, command: str) -> str:
        comm=command.replace('G','G')
        comm=command.replace('()','o')
        comm=command.replace('(al)','al')
        return comm
s=Solution()
print(s.interpret('G()(al)'))
print(s.interpret('G()()()()(al)'))
print(s.interpret("(al)G(al)()()G"))