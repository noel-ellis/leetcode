def isPalindrome(x: int) -> bool:
    s = str(x)
    if s == s[::-1]:
        return True
    return False


def test1():
    return 121


def test2():
    return -121


def test3():
    return 10


print(f'test1: {isPalindrome(test1())}')
print(f'test2: {isPalindrome(test2())}')
print(f'test3: {isPalindrome(test3())}')
