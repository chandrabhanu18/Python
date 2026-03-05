class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        opt1 = self.help(s, '0')
        opt2 = self.help(s, '1')
        
        return min(opt1, opt2)
    def help(self, s, ch):
        ans = 0
        n = len(s)
        
        for i in range(n):
            if i % 2 == 0 and s[i] != ch:
                ans += 1
            elif i % 2 == 1 and s[i] == ch:
                ans += 1
        
        return ans    
