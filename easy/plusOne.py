class Solution:
    def plusOne(self, digits):
        digits = str(digits)
        digits = digits.replace('[', '')
        digits = digits.replace(']', '')
        digits = digits.replace(',', '')
        digits = digits.replace(' ','')
        digits = list(str(int(digits)+1))
        return digits