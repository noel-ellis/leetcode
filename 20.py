class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element == '(' or element == '[' or element == '{':
                stack.append(element)
                continue
            if len(stack) == 0:
                return False
            top_of_stack = stack.pop()
            if element == ')' and top_of_stack != '(':
                return False
            if element == ']' and top_of_stack != '[':
                return False
            if element == '}' and top_of_stack != '{':
                return False

        if len(stack) != 0:
            return False
        return True


def tests():
    return {'s': "()"},  {'s': "()[]{}"}, {'s': '([{}])'}, {'s': "(]"}, {'s': ")("}, {'s': '([)]'}, {'s': '['}


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        print(
            f'==============\nresult {num}: {solution.isValid(**test)}\n')


main()
