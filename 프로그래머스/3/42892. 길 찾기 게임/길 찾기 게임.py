import sys

sys.setrecursionlimit(int(1e5))

class TreeNode:
    def __init__(self, item):
        self.x = item[0]
        self.y = item[1]
        self.id = item[2]
        self.left = None
        self.right = None

def add_node(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            add_node(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            add_node(parent.right, child)

def preorder_traversal(node, result):
    if node is None:
        return
    result.append(node.id)
    preorder_traversal(node.left, result)
    preorder_traversal(node.right, result)

def postorder_traversal(node, result):
    if node is None:
        return
    postorder_traversal(node.left, result)
    postorder_traversal(node.right, result)
    result.append(node.id)

def solution(nodeinfo):
    # 각 노드에 id 추가
    for i, info in enumerate(nodeinfo):
        info.append(i + 1)
    
    # y좌표에 따라 내림차순, x좌표에 따라 오름차순으로 노드 정렬
    nodes = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    
    # 트리 구성
    root = TreeNode(nodes[0])
    for node in nodes[1:]:
        add_node(root, TreeNode(node))
    
    # 순회
    preorder_result = []
    postorder_result = []
    preorder_traversal(root, preorder_result)
    postorder_traversal(root, postorder_result)
    
    return [preorder_result, postorder_result]