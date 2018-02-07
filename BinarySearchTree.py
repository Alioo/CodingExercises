""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
import sys
def checkBSTAgain(root, mini, maxi):
    if root is None:
        return True
    elif root.data > maxi or root.data < mini:
        return False
    return checkBSTAgain(root.left, mini, root.data - 1) and checkBSTAgain(root.right, root.data + 1, maxi)
def checkBST(root):
    return checkBSTAgain(root,-sys.maxsize-1,sys.maxsize)