#  File: Josephus.py

#  Description: Gives the solution to the Josephus problem
#  reading the number of soldiers, the starting soldier to count
#  from and the number of people to skip in each count from
#  a text file.

#  Student Name: Mark Simmons

#  Student UT EID: mjs5839

#  Partner Name: Daniel Espinoza

#  Partner UT EID: dee467

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/9/18

#  Date Last Modified: 11/9/18

class Link(object):
  # Constructor
  def __init__(self,data,next=None):
    self.data=data
    self.next=next

class CircularList(object):
  # Constructor
  def __init__ ( self ): 
    self.first=None

  # Insert an element (value) in the list
  def insert ( self, data):
      new_list=Link(data)
      if self.first==None:
        new_list.next=new_list
        self.first=new_list
      else:
        new_list.next=self.first
        current=self.first
        while(current.next!= self.first):
          current=current.next
        current.next=new_list



  # Find the link with the given data (value)
  def find ( self, data ):
    current=self.first
    # if target is first link, return
    if current.data==data:
      return current
    # else, traverse entire list
    while(current.next != self.first):
      if(current.next.data==data):
        return current.next
      current=current.next
    return None    

  # Delete a link with a given data (value)
  def delete ( self, data ):
    current=self.first
    # if list of len 1 and target is lone link
    if (current.data==data and current.next==current):
        deleted=current
        self.first=None
        return deleted
    # else traverse list
    while(current.next != self.first):
      if(current.next==data):
        deleted=current.next
        current.next=current.next.next
        return deleted
      current=current.next
    if (current.next==data):
        deleted=current.next
        current.next=current.next.next
        self.first=current.next
        return deleted
    return None

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    traverse=1
    # get the start location
    while(traverse<n):
      start=start.next
      traverse+=1
    return self.delete(start) 

  # Return a string representation of a Circular List
  def __str__ ( self ):
    temp=self.first
    strg=""
    if self.first==None:
      return strg
    while(temp.next != self.first):
      strg+=str(temp.data)
      strg+="  "
      temp=temp.next
    strg+=str(temp.data)


    return strg


def main():
  in_file=open("./josephus.txt")
  # first line is number of soldiers
  line=in_file.readline()
  soldiers=line.strip()
 
  # second line is start index
  line=in_file.readline()
  start=int(line.strip())
  
  # third line is number of people to skip in each step
  line=in_file.readline()
  step=int(line.strip())

  # populate circular list
  Circle=CircularList()
  for x in range(int(soldiers)):
    Circle.insert(x+1)
  start=Circle.find(start)

  # incrementally remove soldiers
  for x in range(int(soldiers)):
    start=Circle.delete_after(start,step)
    print(start.data)
    start=start.next
main()
