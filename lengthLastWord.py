class Solution:
    def lengthOfLastWord(self, s):
        start, end = -1, -1
        count_flag = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and not count_flag:
                start = i
                count_flag = True
            if s[i] == " " and count_flag:
                end = i
                break

        return start - end


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("hello world"))
    print(solution.lengthOfLastWord("    "))
