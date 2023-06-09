class Solution:
    def toArabic(self, roman: str):
        if roman == "I":
            return 1
        if roman == "V":
            return 5
        if roman == "X":
            return 10
        if roman == "L":
            return 50
        if roman == "C":
            return 100
        if roman == "D":
            return 500
        if roman == "M":
            return 1000

    def romanToInt(self, s: str) -> int:
        sum = 0
        l = list(s)
        while len(l) > 0:
            left = self.toArabic(l.pop(0))
            if len(l) != 0 and self.toArabic(l[0]) > left:
                right = self.toArabic(l.pop(0))
                sum += right - left
                continue
            sum += left

        return sum


def main():
    test1 = "III"
    test2 = "LVIII"
    test3 = "MCMXCIV"

    solution = Solution()
    print(solution.romanToInt(test1))
    print(solution.romanToInt(test2))
    print(solution.romanToInt(test3))


main()
