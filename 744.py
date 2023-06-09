class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        greater_than_target = [letter for letter in letters if letter > target]
        if greater_than_target == []:
            return letters[0]
        return min(greater_than_target)


def tests():
    return {'letters': ["c", "f", "j"], 'target': "a"}, {'letters': ["c", "f", "j"], 'target': "c"}, {'letters': ["x", "x", "y", "y"], 'target': "z"},


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.nextGreatestLetter(**test)}\n')


main()
