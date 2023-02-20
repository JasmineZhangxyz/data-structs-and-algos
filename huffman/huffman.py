# Author: Xiyue Zhang
# Date started:
# Last revised:


from heapq import heapify, heappush, heappop


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.left is None:
            self.left = Node(data)
        elif self.right is None:
            self.right = Node(data)


# GLOBAL VARIABLES
heap = []
heapify(heap)


def file_to_array(filename):
    a = []
    dict = {}
    f = open(filename, "r")
    lines = f.readlines()
    for i in range(1, len(lines)):
        line = lines[i].rstrip()
        a.append(int(line))
        dict.update({str(i): int(line)})
    return a, dict


def make_min_heap(a):
    global heap
    for item in a:
        heappush(heap, item)


def huffman(freq_dict):
    global heap
    if len(freq_dict) == 2:
        x = heappop(heap)
        y = heappop(heap)
        tree = Node(None)
        tree.insert(x)
        tree.insert(y)
        return tree
    else:
        # let a, b have the smallest frequencies
        a = heappop(heap)
        b = heappop(heap)
        # define p_ab = p_a + p_b
        p_ab = a + b
        # create new dict of freq -> delete a and b's frequency and add in frequency p_ab
        key_list = list(freq_dict.keys())
        val_list = list(freq_dict.values())
        a_key = key_list[val_list.index(a)]
        b_key = key_list[val_list.index(b)]
        a_b = str(a_key + "_" + b_key)
        temp_dict = freq_dict.copy()
        del temp_dict[a_key]
        del temp_dict[b_key]
        temp_dict.update({a_b: p_ab})
        # replaces x and y with xy in heap
        heappush(heap, p_ab)
        recurse = huffman(temp_dict)
    temp_node = Node(None)
    temp_node.insert(a)
    temp_node.insert(b)
    return temp_node


def max_depth(node):
    if not node:
        return 0
    else:
        l_depth = max_depth(node.left)
        r_depth = max_depth(node.right)
    if l_depth > r_depth:
        return l_depth
    else:
        return r_depth


def min_depth(node):
    if not node:
        return 0
    if node.left is None and node.right is None:
        return 1
    if node.left is None:
        return min_depth(node.right) + 1
    if node.right is None:
        return min_depth(node.left) + 1
    return min(min_depth(node.left), min_depth(node.right)) + 1


if __name__ == "__main__":
    testfile = "TestFile.txt"
    freq = file_to_array(testfile)
    test_array = freq[0]
    test_dict = freq[1]
    make_min_heap(test_array)
    tree = huffman(test_dict)
    part1 = max_depth(tree)
    part2 = min_depth(tree)
    print("Answer to part 1: " + str(part1))
    print("Answer to part 2: " + str(part2))
