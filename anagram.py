class Solution:
    def groupAnagrams(self, strs):
        keys = set()
        items = dict()
        for str in strs:
            key = "".join(sorted(str))
            if key in keys:
                items[key].append(str)
            else:
                keys.add(key)
                items[key] = [str]
        result = [x for _, x in items.items()]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
