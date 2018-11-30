#  File: BabyNames.py

#  Description: Make a menu that displays data about baby names

#  Student Name: Daniel Espinoza

#  Student UT EID:  dee467

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/14/2018

#  Date Last Modified: 9/14/2018

def Enter1(dict):
    try:
# Make a list of the decades
        decades=["1900" ,"1910", "1920", "1930","1940","1950","1960", "1970", "1980","1990","2000" ]
# Input check
        name = str(input("Enter a name:"))
# get the sorted ranking in order from highest to lowest ie 0-1001
        ord_rank=sorted(dict[name])
#get where the index of the highest value is at
        idx=0
        for x in dict[name]:
            if x ==ord_rank[0]:
               break
            idx+=1
#print statements
        print()
        print("The matches with their highest ranking decade are:")
        print(name +" "+ decades[idx])
        print()
    except:
# if anything fails the code will not stop but just
#  report that there is nothing there
        print()
        print(name + " does not appear in any decade.")
        print()
def Enter2(dict):
    try:
# list of years
        decades=["1900" ,"1910", "1920", "1930","1940","1950","1960", "1970", "1980","1990","2000" ]
#input check
        name = str(input("Enter a name:"))
# list made from the name's values
        ranks=dict[name]
        print()
# print the list with the name and ranks
        print(name+": ", end='')
        for x in range(len(ranks)):
            if x==len(ranks)-1:
                print(str(ranks[x]))
                break
# will continue on the same line as long as it is not last
            print(str(ranks[x]),end=' ')
# prints the year with rank
        for x in range(len(ranks)):
            print((decades[x])+": "+ str(ranks[x]))
        print()
# incase something fails
    except:
        print()
        print(name + " does not appear in any decade.")
        print()
def Enter3(dict):
      try:
# list of decades and input check
        print()
        decades = ["1900", "1910", "1920", "1930", "1940", "1950", "1960", "1970", "1980", "1990", "2000"]
        decade=input("Enter decade: ")
# find where in the list the input is
        idx=0
        for x in decades:

            if x ==decade:
                break;
            idx += 1

# name_rank will be a 2-D list
# empty list that will be fill with ranks
        name_rank=[]
        ranks=[]
# go through all the list values
        for x in dict.keys():
            temp=dict[x]
# if unranked , ignore, else append the rank
# to the rank list, append the name and rank to the 2-D list [name, rank]
            if temp[idx]!=1001:
                ranks.append(temp[idx])
                inner=[x,temp[idx]]
                name_rank.append(inner)
# sort the ranks list
        ranks=sorted(ranks)
# find corresponing ranks as we go down the list, printing only if it is the
# right rank for the name
        for x in range(len(ranks)):
            for y in range(len(ranks)):
                temp=name_rank[y]
                if ranks[x]==temp[1]:

                    print(temp[0],": ", temp[1])
                    temp[1]=1001
        print()
      except:
# In case of failure
          print()
          print(decade + " is not an acceptable decade")
          print()
def Enter4(dict):
#storage for names that meet the prereqs
    names = []
#start a counter
    count=0
# go through all the keys
    for x in dict.keys():
# list of corresponding key value
        temp = dict[x]
# boolean flag
        flag=True
# If it is not in a decade ignore
        for y in temp:
            if y == 1001:
                flag=False
# else append it to the name
        if flag != False:
            names.append(x)
            count+=1
# sort the names by a-z
    name_rank=sorted(names)
    print(count," names appear in every decade. The names are:")
# print out the count and the names
    for x in name_rank:
        print(x)
    print ()

def Enter6(dict):
# start a counter
    count=0
    print()
# empty list for names
    names=[]
#go though every key
    for x in dict.keys():
#list of key values
        temp=dict[x]
        flag=True
# goes though the temp list of values and checks for descending order but checks
# if the value becames too unpopular and got unranked or stagnated
        for y in range(1,len(temp)):
            if temp[y]<temp[y-1] or temp[0]==1001 or temp[y]==1001 or temp[y]==temp[y-1]:
                flag=False
        if flag != False:
#else append the name
            names.append(x)
            count += 1
#sort the names by a-z
# print the count and names
    names = sorted(names)
    print(count, " names are less popular in every decade.")
    for x in names:
        print(x)
    print()
def Enter5(dict):
# start a counter
    count=0
    print()
#empty list for names
    names=[]
#iterate though keys
    for x in dict.keys():
        temp=dict[x]
#boolean flag
        flag=True
# goes though the temp list of values and checks for ascending order but checks
# if the value was ever unranked or stagnated
        for y in range(1,len(temp)):
            if temp[y] > temp[y - 1] or temp[0] == 1001 or temp[y] == 1001 or temp[y] == temp[y - 1]:
                flag=False
        if flag != False:
# else add it to the list
            names.append(x)
            count += 1
# reorder the names a-z
    names = sorted(names)
#printthecount and names
    print(count, " names are more popular in every decade.")
    for x in names:
        print(x)
    print()
def menu():
# create the menu
    print("Enter 1 to search for names.")
    print("Enter 2 to display data for one name")
    print("Enter 3 to display all names that appear in only one decade.")
    print("Enter 4 to display all names that appear in all decades.")
    print("Enter 5 to display all names that are more popular in every decade.")
    print("Enter 6 to display all names that are less popular in every decade.")
    print("Enter 7 to quit.")
    print ()
def main():
#read in the name.txt file
    in_file = open("./name.txt", "r")
#create an empty dict
    dict={}
# go though each line and split the info into a list
    for line in in_file:
        temp_list=line.split()
        rank=[]
# get only the numbers by passing over the first index and putting the rest a list to use as values
        for x in range((len(temp_list)-1)):
            if int(temp_list[x+1])==0:
                temp_list[x+1]=1001
            rank.append(int(temp_list[x+1]))
# the key is the first indexed value; name,  rest are the rankings
        dict[temp_list[0]]=rank
# will continue to loop no matter what
    while(True):
# print the menu
        menu()
#input check choice
        user_in = int(input("Enter choice: "))
# execute corresponding functions
        if user_in == 1 :
            Enter1(dict)
        elif user_in == 2 :
            Enter2(dict)
        elif user_in == 3 :
            Enter3(dict)
        elif user_in == 4 :
            Enter4(dict)
        elif user_in == 5 :
            Enter5(dict)
        elif user_in == 6:
            Enter6(dict)
# if the value exceeds or is 7 it will exit
        elif user_in >= 7 :
            print()
            print("Goodbye.")
            print()
            break

if __name__ == '__main__':
    main()