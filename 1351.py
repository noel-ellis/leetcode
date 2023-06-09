def countNegatives(grid: list[list[int]]) -> int:
    sum = 0
    m = len(grid)
    n = len(grid[0])
    i = 0
    while i < m:
        j = 0
        while j < n:
            print(f'row: {i}; column: {j}; element: {grid[i][j]}')
            if grid[i][j] < 0:
                sum += (m - i) * (n - j)
                n -= n - j
                j += 1
                print(f'    *** n: {n}; sum: {sum}')
                break
            j += 1
        i += 1

    return sum


def test1():
    return [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]


def test2():
    return [[3, 2], [1, 0]]


def test3():
    return [[3, 2], [-3, -3], [-3, -3], [-3, -3]]


def main():
    print(f'test1:{countNegatives(test1())}')
    print(f'test2:{countNegatives(test2())}')
    print(f'test3:{countNegatives(test3())}')


main()
