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
                print("right: {} s[right]: {} c_idx: {}".format(right, s[right], c_idx))
                left = max(left, c_idx[s[right]])

            print("right:{} left:{}. longest: {}. curr length: {}. Set c_idx[{}]:{}".format(right, left, longest, right-left+1, s[right], right + 1))
            longest = max(longest, right - left + 1)
            c_idx[s[right]] = right + 1
        return longest

if __name__ == '__main__':
    test_sol = Solution()
    assert test_sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert test_sol.lengthOfLongestSubstring("bbbbb") == 1
    assert test_sol.lengthOfLongestSubstring("pwwkew") == 3