#  File: PhoneBook.py

#  Description: Reads a text document containing contact information for several people.
#  Allows user to access, edit, and delete information contained.

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Partner Name: Mark Simmons

#  Partner UT EID: mjs5839

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 09/19/2018

#  Date Last Modified: 09/21/2018

class ContactInfo(object):
# constructor
    def __init__(self,name="",street="",city="",state="",\
                 zip="",country="",phone="",email=""):
        self.name=name
        self.street=street
        self.city=city
        self.state=state
        self.zip=zip
        self.country=country
        self.phone=phone
        self.email=email

# string representation of Contact Info
    def __str__(self):
        return (
        "Name- {n}\n\
        Street- {s}\n\
        City- {c}\n\
        State- {st}\n\
        Zip- {z}\n\
        Country- {cn}\n\
        Phone- {p}\n\
        Email- {e}".format(n = self.name, s = self.street, c = self.city, st =self.state,\
        z = self.zip, cn = self.country, p = self.phone, e = self.email))
# Define global dictionary to hold all the contact information
phone_book = {}

# This function adds the contact information of a new person in the
# dictionary
def add_person():
    # Prompt the user to enter the name of the new person
        inname = input("Enter name: ").strip()
    # Check if name exists in phone book. If it does print a message
    # to that effect and return
        if (inname in phone_book.keys()):
            print(inname, "already exists in the phone book.")
            return
        if (inname == ''): # Do nothing if no name given
            return
# Prompt the user to enter the required contact information
        instreet = input("Enter street: ")
        incity = input("Enter city: ")
        instate = input("Enter state: ")
        inzip = input("Enter zip: ")
        incountry = input("Enter country: ")
        inph = input("Enter phone: ")
        inmail=input("Enter email address: ")
  # Create the ContactInfo object
        contactObj = ContactInfo (inname, instreet, incity, instate, inzip, incountry, inph, inmail)
  # Add the name and the contact information to the phone dictionary
        phone_book[inname]=contactObj
  # Print message that the information was added successfully
        print(inname, "was added to the phonebook.")
        return inname

# This function deletes an existing person from the phone dictionary
def delete_person():
  # Prompt the user to enter the name of the person
    inname = input("Enter name: ")
  # If the name exists in phone book delete it.
  # Print message as to the action.
    if (inname in phone_book.keys()):
        del phone_book[inname]
        print(inname, "was deleted from the phone book.")
    elif (inname == ''):
        return
    else:
        print(inname, "does not exist in the phone book.")

# This function updates the information of an existing person
def update_person():
  # Prompt the user to enter the name of the person
  inname=input("Enter name: ")
  # Check if name exists in phone book. If it does prompt
  if (inname in phone_book.keys()):
  # the user to enter the required information.
  # Write a message as to the action
      instreet = input("Enter street: ")
      if instreet == '':
          instreet = phone_book[inname].street
      incity = input("Enter city: ")
      if incity == '':
          incity = phone_book[inname].city
      instate = input("Enter state: ")
      if instate == '':
          instate = phone_book[inname].state
      inzip = input("Enter zip: ")
      if inzip == '':
          inzip = phone_book[inname].zip
      incountry = input("Enter country: ")
      if incountry == '':
          incountry = phone_book[inname].country
      inph = input("Enter phone: ")
      if inph == '':
          inph = phone_book[inname].phone
      inmail = input("Enter email address: ")
      if inmail == '':
          inmail = phone_book[inname].email
      # Create the ContactInfo object
      contactObj = ContactInfo(inname, instreet, incity, instate, inzip, incountry, inph, inmail)
      phone_book[inname]=contactObj
  elif (inname == ''):
      return
  else:
      print(inname, "does not exist in the phone book.")

# This function prints the contact information of an existing person
def search_person():
  # Prompt the user to enter the name of the person
    inname=input("Enter name: ")
  # Check if name exists in phone book. If it does print the
  # information in a neat format.
    if (inname in phone_book.keys()):
      print(phone_book[inname])
    elif (inname == ''):
        return
    else:
        print(inname, "does not exist in the phone book.")

# This function open the file for writing and writes out the contents
# of the dictionary.
def save_quit():
  # Open file for writing
    in_file=open('./phone.txt',"w")
  # Iterate through the dictionary and write out the items in the file
    for x in phone_book.keys():
        in_file.write(phone_book[x].name + '\n')
        in_file.write(phone_book[x].street + '\n')
        in_file.write(phone_book[x].city + '\n')
        in_file.write(phone_book[x].state + '\n')
        in_file.write(phone_book[x].zip + '\n')
        in_file.write(phone_book[x].country + '\n')
        in_file.write(phone_book[x].phone + '\n')
        in_file.write(phone_book[x].email + '\n')
        in_file.write('\n')
    # Close file
    in_file.close()
  # Print  message
    print("Succesful Save")
# This function prints the menu, prompts the user for his/her selection
# and returns it.

def menu():
# This function opens the file for reading, reads the contact information
# for each person and adds it to the dictionary.

    print("1. Add a Person")

    print("2. Delete a Person")

    print("3. Search for a Person")

    print("4. Update Information on a Person")

    print("5. Quit")

    return input("Enter your selection: ")
def create_phone_book():
  # Open file for reading
  in_file = open ("./phone.txt", "r")

  # Read first line (name)
  line = in_file.readline()
  line = line.strip()

  # Loop through the entries for each person
  while (line != ""):
    name = line

    # Read street
    line = in_file.readline()
    line = line.strip()
    street=line
    # Read city
    line = in_file.readline()
    line = line.strip()
    city=line
    # Read state
    line = in_file.readline()
    line = line.strip()
    state= line
    # Read zip-code
    line = in_file.readline()
    line = line.strip()
    zip=line
    # Read country
    line = in_file.readline()
    line = line.strip()
    country=line
    # Read phone number
    line = in_file.readline()
    line = line.strip()
    phone=line
    # Read e-mail address
    line = in_file.readline()
    line = line.strip()
    email=line
    # Read blank line
    line = in_file.readline()
    line = line.strip()
    # Read first line of the next block of data
    line = in_file.readline()
    line = line.strip()

    # Create ContactInfo object
    contactinfo= ContactInfo(name,street,city,state,zip,country,phone,email)
    # Add to phone dictionary
    phone_book[name]=contactinfo
  # Close file
  in_file.close()
def main():
  # Read file and create phone book dictionary
  create_phone_book()

  # Print logo
  print("Phone Book")

  # Print menu and get selection
  # Process request, print menu and prompt again and again
  # until the user types 5 to quit.
  while True:
    key = menu().strip()
    if key == '1':
        add_person()
    elif key == '2':
        delete_person()
    elif key == '3':
        search_person()
    elif key == '4':
        update_person()
    else:
        break
  
  # Save, print goodbye message, quit
  save_quit()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

