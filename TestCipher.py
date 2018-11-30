#  File: TestCipher.py

#  Description: Creates a

#  Student Name: Daniel Espinoza

#  Student UT EID: dee467

#  Course Name: CS 313E

#  Unique Number:51350

#  Date Created:9/9/2018

#  Date Last Modified:9/10/2018

#note ascii text : lowercase is from 97('a') to 122 ('z')
# takes a single string as input parameter and returns a string
def substitution_encode ( strng ):
# Making  a 26 length list of the unique cipher
  cipher=['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
# make an empty list to be amended
  string_sublist=[]
  for x in strng:
# Makes sure the letter are in lowercase and if not passover
    if ord(x)>=97 and ord(x)<=122 :
# get the index of the corresponding letter for the cipher
      idx=(ord(x)-ord('a'))%26
# add the ciphered letter to the empty list
      string_sublist.append(cipher[idx])
    else:
# adds it to the empty list if it passed
      string_sublist.append(x)
# returns string of joined substitute list
  return (''.join(string_sublist))
# takes a single string as input parameter and returns a string
def substitution_decode ( strng ):
# cipher list
  cipher=['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'y', 'h', 'n', 'u', 'j', 'm', 'i', 'k', 'o', 'l', 'p']
# a-z list of elements to decipher
  decipher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# empty list
  string_sublist = []
  for x in strng:
    idx=0
# makes sure it is lowercase
    if ord(x) >= 97 and ord(x) <= 122:
# stores the index of the location of where the current letter is in the cipher list
      for y in cipher:
        if x==y :
         break
        else:
          idx+=1
# adds it to the empty list
      string_sublist.append(decipher[idx])
    else:
      string_sublist.append(x)
# string of joined letters from substitute
  return (''.join(string_sublist))

# takes two strings as input parameter and returns a string
def vigenere_encode ( strng, passwd ):
# length of password
  len_pwd=len(passwd)
  counter=0
#empty string
  ret_str=""
  for x in strng:
# lowercase security
    if ord(x) >= 97 and ord(x) <= 122:
#makes sure the password repeats
      passidx=counter%len_pwd
#makes a number 0-25 or both password letter and string letter
      enc_pol=(ord(x))%97
      pass_pol=ord(passwd[passidx])%97
#makes it into a character
# gets the point where it land a-z then add 97 to make it into ascii
      enc_let=chr(((enc_pol+pass_pol)%26)+97)
# adds that letter to the string
      ret_str+=enc_let
# only goes to next password letter if it changes a letter
      counter+=1
    else:
# adds special characters
      ret_str+=x
  return ret_str

# takes two strings as input parameter and returns a string
def vigenere_decode ( strng, passwd ):
#almost the same as the encoder
  len_pwd = len(passwd)
  counter = 0
  ret_str = ""
  for x in strng:
    if ord(x) >= 97 and ord(x) <= 122:
      passidx = counter % len_pwd
      # makes a number 0-25
      enc_pol = (ord(x)) % 97
      pass_pol = ord(passwd[passidx]) % 97
      # makes it into a character
#only change, instead of add them we substract to get the value of where it was, the the mod should=+
# then we convert the value to a character
      enc_let = chr(((enc_pol - pass_pol) % 26) + 97)
      ret_str += enc_let
      counter += 1
    else:
      ret_str += x
  return ret_str

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()
  #read line to be encoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
  line = line.lower()
  # decode using substitution cipher

  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  #print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()
  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  line = line.lower()

  passwd = in_file.readline()
  passwd = passwd.strip()
  passwd = passwd.lower()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()