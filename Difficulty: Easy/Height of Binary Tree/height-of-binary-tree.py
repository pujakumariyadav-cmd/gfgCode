'''
Definition for Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    def height(self, root):
        def heightoftree(node):
            if not node:
                return -1  
            left_h = heightoftree(node.left)
            right_h = heightoftree(node.right)
            return 1 + max(left_h, right_h)
        
        return heightoftree(root)

        
        
        
    