#  File: EvenMagicSquare

#  Description: Prints out all possible Magic Squares of
#  order 4 up to a certain point

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 09/21/2018

#  Date Last Modified: 09/23/2018

import math

s_size=0 # re-initialized in main
#check if the columns of the potiential magic square are not valid
def check_col(A):
    for x in range(s_size):
        sum_col=0
        for y in range(s_size):
            sum_col+=A[(s_size*y)+x]
        if sum_col%const!=0:
            return True
    return False
# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square(magic_square):
    n=s_size
    for i in range(n):  # increment thru list, checking columns and rows
        if not check_sum(magic_square, [0, i, 1, 0]) \
                or not check_sum(magic_square, [i, 0, 0, 1]):
            # check along current row and col respectively
            return False
    # check two diagonals: if valid, return true
    return check_sum(magic_square, [0, 0, 1, 1]) \
           & check_sum(magic_square, [0, n - 1, 1, -1])


# Checks if all numbers along a line in a 2-D list add up to a given sum.
# Returns boolean. First two values of incrs indicate starting point
# and the second two indicate what step to take in what direction along the line
def check_sum(magic_square, incrs):
    test_sum = 0
    for i in range(len(magic_square)):
        test_sum += magic_square[incrs[0]][incrs[1]]
        incrs[0] += incrs[2]
        incrs[1] += incrs[3]
    return test_sum == const

# Checks if all numbers in a 1d list add up to 
def check_lines(A):
    return sum(A)%const==0

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
#Goes through each row to print out each element
    for line in magic_square:
        for x in line:
            counter+=1
# checks if a new line needs to be made
            if counter%(len(magic_square)) == 0:
                print('{:4d}'.format(x))
            else:
                print('{:4d}'.format(x), end="")

# feeds 1d array, returns 2d square array
def convert(A):
    B=[]
    for x in range(s_size):
        B.append(A[x*s_size:(x*s_size+ s_size)])
    return B

# permutes contents of fed array
# if at end of array and array forms a magic square, print
# if at end of row and row does not add to canon sum, move on
def permute (a, lo, hi):
# returns until  it gets to main to the main
  if len(co) == thresh:
    return
  if (lo >= hi):
    a=convert(a)
    if check_square(a):
        co.append(1)
        print_square(a)
        print()
  else:
    for i in range (lo, hi):
        a[i], a[lo] = a[lo], a[i]
        if((lo+1)%s_size==0):

            if check_lines(a[0:lo+1])!=True:
                continue
# check every column if it gets to that point
        if(lo>(s_size-1)*s_size):
            if check_col(a):
                continue
        permute(a[:],lo+1,hi)
        a[i], a[lo] = a[lo], a[i]


def main():
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    global s_size
    global const
    global co
    global thresh
    co=[] # counter for how many squares have been printed
    thresh=int(input("How many Magic Squares would you like from 1-10: "))
    s_size=int(math.sqrt(len(a))) # len of side of square
    const = ((s_size * ((s_size ** 2) + 1)) / 2) # canonical sum
    permute(a,0,len(a))

main()