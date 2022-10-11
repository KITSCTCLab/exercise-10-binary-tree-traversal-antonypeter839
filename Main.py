class BinaryTreeNode:
     def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
   
    
def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    if root is not None:
        if new_value < root.new_value:
            if root.new_value is None:
                root.left_child = BinaryTreeNode(new_value)
            else:
                root.left_child.insert(root, new_value)
        elif new_value > root.datanew_value:
            if root.new_value is None:
                root.right_child = BinaryTreeNode(new_value)
            else:
                root.right_child.insert(root, new_value)
    else:
        root = BinaryTreeNode(new_value)
          
def inorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res = inorder(root.left_child)
        res.append(root.data)
        res = res + inorder(root.right_child)
    return res

def preorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res.append(root.data)
        res = res + preorder(root.left_child)
        res = res + preorder(root.right_child)
    return res


def postorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res = postorder(root.left_child)
        res = res + postorder(root.right_child)
        res.append(root.data)
    return res


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
