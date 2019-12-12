class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s:
            return []
        words_length = len(words) * len(words[0])
        s_length = len(s)
        if s_length < words_length:
            return []
        step = len(words[0])
        result = []
        index = 0
        while index < s_length - words_length + 1:
            all_words = [_word for _word in words]
            match = 0
            while all_words:
                word = s[index + match * step: index + (match + 1) * step]
                if word in all_words:
                    match += 1
                    all_words.remove(word)
                else:
                    break
            if match == len(words):
                result.append(index)
                index += step
            else:
                index += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.findSubstring("barfoothefoobarman", ["foo","bar"]) == [0,9]
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
    assert solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]) == [8]
    assert solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]) == [6, 9 ,12]
