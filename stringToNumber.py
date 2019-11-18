class Solution(object):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def myAtoi(self, str):
        start = 0
        end = len(str)
        maxlen = 0
        result = ""
        while start < end:
            index = start
            while index < end:
                if str[index] in Solution.nums:
                    index += 1
                    continue
                if str[index] == ".":
                    if self.is_dot_ok(index, str):
                        index += 1
                        continue
                    index -= 1
                    break
                if str[index] in ["+", "-"]:
                    if index == start:
                        index += 1
                        continue
                    break
                break
            if index - start >= maxlen:
                maxlen = index - start
                result = str[start:index + 1]
            start += 1
        if len(result) == 1 and result[0] not in Solution.nums:
            return ""
        return result

    def is_dot_ok(self, index, str):
        if index == 0 or index == len(str) - 1:
            return False
        return str[index - 1] in Solution.nums and str[index + 1] in Solution.nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.myAtoi("xx ab12.7") == "12.7"
    assert solution.myAtoi(".123") == "123"
    assert solution.myAtoi("+001 +002") == "+002"
    assert solution.myAtoi("-2.") == "-2"
    assert solution.myAtoi("+.1") == "1"
    assert solution.myAtoi("+.+++33") == "+33"
    assert solution.myAtoi("axaxaxabc") == ""