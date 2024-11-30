#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


# Helper functions
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_by_queue(root):
    """
    Breadth-first search using a queue
    It's a concept function. Arrange below values (NOT_FOUND, FOUND, OK) to make it work.
    Args:
        root: TreeNode
    """
    NOT_FOUND = None
    FOUND = lambda node: node
    OK = lambda node: False
    queue = deque([root]) # at least one element in the queue to kick start bfs
    while len(queue) > 0: # as long as there is an element in the queue
        node = queue.popleft() # dequeue
        for child in node.children: # enqueue children
            if OK(child): # early return if problem condition met
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND


def dfs(root, target):
    """
    Depth-first search.
    Uses pre-order traversal (root, left, right).
    """
    if root is None:
        return None
    if root.val == target:
        return root
    # return non-null return value from the recursive calls
    left = dfs(root.left, target)
    if left is not None:
        return left

    # at this point, we know left is null, and right could be null or non-null
    # we return right child's recursive call result directly because
    # - if it's non-null we should return it
    # - if it's null, then both left and right are null, we want to return null
    return dfs(root.right, target)
    # the code can be shortened to: return dfs(root.left, target) or dfs(root.right, target)


def get_average_of_levels_in_binary_tree(root):
    """
    Get the average value of each level in a binary tree.
    """
    avgs = []
    nodes = [root]
    while any(nodes):
        S = 0
        nodes_new = []
        n_nodes = 0
        for node in nodes:
            if node is None:
                continue
            S += node.val
            nodes_new += [node.left, node.right]
            n_nodes += 1
        avgs.append(S / n_nodes)
        nodes = nodes_new[:]
    return avgs


def get_max_depth_of_binary_tree(root) -> int:
    """
    Get the maximum depth (height) of a binary tree.
    Args:
        root: TreeNode
    """
    if root is None:
        return 0
    return 1 + max(get_max_depth_of_binary_tree(root.left),
                   get_max_depth_of_binary_tree(root.right))


def get_min_depth_of_binary_tree(root) -> int:
    """
    Get the minimum depth of a binary tree from the root to the leaf.
    Args:
        root: TreeNode
    """
    if root is None:
        return 0
    if root.left is None and root.right is not None:
        return 1 + get_min_depth_of_binary_tree(root.right)
    if root.left is not None and root.right is None:
        return 1 + get_min_depth_of_binary_tree(root.left)
    return 1 + min(get_min_depth_of_binary_tree(root.left), get_min_depth_of_binary_tree(root.right))


def has_path_sum(root, target_sum: int) -> bool:
    """
    Check if a binary tree has a path with a given sum on root-to-leaf paths using DFS.
    Args:
        root: TreeNode
        target_sum: int
    """
    if root is None:
        return False
    target_sum -= root.val
    if (root.left is None and root.right is None) and target_sum == 0: # is leaf and sum is 0?
        return True
    left = has_path_sum(root.left, target_sum)
    if not left:
        right = has_path_sum(root.right, target_sum)
        return right
    return left


def is_tree_height_balanced(root):
    """
    Check if a binary tree is height-balanced.
    Maximum depth of left subtree - maximum depth of right subtree <= 1
    Args:
        root: TreeNode
    """
    if root is None:
        return True
    return (abs(get_max_depth_of_binary_tree(root.left) - \
                get_max_depth_of_binary_tree(root.right)) <= 1) and \
            is_tree_height_balanced(root.left) and \
            is_tree_height_balanced(root.right)


def in_order_traversal(root):
    """
    In-order traversal of a binary tree.
    Recursively add left, root, and right nodes.
    """
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.val] + in_order_traversal(root.right)


def is_symmetric_tree(root) -> bool:
    """
    Check if a binary tree is symmetric using BFS and a queue.
    """
    def is_queue_symmetric(q):
        l = [node.val if node is not None else None for node in q]
        return l == l[::-1]
    queue = deque([root])
    n_max = 2 # Number of nodes in the next level
    while len(queue) > 0 :
        node = queue.popleft()
        queue.extend([node.left, node.right])
        if len(queue) == n_max:
            if not is_queue_symmetric(queue):
                return False
            queue = deque(filter(lambda x: x is not None, queue)) # Remove None nodes
            n_max = len(queue) * 2
    return True


if __name__ == '__main__':
    ## Visualize the sample binary tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    tree_string = '   3\n' \
                  '  / \\\n' \
                  ' 9  20\n' \
                  '    / \\\n' \
                  '   15  7'
    print(tree_string)

    ## Test get_average_of_levels_in_binary_tree
    print()
    print('Test get_average_of_levels_in_binary_tree with a binary tree with'
          '[3, 9, 20, null, null, 15, 7] which is [3.0, 14.5, 11.0]')
    print(get_average_of_levels_in_binary_tree(root1))

    ## Test get_max_depth_of_binary_tree
    print()
    print('Test get_max_depth_of_binary_tree with a binary tree with'
          '[3, 9, 20, null, null, 15, 7] which is 3')
    print(get_max_depth_of_binary_tree(root1))

    ## Test get_min_depth_of_binary_tree
    print()
    print('Test get_min_depth_of_binary_tree with a binary tree with'
          '[3, 9, 20, null, null, 15, 7] which is 2')
    print(get_min_depth_of_binary_tree(root1))

    ## Test has_path_sum
    print()
    print('Test has_path_sum with a binary tree with'
          '[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1] and 22 which is True')
    root2 = TreeNode(5,
                     TreeNode(4,
                              TreeNode(11,
                                       TreeNode(7),
                                       TreeNode(2)),
                              TreeNode(8,
                                       TreeNode(13),
                                       TreeNode(4))),
                    TreeNode(1))
    print(has_path_sum(root2, 22))

    ## Test is_tree_height_balanced
    print()
    print('Test is_tree_height_balanced with a binary tree with'
          '[3, 9, 20, null, null, 15, 7] which is True')
    print(is_tree_height_balanced(root1))

    ## Test in_order_traversal
    print()
    print('Test in_order_traversal with a binary tree with [3, 9, 20, null, null, 15, 7]')
    print(in_order_traversal(root1))

    ## Test is_symmetric_tree
    print()
    print('Test is_symmetric_tree with a symmetric binary tree with [1, 2, 2, 3, 4, 4, 3]')
    root3 = TreeNode(1,
                     TreeNode(2,
                              TreeNode(4), TreeNode(3)),
                     TreeNode(2,
                              TreeNode(3), TreeNode(4)))
    print(is_symmetric_tree(root3))
