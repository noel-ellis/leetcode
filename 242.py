class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        s_list = sorted(s)
        t_list = sorted(t)

        if s_list == t_list:
            return True

        return False


def tests():
    return {'s': "anagram", 't': 'nagaram'},  {'s': "rat", 't': 'car'},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.isAnagram(**test)}\n')


main()
