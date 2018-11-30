'''
  File: MagicSquare.py

  Description: Uses a unique algorithm to create a magic square of nxn size

  Student's Name: Daniel Espinoza

  Student's UT EID: dee467

  Partner's Name: None

  Partner's UT EID: N/A

  Course Name: CS 313E

  Unique Number: 51350

  Date Created: 9/6/2018

  Date Last Modified:9/7/2018
'''
# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    n=int(n)
    #make a 2-D list of Zeroes
    square = [[0 for i in range(n)] for j in range(n)]
    #makes a float but the idea of making it an int should floor it to take of that .5 off
    mid_index=int(n/2)
    for x in range(n*n):
        value = x+1
# This will set up the beginning of the Magic Square by inserting the 1 in the middle of the bottom row
#  and stores the initial i and j indices
        if value == 1 :
            #current indexing noted by i and j
            i=n-1
            j=mid_index
            square[i][j]= value
        else:
# Makes sure that the conditions are met and it goes up one row if  it is the last element
            if i == n-1 and j == n-1:
                i-=1
            else:
# Goes down one row and one column
                i +=1
                j +=1
# Resets the index if it begins to wrap aroung the corner
                if (i) == n:
                    i = 0
                if (j) == n:
                    j = 0
# if there is a value in the location that is already there goes back two rows up and one column back
                if (square[i][j]!=0):
                    i-=2
                    j-=1
# Sets the value of that grid square
            square[i][j]=value
    return square


# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    counter =0
    print("Here is a {0:d} x {0:d} magic square:".format(len(magic_square)))
#Goes through each row to print out each element
    for line in magic_square:
        for x in line:
            counter+=1
# checks if a new line needs to be made
            if counter%(len(magic_square)) == 0:
                print('{:4d}'.format(x))
            else:
                print('{:4d}'.format(x), end="")






# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    n = len(magic_square)
    check_row=sum(magic_square[0])
# Compares the sums of the rows to the rest them exits if any are false
    for row in magic_square:
        if sum(row) != check_row:
            return False
# fills an list with sums of columns
    columncheck=[]
    for column in magic_square :
        columncheck.append(sum(column))
# Compares the last to the future sum if they conflict returns false
    for x in range(1,len(columncheck)):
        if columncheck[x-1]!= columncheck[x]:
            return False
    Dia_sum1=0
    Dia_sum2=0
    for x in range(n):
# using the indices to get both diagonals to avoid doing another for loop
            Dia_sum1 += magic_square[x][x]
            Dia_sum2 += magic_square[n-x-1][n-x-1]
    if Dia_sum1 != Dia_sum2:
        return False
    return True
# Checks if input is correct
# This function will take in the input
# check if a integer, positive, odd
# returns  boolean values
def check_input(input):
    try:
        input=int(input)
        if (input%2==0 or input<1):
            return False
    except ValueError:
        return False
    return True
def main():
  # Prompt the user to enter an odd number 1 or greater
    user_input= input("Enter  an odd number 1 or greater ")
  # Check the user input
    while (check_input(user_input)!=True):
        user_input= input("Enter an odd number 1 or greater ")
  # Create the magic square
    MagicSquare=make_square(user_input)
  # Print the magic square
    print_square(MagicSquare)
  # Verify that it is a magic square
    if check_square(MagicSquare):
        user_input=int(user_input)
        print("This is a magic square and the canonical sum is {:d}".format(int((user_input)*((user_input*user_input)+1)/2)))
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()