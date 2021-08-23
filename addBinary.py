class Solution:
    def addBinary(self, a, b):
        result_reversed = ""
        m, n = len(a), len(b)
        if m > n:
            a, b = b, a
            m, n = n, m

        diff = n - m
        flag = False
        for i in range(m - 1, -1, -1):
            if a[i] == "1" and b[diff + i] == "1":
                if flag:
                    result_reversed += "1"
                    flag = True
                else:
                    result_reversed += "0"
                    flag = True
            elif a[i] == "1" or b[diff + i] == "1":
                if flag:
                    result_reversed += "0"
                    flag = True
                else:
                    result_reversed += "1"
                    flag = False
            else:
                if flag:
                    result_reversed += "1"
                    flag = False
                else:
                    result_reversed += "0"
                    flag = False

        for j in range(n - m - 1, -1, -1):
            if b[j] == "1":
                if flag:
                    result_reversed += "0"
                    flag = True
                else:
                    result_reversed += "1"
                    flag = False
            if b[j] == "0":
                if flag:
                    result_reversed += "1"
                    flag = False
                else:
                    result_reversed += "0"
                    flag = False
        # at the end of the add, if flag, add "1" at the head
        if flag:
            result_reversed += "1"

        return result_reversed[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("100", "110010"))
