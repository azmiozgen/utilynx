from collections import Counter, deque
import json
import re

from tabulate import tabulate


# Helper functions
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


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


def bubble_sort(arr):
    """
    Bubble sort an array.
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap
    return arr


def can_construct_string(str1: str, str2: str) -> bool:
    """
    Check if str1 can be constructed from characters in str2.
    Without Counter, go over str2 and construct a dictionary of characters and their counts.
    Then, go over str1 and decrement the count of the character in the dictionary.
    """
    st1, st2 = Counter(str1), Counter(str2)
    if st1 & st2 == st1:
        return True
    return False


def climb_stairs(n):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    For each n, you can get there either climbing 1 step from n-1 or 2 steps from n-2.
    So, the number of ways to get to n is the sum of the number of ways to get to n-1 and n-2.
    This is the Fibonacci sequence. Solution is the nth Fibonacci number.
    """
    if n in (0, 1):
        return 1
    prev, curr = 1, 1
    for _ in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr


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


def find_power_set(s):
    """
    Find the power set of a set.
    Time complexity: O(2^n)
    Space complexity: O(2^n)
    """
    n = len(s)
    power_set = []
    for i in range(1 << n):  # 2^n (shift 1 left n times)
        subset = [s[j] for j in range(n) if (i & (1 << j))] # Check if jth bit is set in i
        power_set.append(subset)

    return power_set


def find_power_set_simpler(s):
    """
    Find the power set of a set.
    For each element in the set, we can either include it or exclude it.
    For the set [1, 2, 3]:
        1. start with [[], [1]]
        2. don't add or add 2 to each: [[], [2], [1], [1, 2]]
        3. don't add or add 3 to each: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
        4. continue until all elements are processed
    """
    first = s[0]
    ss = [[], [first]]
    for num in s[1:]:
        new_subsets = []
        for subset in ss:
            new_subsets.append(subset[:])
            subset.append(num)
            new_subsets.append(subset[:])
        ss = new_subsets[:]

    return ss


def find_single_number(nums):
    """
    Find the single number in a list of numbers where every number appears twice except for one.
    [2, 2, 1] -> 1
    [4, 1, 2, 1, 2] -> 4
    XOR operation is commutative and associative,
        meaning that we can rearrange them so that two identical element sitting next to each other
        and xor-ing them result in 0.
    Example:
    1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4
    = 0 xor 0 xor 0 xor 4
    = 4
    """
    xor = 0
    for num in nums:
        xor ^= num

    return xor


def flatten_list_of_lists(list_of_lists):
    """
    Flatten a list of lists.
    [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    """
    return [item for sublist in list_of_lists for item in sublist]


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


def get_digits(n):
    """
    Get the digits of a number.
    123 -> [1, 2, 3]
    """
    digits = []
    if n < 10:
        return [n]
    while n >= 10:
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    return digits[::-1]


def get_max_depth_of_binary_tree(root) -> int:
    """
    Get the maximum depth of a binary tree.
    Args:
        root: TreeNode
    """
    if root is None:
        return 0
    return 1 + max(get_max_depth_of_binary_tree(root.left),
                   get_max_depth_of_binary_tree(root.right))


def get_most_common_element_and_its_count(list_of_elements):
    """
    Return the most common element and its count in a list.
    [1, 2, 3, 1, 2, 3, 1, 2, 3] -> (1, 3)
    """
    counter = Counter(list_of_elements)
    if not counter:
        return None, 0
    most_common, count = counter.most_common(1)[0]
    return most_common, count


def get_sqrt_from_scratch(x: int) -> int:
    """
    Get the square root of a number without using the sqrt function.
    Use binary search to find the square root.
    """
    if x == 0:
        return 0
    if x in [1, 2, 3]:
        return 1
    if x == 4:
        return 2
    upper = x // 2 + 1  ## Upper bound trick
    lower = 2
    while lower <= upper:
        root = lower + (upper - lower) // 2
        if root == x // root:
            return root
        if root > x // root:
            upper = root - 1
        else:
            lower = root + 1
    return upper


def print_table(rows, headers=None, tablefmt='fancy_grid'):
    """
    Print a table with the given title and columns.
    rows: list of lists
    headers: list of strings
    tablefmt: str
    print_table([[1, 2, 3], [4, 5, 6]], headers=['a', 'b', 'c']) -->
    | a | b | c |
    |-----------|
    | 1 | 2 | 3 |
    |-----------|
    | 4 | 5 | 6 |
    |-----------|
    """
    if not headers:
        headers = []
    print(tabulate(rows, headers=headers, tablefmt=tablefmt))


