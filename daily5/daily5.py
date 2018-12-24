class Node:

    def __init__(self, string):
        self.data = string
        self.children = []

    def append(self, child):
        self.children.append(child)


data = [data.strip() for data in open('enable1_word_list', 'r')]

max_depth = 0


def make_tree(node):
    for i in range(0, node.data.__len__()):
        substring = node.data[:i] + node.data[i + 1:]
        if substring in data:
            child = Node(substring)
            node.append(child)
            make_tree(child)

    # return node


def count_max_length(node, count):
    count += 1
    if node.children.__len__() == 0:
        global max_depth
        if max_depth < count:
            # global max_depth
            max_depth = count
    else:
        for child in node.children:
            count_max_length(child, count)


root = Node('princesses')
make_tree(root)
count_max_length(root, 0)
print(max_depth)
