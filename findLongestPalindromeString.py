# 寻找一个字符串中的最长的回文子字符串
# 如： 'abcdeedcghk' --> 'cdeedc'
# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def getLongest(self, str_list):
        slice_start = 0
        str_slice = str_list[slice_start:]
        
        is_odd = 0
        
              
        while len(str_slice) > 0:
            str_slice_size = len(str_slice)
            
            if str_slice_size == 2:
                return str_slice if str_slice[0] == str_slice[1] else None
            
            is_odd = str_slice_size % 2
            half_size = int(str_slice_size / 2)
            
            left_part = str_slice[:half_size]
            right_part = str_slice[half_size + 1 if is_odd else half_size:]
            
            # reverse the left part, check if equals to right part.
            if left_part[::-1] == right_part:
                return str_slice
            
            slice_start += 1
            str_slice = str_list[slice_start:]
            
        
    def longestPalindrome(self, s: str) -> str:
        sub_str_list = ''
        
        if not s:
            return s

        # note: 'abcdefg' -> 'a' case
        longest_p_str = s[0]
        
        for c in s:
            sub_str_list += c
            if len(sub_str_list) > 1:
                longest = self.getLongest(sub_str_list)
                if longest is not None and len(longest) > len(longest_p_str):
                    longest_p_str = longest
                    
        return longest_p_str
