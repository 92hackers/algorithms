class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        
        result = 1
        length = 2

        while length <= len(s):
            i = 1
            hashmap = {}
            goon = False
            index = 0
            while index < len(s):
                c = s[index]
                print(index, c, hashmap, length)
                if not hashmap.get(c): # no duplicate item.
                    hashmap[c] = 1
                    if i == length:
                        result = length
                        length += 1 # Try longer one.
                        goon = True
                        break
                    else:
                        i += 1
                        index += 1
                else:
                    #print("next jump:", index, i)
                    index = index - i + 2
                    i = 1
                    hashmap = {}
            if not goon: # No longger one found.
                break
        return result

solution = Solution()

s = "abcabcbb"
#s = "aab"
#s = "dvdf"


print(solution.lengthOfLongestSubstring(s))
