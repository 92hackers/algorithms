import time

class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        word_size = len(words[0])
        window_size = word_size * len(words)

        hashmap = {}

        for w in words:
            if not hashmap.get(w):
                hashmap[w] = 1
            else:
                hashmap[w] += 1

        def split_by_fixed_count(s, count):
            return [s[i:i+count] for i in range(0, len(s), count)]

        i = 0
        while i < (len(s) - window_size) + 1:
            substr = s[i:i+window_size]
            hashmap_copy = hashmap.copy()
            substr_list = split_by_fixed_count(substr, word_size)
            # Check if substr holds all words of the `words` list.
            for w in substr_list:
                value = hashmap_copy.get(w)
                #print("idx:", idx)
                if not value:
                    break

                if value == 1:
                    hashmap_copy.pop(w) # Remove the key
                else:
                    hashmap_copy[w] = value - 1
            #print('after replace:', substr)
            if not hashmap_copy: # If all keys cleared.
                result.append(i)
            i += 1
        return result


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        word_size = len(words[0])
        window_size = word_size * len(words)

        i = 0
        while i < (len(s) - window_size) + 1:
            substr = s[i:i+window_size]
            #print(substr)
            # Check if substr holds all words of the `words` list.
            for w in words:
                idx = self.find_word_index(substr, w, word_size)
                #print("idx:", idx)
                if idx < 0:
                    break
                substr = substr[:idx] + substr[idx+word_size:]
            #print('after replace:', substr)
            if not substr:
                result.append(i)
            i += 1
        return result

    def find_word_index(self, string, word, word_size):
        """
        Find index of the target word in the string.
        """
        start = 0
        while True:
            idx = string.find(word, start)
            if idx < 0 or idx % word_size == 0:
                return idx
            else:
                start += 1


s = "barfoothefoobarman"
words = ["foo","bar"]

#s= "wordgoodgoodgoodbestword"
#words = ["word","good","best","word"]

#s = "ababaab"
#words = ["ab","ba","ba"]


"""
s = "barfoothefoobarman"
words = ["foo","bar"]

s= "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

s = "ababaab"
words = ["ab","ba","ba"]
"""

start = time.time()
solution = Solution2()

print(solution.findSubstring(s, words))

print('time consumed:', time.time() - start)
