import sys

sys.setrecursionlimit(int(1e5))

class Node():
    def __init__(self,idx,x,left=None,right=None):
        self.idx = idx
        self.x = x
        self.left = left
        self.right = right
        
def preorder(root,answer):
    if root:
        answer.append(root.idx)
        preorder(root.left,answer)
        preorder(root.right,answer)
    return answer

def postorder(root,answer):
    if root:
        postorder(root.left,answer)
        postorder(root.right,answer)
        answer.append(root.idx)
    return answer

def add_node(parent,x,idx):
    if parent.x<x:
        if parent.right:
            add_node(parent.right,x,idx)
        else:
            parent.right=Node(idx,x)
    else:
        if parent.left:
            add_node(parent.left,x,idx)
        else:
            parent.left=Node(idx,x)
        
        
        
def solution(nodeinfo):
    index_nodeinfo = [[i+1,x,y] for i,(x,y) in enumerate(nodeinfo)]
    index_nodeinfo.sort(key=lambda x : -x[2])
    root = Node(idx = index_nodeinfo[0][0], x=index_nodeinfo[0][1])
    for idx,x,y in index_nodeinfo[1:]:
        add_node(root,x,idx)
        
    return [preorder(root,[]),postorder(root,[])]