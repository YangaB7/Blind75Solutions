#first soln time complexity O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        parser1 = 0
        parser2 = len(s) - 1
        while parser1 < parser2:
            if not s[parser1].isalnum():
                parser1 += 1
                continue
            if not s[parser2].isalnum():
                parser2 -= 1
                continue
            if s[parser1].lower() == s[parser2].lower():
                parser1 += 1
                parser2 -= 1
            else:
                return False
        return True   
