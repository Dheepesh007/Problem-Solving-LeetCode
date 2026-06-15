from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Compare the frequency of characters in both strings
        return Counter(s) == Counter(t)
