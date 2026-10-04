class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s.lower():
            if char.isalnum():
                res += char
        return res == res[::-1]