def has_cycle(head):
    """
    Check if a linked list has a cycle.
    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


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


def is_valid_parantheses(s):
    """
    Check if a string of parantheses is valid.
    """
    par_map = {')': '(', '}': '{', ']': '['}
    opens = par_map.values()
    stack = []
    for char in s:
        if char in opens:
            stack.append(char)
        else:
            if not stack or par_map[char] != stack[-1]:
                return False
            stack.pop()
    return not stack


def merge_two_sorted_linked_lists(list1, list2):
    """
    list1 and list2 are the heads of two sorted linked lists.
    Merge the two lists into one sorted list.
    Return the head of the merged linked list.

    """
    dummy = ListNode()
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1
    else:
        cur.next = list2

    return dummy.next


def read_json(json_file):
    """
    Read a json file and return the data.
    """
    with open(json_file, encoding='utf-8') as f:
        return json.load(f)


def remove_non_numeric_chars(string):
    """
    Remove all non-numeric characters from a string.
    "sa 00sadl23.txt" -> "0023"
    """
    return re.sub(r'[^0-9]', '', string)


def remove_vowels(string):
    """
    Remove all vowels from a string.
    """
    return re.sub(r'[aeiouAEIOU]', '', string)
    # return ''.join(filter(lambda x: x not in 'aeiouAEIOU', string))


def roman_numeral_to_int(s: str) -> int:
    """
    Convert a roman numeral to an integer.
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    pass_char = False
    for i, char in enumerate(s):
        if pass_char:
            pass_char = False
            continue
        char_val = roman_map[char]
        if i == len(s) - 1:
            char_next = None
        else:
            char_next = s[i + 1]
            char_next_val = roman_map[char_next]
        if char_next is None:
            total += char_val
        else:
            if char_next_val <= char_val:
                total += char_val
            else:
                total += char_next_val - char_val
                pass_char = True
    return total


def write_json(json_file, data, indent=4):
    """
    Write data to a json file.
    """
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent)


if __name__ == '__main__':
    ## Test bubble_sort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print('Test bubble_sort with', arr)
    print(bubble_sort(arr))

    ## Test can_construct_string
    print()
    str1 = 'abc'
    str2 = 'aabbcc'
    print('Test can_construct_string with', str1, str2)
    print(can_construct_string(str1, str2))

    ## Test climb_stairs
    print()
    n = 4
    print('Test climb_stairs with', n)
    print(climb_stairs(n))

    ## Test find_power_set
    print()
    s = [1, 2, 3]
    print('Test find_power_set with', s)
    print(find_power_set(s))

    ## Test find_power_set_simpler
    print()
    print('Test find_power_set_simpler with', s)
    print(find_power_set_simpler(s))

    ## Test find_single_number
    print()
    print('Test find_single_number with [2, 2, 1]')
    print(find_single_number([2, 2, 1]))

    ## Test flatten_list_of_lists
    print()
    print('Test flatten_list_of_lists with [[1, 2], [3, 4]]')
    print(flatten_list_of_lists([[1, 2], [3, 4]]))

    ## Test get_average_of_levels_in_binary_tree
    print()
    print('Test get_average_of_levels_in_binary_tree with a binary tree with'
          '[3, 9, 20, null, null, 15, 7] which is [3.0, 14.5, 11.0]')
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(get_average_of_levels_in_binary_tree(root))

    ## Test get_digits
    print()
    n = 123
    print('Test get_digits with', n)
    print(get_digits(n))

    ## Test get_max_depth_of_binary_tree
    print()
    print('Test get_max_depth_of_binary_tree with a binary tree with'
          '[3, 9, 20, null, null, 15, 7]')
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(get_max_depth_of_binary_tree(root))

    ## Test get_most_common_element_and_its_count
    print()
    print('Test get_most_common_element_and_its_count with [1, 2, 3, 1, 2, 3, 1, 2, 3]')
    print(get_most_common_element_and_its_count([1, 2, 3, 1, 2, 3, 1, 2, 3]))

    ## Test get_sqrt_from_scratch
    print()
    print('Test get_sqrt_from_scratch with', 8)
    print(get_sqrt_from_scratch(8))
    print('Test get_sqrt_from_scratch with', 122)
    print(get_sqrt_from_scratch(122))

    ## Test has_cycle
    print()
    print('Test has_cycle with a linked list with cycle (3 -> 2 -> 0 -> 2)')
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = head.next
    print(has_cycle(head))

    ## Test in_order_traversal
    print()
    print('Test in_order_traversal with a binary tree with [3, 9, 20, null, null, 15, 7]')
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20,
                             TreeNode(15), TreeNode(7)))
    print(in_order_traversal(root))

    ## Test is_symmetric_tree
    print()
    print('Test is_symmetric_tree with a symmetric binary tree with [1, 2, 2, 3, 4, 4, 3]')
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4), TreeNode(3)),
                    TreeNode(2,
                             TreeNode(3), TreeNode(4)))
    print(is_symmetric_tree(root))

    ## Test is_valid_parantheses
    print()
    print('Test is_valid_parantheses with "([])"')
    print(is_valid_parantheses('([])'))
    print('Test is_valid_parantheses with "([)]"')
    print(is_valid_parantheses('([)]'))

    ## Test merge_two_sorted_linked_lists
    print()
    print('Test merge_two_sorted_linked_lists with two linked lists'
          '(1 -> 2 -> 4) and (1 -> 3 -> 4)')
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merged = merge_two_sorted_linked_lists(list1, list2)
    while merged:
        print(merged.val, end='->')
        merged = merged.next

    ## Test print_table
    print()
    print('Test print_table with [[1, 2, 3], [4, 5, 6]]')
    print_table([[1, 2, 3], [4, 5, 6]])

    ## Test remove_vowels
    print()
    print('Test remove_vowels with "sa 00sadl23.txt"')
    print(remove_vowels('sa 00sadl23.txt'))

    ## Test roman_numeral_to_int
    print()
    print('Test roman_numeral_to_int with "III (3)"')
    print(roman_numeral_to_int('III'))
    print('Test roman_numeral_to_int with "MDCCLXXIII (1773)"')
    print(roman_numeral_to_int('MDCCLXXIII'))
    print('Test roman_numeral_to_int with "MCMXCVI (1996)"')
    print(roman_numeral_to_int('MCMXCVI'))
