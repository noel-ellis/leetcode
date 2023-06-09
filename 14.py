class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0
        length = 0
        strs_shortened = ['']
        while len(set(strs_shortened)) == 1:
            strs_shortened = [word[:i+1]
                              for word in strs]
            if len(strs_shortened[0]) == length:
                return strs_shortened[0]
            length = len(strs_shortened[0])
            i += 1

        return strs_shortened[0][:-1]


def tests():
    return ["flower", "flow", "flight"], ["dog", "racecar", "car"], ["a", "abc"], ["abc", "c"], ['a', 'a']


def main():
    solution = Solution()
    for test in tests():
        print(
            f'======================\nresult: {solution.longestCommonPrefix(test)}\n======================')


main()
