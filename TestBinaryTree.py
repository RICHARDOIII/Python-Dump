#  File: TestbinaryTree.py

#  Description: Adds new functionality to the Binary Tree object,
#  including depth and breadth first traversal functions, a comparison
#  function, and a height-measuring function.

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/14/2018

#  Date Last Modified: 11/16/2018


# Basic data unit in binary tree
# Contains pointers to left and right
# children, and attribute for data
class Node (object):
# Constructor
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

# The binary tree object.
# Attribute points to node at root
# of tree.
class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into a tree
  def insert (self, data):
    new_node = Node (data)
    # initialize to root if tree empty
    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      # traverse tree until appropriate spot found
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # search for a node with a key
  def search (self, data):
    current = self.root
    while (current != None) and (current.data != data):
      if (data < current.data):
        current = current.lchild
      else:
        current = current.rchild
    if current != None and current.data == data :
        return current
    else: # data not in tree
        return

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order (aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order(aNode.lchild)
      self.post_order(aNode.rchild)
      print(aNode.data)

  # delete a node with a given key
  def delete (self, data):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the key if it exists
    while (delete_node != None) and (delete_node.data != data):
      parent = delete_node
      if (data < delete_node.data):
        delete_node = delete_node.lchild
        if_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if the delete node is a leaf node
    if (delete_node_node.lchild == None) and (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = None
      elif (is_left):
        parent.lchild = None
      else:
        parent.rchild = None

    # check if the delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild
    # check if the delete node has only a right child


    # delete node has both left and right children
    else:
      # find the delete node's successor and successor's parent
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect the delete node's child to be the successor's left child
      successor.lchild = delete_node.lchild

      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

    return delete_node

  # Returns true if two binary trees are similar
  def is_similar (self, pNode):
    local=0
    if pNode != None:
      local = self.search(pNode.data)
      if local==None:
        return False
      if self.is_similar(pNode.lchild)==False:
        return False
      if self.is_similar(pNode.rchild)==False:
        return False
    return True

  # Prints out all nodes at the given level
  # Level indicated by int w/ zero being the root
  # of the tree.
  def print_level (self, level):
    if level==0:
        print(self.root.data)
        return
    current=[self.root]
    # traverse till target level reached
    for i in range(level):
        temp=[]
        for node in current:
            if node.lchild != None:
                temp.append(node.lchild)
            if node.rchild != None:
                temp.append(node.rchild)
        current=temp
    for node in current:
        print(node.data,end=" ")
    print()

  # Returns the height of the tree
  def get_height (self):
    current=[self.root]
    height=0
    while(current!=[]):
        temp=[]
        for node in current:
            if node.lchild!=None:
                temp.append(node.lchild)
            if node.rchild != None:
                temp.append(node.rchild)
        current=temp
        height+=1
    return height

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
    current=[self.root]
    if self.root==None:
        return 0
    left=0
    right=0
    for i in range(self.get_height()):
        temp = []
        for node in current:
            if node.lchild!=None:
                temp.append(node.lchild)
                left+=1
            if node.rchild != None:
                temp.append(node.rchild)
                right+=1
        current=temp
    return left+right+1

def main():
    # Create three trees - two are the same and the third is different
    tree1=Tree()
    tree1.insert(50)
    tree1.insert(30)
    tree1.insert(70)
    tree1.insert(10)
    tree1.insert(40)
    tree1.insert(60)
    tree1.insert(80)
    tree1.insert(7)
    tree1.insert(25)
    tree1.insert(38)
    tree1.insert(47)
    tree1.insert(58)
    tree1.insert(65)
    tree1.insert(77)
    tree1.insert(96)
    tree2=tree1
    tree3 = Tree()
    tree3.insert(50)
    tree3.insert(30)
    tree3.insert(70)
    tree3.insert(10)
    tree3.insert(40)
    tree3.insert(27)
    tree3.insert(80)
    tree3.insert(7)
    tree3.insert(65)
    tree3.insert(38)
    tree3.insert(47)
    tree3.insert(58)
    tree3.insert(78)
    tree3.insert(77)
    tree3.insert(96)
    # Test your method is_similar()
    print(tree3.is_similar(tree1.root))
    print(tree2.is_similar(tree1.root))
    # Print the various levels of two of the trees that are different
    for x in range(tree1.get_height()):
        tree1.print_level(x)
    print()
    for x in range(tree3.get_height()):
        tree3.print_level(x)
    print()
    # Get the height of the two trees that are different
    print(tree1.get_height())
    print(tree3.get_height())
    # Get the total number of nodes a binary search tree
    print(tree3.num_nodes())
main()