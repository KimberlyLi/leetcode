class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = left = 0
        c_idx = {}
        
        for right in range(len(s)):
            if s[right] in c_idx:
                left = max(left, c_idx[s[right]])
            longest = max(longest, right - left + 1)
            c_idx[s[right]] = right + 1
        return longest
