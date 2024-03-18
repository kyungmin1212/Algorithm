import sys

sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add_node(root, x):
    if root.value < x:
        if root.right:
            add_node(root.right, x)
        else:
            root.right = Node(value=x)
    else:
        if root.left:
            add_node(root.left, x)
        else:
            root.left = Node(value=x)


root = Node(value=arr[0])
for item in arr[1:]:
    add_node(root, item)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)
    return


postorder(root)
