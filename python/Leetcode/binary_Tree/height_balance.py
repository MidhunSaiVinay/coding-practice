from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def check_height(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check_height(node.left)
        right_height, right_balanced = check_height(node.right)
        
        current_height = max(left_height, right_height) + 1
        is_current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        
        return current_height, is_current_balanced
    
    _, balanced = check_height(root)
    return balanced



# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)


    

def print_levels(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(" ".join(map(str, level_nodes)))

print_levels(root)