#  File: Work.py 

#  Description:  Find the least amount of line to initially code before drinking a cup of coffee

#  Student Name:  Daniel Espinoza

#  Student UT EID:  dee467

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created:10/7/2018

#  Date Last Modified:10/8/2018

def black_coffee(test_num,k,cups):
#Base case
    if test_num//k**cups==0:
        return 0
    else:
# creates a recursive function to sum the series
        return test_num//k**cups + black_coffee(test_num,k,cups+1)

def binarySearch (n, k):
  lo = 0
  hi = n
  while (lo <= hi):
# get the middle value
    mid = (lo + hi) // 2
# the v passes but we still need to get the lowest possible
# v so we scale the hi to the value of the mid
    if ( (black_coffee(mid,k,0)>=n) and mid<hi):
      hi=mid
# the v does not pass and the scale should move up the low
# to the position of the mid 
    elif( (black_coffee(mid,k,0)>=n)==False and mid>lo):
      lo=mid+1
# the reason it is the hi and not mid is because the lo and mid would
# the same and that value should not work but the hi should.
    else:
      return hi
  return -1

def main():

    in_file=open("./work.txt","r")
# read in however many test cases to test
#from the first line and covert to int
    num_test=in_file.readline()
    num_test=num_test.strip()
    num_test=int(num_test)

    for x in range(num_test):
# read in each line and pass it to the binary search function
        line=in_file.readline()
        line=line.strip()
        cases=line.split()
# print out the least amount of lines of code
        print(binarySearch(int(cases[0]),int(cases[1])))
main()
