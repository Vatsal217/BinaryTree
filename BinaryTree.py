
class Node:
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None
def insert(root,node):
        if root is None:
            root=node
        else:
            if root.val< node.val:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)
                    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
def height(self, node):
    if node is None:
        return -1
    left_height = self.height(node.left)
    right_height=self.height(node.right)
    
    return 1+max(left_height, right_height)




r = Node(50)
 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
inorder(r) 
                
print(insert.height(insert.r))
                    
                    
                    