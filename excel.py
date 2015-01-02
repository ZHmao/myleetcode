Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    
    
    
my solution:  python

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        retValue = 0
        length = len(s)
        for i in range(length):
            asciiValue = ord(s[i])
            retValue = retValue + (26**(length-1-i))*(asciiValue - 64)
            
        return retValue
        
