import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        #Write your code here
        queue = []
        result = []
        if root:
            queue.append(root)
            
            while queue:
                tmp_root = queue.pop(0)
                result.append(tmp_root.data)
                if tmp_root.left:
                    queue.append(tmp_root.left)
                if tmp_root.right:
                    queue.append(tmp_root.right)
        result = map(str, result)
        print(' '.join(result))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
