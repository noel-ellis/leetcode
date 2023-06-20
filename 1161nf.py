from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfChildNodes(self, node: TreeNode) -> int:
        sum = 0
        if node.left:
            sum += node.left.val

        if node.right:
            sum += node.right.val

        return sum

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val

        sum = self.sumOfChildNodes(self, root)
        if sum > maxSum:
            maxSum = sum


def tests():
    return {'root':  [1, 7, 0, 7, -8, None, None]},


def populate_node(node: TreeNode, root: list):
    if root == []:
        return

    node.left = TreeNode(val=root.pop(0))
    node.right = TreeNode(val=root.pop(0))

    if node.left.val:
        populate_node(node.left, root)

    if node.right.val:
        populate_node(node.right, root)


def makeTree(root: list):
    starting_node = TreeNode(val=root.pop(0))
    populate_node(starting_node, root)
    return starting_node


def main():
    solution = Solution()
    for num, test in enumerate(tests()):
        test['root'] = makeTree(test['root'])
        print(
            f'==============\nresult {num}: {solution.maxLevelSum(**test)}\n')


main()
