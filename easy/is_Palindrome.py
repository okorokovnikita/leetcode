class Solution:
    def is_palindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False