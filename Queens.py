#  File: Queens.py

#  Description: Prints out all Queen orientations

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/29/2018

#  Date Last Modified: 10/29/2018
class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.n = n
    self.board = []
    self.set_board()
    

  # initializes empty board of size n
  def set_board (self):
    self.board = []
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n): # check rows and cols
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n): # check diagonals
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # checks if all columns have a queen on one spot
  def valid_cols (self):
    for i in range (self.n):
      queen = False
      for j in range (self.n):
        if self.board[j][i] == 'Q':
          queen = True
      if not queen:
        return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col=0, row=0):
    if (col == self.n):
      global solutions
      self.print_board()
      print()
      solutions += 1
      return True
    else:
      for i in range (self.n) [row:]:
        if (self.is_valid(i, col)):
          self.board[i][col] = 'Q'
          #print('before check, col =', col)
          if (self.recursive_solve (col + 1, 0)):
            #print ('check passed, col =', col)
            #self.print_board()
            self.board[i][col] = '*'
            self.recursive_solve (col, i+1)
            return True
          self.board[i][col] = '*'
      return False
 
def main():
  global solutions
  solutions=0
  n=0
  while True:
    try:
      n = int(input('Enter the size of board: '))
    except:
      continue
    break
  # create a regular chess board
  game = Queens (n)

  # place the queens on the board
  game.recursive_solve()

  print("There are {s} solutions for a {n} x {n} board."\
    .format(s=solutions, n=n))

main()
