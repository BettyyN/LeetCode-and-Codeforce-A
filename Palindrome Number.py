class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_no = 0
        orginal_no=x
        while x>0:
            digit=int(x%10)
            reversed_no = (reversed_no * 10) + digit
            x/=10
        return orginal_no==reversed_no;
