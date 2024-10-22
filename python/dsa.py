
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class Solution:

    def createTree(self, input):
        if not input:
            return None

        root = Node(input[0]) # head
        queue = [root]
        i = 2 #based on assumption of one root node

        while i < len(input):
            current = queue.pop(0)
            children = []

            while i < len(input) and input[i] is not None:
                child = Node(input[i])
                children.append(child)
                queue.append(child) 
                i += 1

            current.children = children 
            i += 1

        return root

    def postorder(self, root: Node) -> List[int]:

        result = []

        def traverse(node):
            if node is None:
                return
            for child in node.children:
                traverse(child) 
            result.append(node.val) 

        traverse(root)
        return result


"""
Input: root = [1,null,3,2,4,null,5,6]
"""

"""
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
"""

solve = Solution()

root1 = solve.createTree([1, None, 3, 2, 4, None, 5, 6])
print("Postorder traversal of tree:", solve.postorder(root1)) 

root2 = solve.createTree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
print("Postorder traversal of tree:", solve.postorder(root2))  