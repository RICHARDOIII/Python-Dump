#  File: TestLinkedList.py

#  Description: Creates a Link and LinkedList class,
#  creates and tests multiple helper methods to expand
#  functionality

#  Student Name: Mark Simmons

#  Student UT EID: mjs5839

#  Partner Name: Daniel Espinoza

#  Partner UT EID: dee467

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/4/18

#  Date Last Modified: 11/16/18

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return(str(self.data))


class LinkedList(object):
    def __init__(self):
        self.first = None

    # insert link at beginning of list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # insert link at end of list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        # set new_link as first if list empty
        if (current == None):
            self.first = new_link
            return

        # traverse list to end
        while (current.next != None):
            current = current.next

        current.next = new_link

    # searches list for given link, 
    def find_link(self, data):
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current



    # add an item in an ordered list in ascending order
    def insert_in_order (self, data):
            current = self.first
            if current.data >= data:
                self.insert_first(data)
                return
            while (current != None):
                if current.next.data != None and current.next.data >= data:
                    current.next = Link(data, current.next)
                    return
                current = current.next


    # return length of linked list
    def get_num_links(self):
        length=0
        temp=self.first
        while (temp != None):
            length+=1
            temp = temp.next
        return length

    # search in an unordered list, return None if not found
    def find_unordered (self, data):
        temp=self.first
        if temp.data == data:
            return True
        while (temp.next != None):
            if temp.next.data == data:
                return True
            temp = temp.next
        return None

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
            current = self.first
            while (current != None):
                if current.data == data:
                    return True
                elif current.data > data:
                    return None
                current = current.next
            return None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
            current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current.data

  # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        strg = ""
        temp = self.first
        if self.first==None:
            return strg
        while (temp != None):
            strg += str(temp.data)
            temp = temp.next
            strg += "  "
        if self.first.next == None:
            strg += str(self.first.data)
        return strg

  # Copy the contents of a list and return new list
    def copy_list (self):
        temp=self.first
        copy=LinkedList()
        while (temp != None):
            copy.insert_last(temp.data)
            temp = temp.next
        return copy

    # Reverse the contents of a list and return new list
    def reverse_list (self):
            temp = self.first
            reverse = LinkedList()
            while (temp != None):
                reverse.insert_first(temp.data)
                temp = temp.next
            return reverse

# Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        temp=self.first
        temp2=self.copy_list()
        sorted=LinkedList()
        while(sorted.get_num_links()!=self.get_num_links()):
            min=temp.data
            while (temp !=None):
                if temp.data<min:
                    min=temp.data
                temp=temp.next
            sorted.insert_last(min)
            temp2.delete_link(min)
            temp=temp2.first
        return sorted

  # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
            current = self.first
            previous = current
            while (current != None):
                if current.data < previous.data:
                    return False
                previous = current
                current = previous.next
            return False

  # Return True if a list is empty or False otherwise
    def is_empty (self):
        return self.first==None

  # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
            s_current = self.first
            o_current = other.first
            return_list = LinkedList()
            while (s_current != None) and (o_current != None):
                if (s_current.data < o_current.data):
                    return_list.insert_last(s_current)
                    s_current = s_current.next
                else:
                    return_list.insert_last(o_current)
                    o_current = o_current.next
            if (s_current == None):
                while (o_current != None):
                    return_list.insert_last(o_current)
                    o_current = o_current.next
            elif (o_current == None):
                while (s_current != None):
                    return_list.insert_last(s_current)
                    s_current = s_current.next
            return return_list

  # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
            s_current = self.first
            o_current = other.first
            while (s_current != None) or (o_current != None):
                if s_current == None:
                    return False
                elif o_current == None:
                    return False
                elif s_current.data != o_current.data:
                    return False
                else:
                    s_current = s_current.next
                    o_current = o_current.next


  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
            links = {}
            return_list = self.copy_list()
            return_list=return_list.reverse_list()
            current = self.first
            while (current != None):
                links[current.data] = True
                current = current.next
            current = self.first
            while (current != None):

                if links[current.data]:
                    links[current.data] = False
                elif not links[current.data]:
                    links[current.data]="dup"
                    # delete this entry if encountered again
                if links[current.data]=="dup":
                    return_list.delete_link(current.data)
                current = current.next
            return_list=return_list.reverse_list()
            return return_list

def main():
    list_1 = LinkedList()
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    print("Testing insert_first and __str__")
    list_1.insert_first(8)
    list_1.insert_first(-5)
    list_1.insert_first(-2)
    list_1.insert_first(-6)
    list_1.insert_first(4)
    list_1.insert_first(42)
    list_1.insert_first(3)
    list_1.insert_first(0)
    list_1.insert_first(9)
    list_1.insert_first(2)
    list_1.insert_first(10)
    print(list_1)
    # Test method insert_last()
    print()
    print("Testing insert_last")
    list_1.insert_last(44)
    print(list_1)
    # Test method insert_in_order()
    print()
    print("Testing insert_in_order")
    list_2 = LinkedList()
    list_2.insert_last(1)
    list_2.insert_last(2)
    list_2.insert_last(3)
    list_2.insert_last(5)
    list_2.insert_last(6)
    print("List before inserting 4:", list_2)
    list_2.insert_in_order(4)
    print("List after insertion", list_2)
    # Test method get_num_links()
    print()
    print("Testing get_num_links")
    print("list_1 should return 12 and list_2 6")
    print("list_1: {a}, list_2: {b}".format(a = list_1.get_num_links(), b = list_2.get_num_links()))
    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print()
    print("Testing find_unordered")
    print("First case should return True, second None")
    print(list_1.find_unordered(10))
    print(list_1.find_unordered(55))
    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print()
    print("Testing find_ordered")
    print("First case should return True, second None")
    print(list_2.find_ordered(5))
    print(list_2.find_ordered(7))
    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print()
    print("Testing delete_link")
    print("First case should return 2, second None")
    print(list_1.delete_link(2))
    print(list_1.delete_link(55))
    # Test method copy_list()
    print()
    print("Testing copy_list")
    print("Both lists should be equivalent")
    copy=list_1.copy_list()
    print(list_1)
    print(copy)
    # Test method reverse_list()
    print()
    print("Testing reverse_list")
    print(list_1)
    reverse=list_1.reverse_list()
    print(reverse)
    # Test method sort_list()
    print()
    print("Testing sort_list")
    print("Second list should be sorted")
    r=list_1.sort_list()
    print(list_1)
    print(r)
    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print()
    print("Testing is_sorted")
    print("First case should return True, second False")
    print(list_1, list_1.is_sorted())
    print(list_2, list_2.is_sorted())
    # Test method is_empty()
    print()
    print("Testing is_empty")
    print("First case should return True, second False")
    t=LinkedList()
    print(t, t.is_empty())
    print(list_2, list_2.is_empty())
    # Test method merge_list()
    print()
    print("Testing merge_list")
    print(r)
    print(list_2)
    print("Merged:", r.merge_list(list_2))
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print()
    print("Testing is_equal")
    print("First case should return True, second False")
    print("list_1, list_1.copy_list():", list_1.is_equal(copy))
    print("list_1, list_2", list_1.is_equal(list_2))
    # Test remove_duplicates()
    print()
    print("Testing remove_duplicates")
    list_1.insert_last(8)
    list_1.insert_last(4)
    list_1.insert_last(9)
    list_1.insert_last(2)
    print(list_1)
    print("Without duplicates:", list_1.remove_duplicates())

if __name__ == "__main__":
    main()