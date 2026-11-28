# Replace Elements with Greatest Element on Right Side
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=maximum
            maximum=max(maximum,current)
        return arr
s=Solution()
print(s.replaceElements([17,18,5,4,6,1]))
print(s.replaceElements([400]))

# To lower
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=s.lower()
        return ans
s=Solution()
print(s.toLowerCase( "Hello"))
print(s.toLowerCase( "here"))
print(s.toLowerCase("LOVELY"))

# Check If Two String Arrays are Equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1)==''.join(word2)
s=Solution()
print(s.arrayStringAreEqual(["ab", "c"],["a", "bc"]))
print(s.arrayStringAreEqual( word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(s.arrayStringAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))