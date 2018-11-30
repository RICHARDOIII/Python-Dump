#  File: BST_Cipher.py

#  Description: Using a binary tree to encrypt and decrypt a password

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created:11/12/2018

#  Date Last Modified:11/12/2018
class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    # the root is equal to the fisrt character
    self.root = Node(ord(encrypt_str[0]))
    #inserts the rest using the insert method
    for char in encrypt_str[1:]:
      self.insert(char)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    data = ord(ch)
    # only accept spaces and lowercase letters
    if (data != 32) and (data < 97 and data > 122):
      return
    new_node = Node(data)
    #print("new node", new_node)
    # if the root is empty then the root is the new one
    if self.root == None:
      self.root = new_node
    else:
      current = self.root
      # while it hasn't gotten to the end of the branch
      while not (current.isLeaf()):
        if data == current.data: # skip repeat chars
          return
      #if the current node has not left child set the current equal
        # to the left child
        elif data < current.data:
          if not current.hasLeft():
            break
          current = current.lchild
        else: # data > current.data
          if not current.hasRight():
            break
          current = current.rchild
      # if the letter comes before then the left child is the new node
      if data < current.data:
        current.lchild = new_node
      #else the right child becomes the new node
      else: 
        current.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    curr = self.root
    strg = ''
    tgt = ord(ch)
    # the thing cjecks out return asterisk
    if curr.data == tgt:
      return '*'
    while curr != None:
      # if the current is the target return string
      if curr.data == tgt:
        return strg
      # if target is less then current add <
      elif tgt < curr.data:
        strg += '<'
        curr = curr.lchild
      # else target is greater and add > to string
      else: # tgt > curr.data
        strg += '>'
        curr = curr.rchild
    #else return a ''
    return ''

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
  #if we have * return root data
    if st == '*':
      return chr(self.root.data)
    curr = self.root
    for char in st:
# if the current is none then return empty string
      if curr == None:
        return ''
# if the thingg is a < go the the left
      elif char == '<':
        curr = curr.lchild
# if the thing is a > go to the right
      elif char == '>':
        curr = curr.rchild
# if niether then return empty string
      else:
        return ''
    if curr == None:
      return ''
# return the currents data
    return chr(curr.data)

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    st = st.lower()
    return_st = ''
    # for every character in the passed in
    # str it will go through the search
    for char in st:
      #while in alphabet or a  space
      if char.isalpha() or char == ' ':
        return_st += self.search(char) + '!'
    return return_st[:-1] # cut out last '!'


  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    #split up the thing by !
    st = st.split(sep='!')
    return_st = ''
    # or every thing is string st we use the traverse method
    for ch in st:
      return_st += self.traverse(ch)
    return return_st

  # print 2-D representation of binary tree object
  # prints every node beneath passed node
  # only prints passed node if root
  def print_tree (self, level):
    next_level = []
    strg = ''
    leaf_count = 0
    # for each node we go up down then up the levels
    #  til we get back to the roots
    for node in level:
      strg += str(node) + ' '
      if node == ' ' or node.isLeaf():
        next_level += [' ', ' ']
        leaf_count += 1
        continue
      # left node then right node
      if node.hasLeft():
        next_level.append(node.lchild)
      else:
        next_level.append(' ')
      if node.hasRight():
        next_level.append(node.rchild)
      # spacer
      else:
        next_level.append(' ')
    # once we get to all the leafs of that level we go up
    if leaf_count == len(level):
      return
    #recursive call
    next_strg = self.print_tree(next_level)
    #when we get back to the root return strg reprensation
    if next_strg != None:
      strg += next_strg
    return strg




class Node (object):
  # Constructor
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  # Return true if leaf node
  def isLeaf (self):
    # if the node has any children it will return False not at leaf
    # else it is
    return self.lchild == None and self.rchild == None

  # Return true if has lchild
  def hasLeft (self):
    return self.lchild != None
  # Return true if has rchild
  def hasRight (self):

    return self.rchild != None
  # Returns the node's current data as the printable data
  def __str__ (self):
    return str(self.data)

def main():
  # have the user input and set the encryption key.
  key = input("Enter encryption key: ")
  # creates a binary tree using the key
  encrypt_tree = Tree(key)
  print()
  encrypt = input("Enter string to be encrypted: ")
  # passes the word to be encrypted into the encrypt method
  print("Encrypted string: ", encrypt_tree.encrypt(encrypt))

  print()
  decrypt = input("Enter string to be decrypted")
  # passes the word to be decrypted into the decrypt method
  print("Decrypted string: ", encrypt_tree.decrypt(decrypt))

main()