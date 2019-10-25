class Solution(object):
    book = dict()
    book[1, 4] = "IV" # 4
    book[1, 9] = "IX" # 9
    book[2, 4] = "XL" # 40
    book[2, 9] = "XC" # 90
    book[3, 4] = "CD" # 400
    book[3, 9] = "CM" # 900
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        x = num
        round = 0
        while x:
            remain = x % 10
            round += 1
            result.insert(0, self.covertToRoma(remain, round))
            x /= 10
        return "".join(result)

    def covertToRoma(self, number, round):
        if number == 4 or number == 9:
            return Solution.book[round, number]
        return self._covert(number, round)

    def _covert(self, num, round):
        if round == 1:
            return "I"*num if num < 5 else "V" + "I"*(num - 5)
        if round == 2:
            return "X"*num if num < 5 else "L" + "X"*(num - 5)
        if round == 3:
            return "C"*num if num < 5 else "D" + "C"*(num - 5)
        if round == 4:
            return "M"*num


if __name__ == "__main__":
    solution = Solution()
    assert solution.intToRoman(3) == "III"
    assert solution.intToRoman(4) == "IV"
    assert solution.intToRoman(9) == "IX"
    assert solution.intToRoman(58) == "LVIII"
    assert solution.intToRoman(1994) == "MCMXCIV"