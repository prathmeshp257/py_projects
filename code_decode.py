# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# f if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# Take input from the User
import random
import string
choice = 0
try:
    choice = int(input("Press 1 for Coding, 2 for Decoding & 0 to Quit & Press Enter: "))
except:
    print('Invalid Input')
if choice == 0: print("Program Terminated")
while choice == 1 or choice == 2:

    if choice == 1:
        # Take Input from User
        str1 = input("Enter any string to Encode: ")
        # Define newstr & list for further usage
        newstr = ''
        lst = []
        # First Encode the string
        # Append all chars in list
        if len(str1) > 2:
            '''# Brute force
            for i in str1:
                lst.append(i)
            # Now Append first element in the last & remove first element
            lst.insert(-1, lst[0])
            lst.pop(0)
            # Now Insert 3 random characters in first & last in the string using random method
            lst.insert(0, ''.join(random.choices(string.ascii_letters + string.digits, k=3)))
            lst.insert(len(lst), ''.join(random.choices(string.ascii_letters + string.digits, k=3)))
            # Now Join all list elements in newstr
            for i in lst:
                newstr += i'''
            str1 = str1[1:] + str1[0]
            str1 = ''.join(random.choices(string.ascii_letters + string.digits, k=3)) + str1 + ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            print(str1)
        else:
            # Here in this case reverse  the string
            for i in str1:
                newstr = i + newstr

        print(newstr)
        try:
            choice = int(input("Press 1 for Coding, 2 for Decoding & 0 to Quit & Press Enter: "))
        except:
            print('invalid input')
            break
        if choice == 0:
            print("Program Terminated")
            break


    elif choice == 2:
        # Take Input from the user
        str1 = input("Enter any string to decode: ")
        # Define newstr empty string & empty list for further use
        newstr = ''
        lst = []
        # for string size less than 3 reverse the string
        if len(str1) < 3:
            for i in str1:
                newstr = i + newstr

        else:
            '''# append all string elements in list
            for elem in str1:
                lst.append(elem)
            # splice the list for required indexes
            lst = lst[3:len(lst)-3]
            lst.insert(0, lst[-1])
            lst.pop()
            newstr = ''.join(lst)'''
            str1 = str1[3:len(str1)-3]
            str1 = str1[-1] + str1[:len(str1)-1]

        print(str1)
        try:
            choice = int(input("Press 1 for Coding, 2 for Decoding & 0 to Quit & Press Enter: "))
        except:
            print('invalid input')
            break
        if choice == 0:
            print("Program Terminated")
            break
