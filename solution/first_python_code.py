'''
    Shiv's
    learning Python with previous OO coding experience (Java)
    referring https://www.youtube.com/watch?v=N4mEzFDjqtA  - 43mins
                                    install : 00:17
                                    Basics : 02:23
                                    Arithmetic : 04:21
                                    Strings : 05:54
                                    Lists / Arrays : 08:08
                                    Tuples : 12:24
                                    Dictionary : 13:37
                                    Conditionals : 15:46
                                    For Loop : 19:41
                                    While Loop : 21:57
                                    Functions : 24:59
                                    User Input : 26:34
                                    String Functions : 26:57
                                    File I/O : 30:11
                                    Classes / Objects : 32:04
                                    Constructors : 34:39
                                    Inheritance : 37:24
                                    Overwriting Functions : 37:58
                                    Overloading Functions : 39:47
                                    Polymorphism : 41:19﻿
    Also if you are using Pycharm the quick shortcuts
                    Shift+F10 to run,
                    Shift+Esc to close "Run" tab
'''

import random
import sys
import os


#simple printing to console (also, will explain above imports later)
print("**hello python world");

# noticed # above? '#" used for single line comment

'''
Also noticed (\''') multiline commenting
ok..!
'''

print("**************************************************************")
#print circus
print("**print circus")
#now to print " itsel, escape charecter concept
print('**showing double and single quotes acts same, wrt string and print')
print("**AS USUAL printing \' \" \' via \\\"  and same goes to printing\" \' \"")
print("**Hi \n" * 2)


print("**************************************************************")
#variables
print("\nplaying with variables")
name = "shiva";
age = 100
print("**name=", name)
print("**age=", age);
#also notice no semicolon needed and putting won't affect a thing
print("**Hello world, this is", name, "and my age is", age, ", kidding")
#ie print(variable, variable, variable)
print("**printing same via \%s and \%i as in C with little difference")
print("**Hello world, this is %s and my age is %i, kidding" % (name, age))
print("**Removing the default new line char at the end in \"print()\" using (end=\"\")- ", end="")
print("and testing")
name = age
print("**Weakly typed- after name = age, name = %s" % (name))

print("**************************************************************")
#strings
print("\nstrings and appending 2 strings using +")
multiLine_string = '''trying multiline strings and 
using this string to append new one '''
print("**multiLine_string=", multiLine_string)
stringToBeAppended = "-to be appended"
print("**multiLine_string + stringToBeAppended =", multiLine_string +
      stringToBeAppended)

print("**************************************************************")
#some spacial operataions that are not there in Java
print("\n**operations")
print("2 ** 4 = ", 2 ** 4) #prints 16
print("5 // 2 = ", 5 // 2) #prints 2
print("AS USUAL 5 / 2 =", 5 / 2) #as usual
print("AS USUAL 5 % 2 = ", 5 % 2) #as usual
age = age+2
print("AS USUAL age after adding 2=", age)
age = age/2;
print("AS USUAL age after dividing by 2=", age)
#simple add,divide, etc

print("**************************************************************")
#lets try list/arrays now
print('\narrays/lists')
array1 = [0,1,2,"three", 4]
#notice!? no flower brackets used as in Java
print("printing simple array, array=", array1)
print("**one more proof of weakly typed")
print("\nprinting subset, array1[1:3]=array1[0-in,ex]", array1[1:3])
array2 = [5, "six", 7, "eight"]
#lets see 2-D arrays
array2D = [array1, array2]
#note above array is list and hence need not be "completely rectangular"
print("\nAS USUAL 2-D array, array2D=\n", array2D)
print("\nAS USUAL printing 2nd row, array2D[1]=", array2D[1])
print("\nAS USUAL (R1,C2) = array2D[0][1]) = ", array2D[0][1])
print("\nAS USUAL (R1,C2) = array2D[1][3]) = ", array2D[1][3])
array2D.append("append1")
array2D.append("append2")
print("\nafter [array2D.append(append1) and append2]\n", array2D)
array2D.insert(1, "inserted")
print("\nafter [array2D.insert(1, \"inserted\")]\n", array2D)
array2D.remove("append1")
print("\nafter [array2D.remove(\"append1\")]\n", array2D)
del array2D[2]
array3 = ["d", "a", "f"];
print("\narray3", array3)
array3.sort()
print("\narray3.sort() = ", array3)
print("len(array2D)=", len(array2D))
print("len(array3)=", len(array3))
'''
print("max(array2D)", max(array2D))
this will create error, as it does not apply iteratively within
'''
print("min(array3)", max(array3))

print("**************************************************************")
print("\ntuples- list but content cannot be changed after created")
pi_tuple = (3, 1, 4, 1, 5, 9)
print("pi_tuple=", pi_tuple)
print("if you really want to change content, convert to list and then change")
list_tuple = list(pi_tuple)
list_tuple.append(11)
print("list_tuple after appending 11", list_tuple)
back_to_tuple = tuple(list_tuple)
print("back_to_tuple", back_to_tuple)
print("len(back_to_tuple)=", len(back_to_tuple))
print("min(back_to_tuple)=", min(back_to_tuple))


print("**************************************************************")
print("Dictionary/maps")
name_map = {
        "shiva": "d",
        "rajnish": "p",
        "sanj": "a"
}
print("name_map['rajnish']: ", name_map['rajnish'])
print("name_map['shiva']:", name_map['shiva'])
#debug later below delete not working
#del name_map['sanj']
print("after delete name_map['sanj']:", name_map['sanj'])

print("name_map.keys()-", name_map.keys())
print("name_map.values()-", name_map.values())

print("**************************************************************")
print("ifs/loops")
print("if else elif- keywords")
age = 21
if age > 16:
        print("good to drive as age > %i" % (age))
else:
        print("not old enough")

print("and or not - keywords")
if (1 ==1 and 2==2):
        print("from if: true 1==1 and 2==2")
if (1==1 and not(2==2)):
        print("true 1==1 and 2==2")
else:
        print("from else: false 1==1 and not(2==2)")

print("looping though number range")
for x in range(0, 10):
        print(x, end="")
print("\nfor x in [\"a\", \"b\", \"c\"]:")
for x in ["a", "b", "c"]:
        print(x, end="")

#parsing through matrix
matrix = [[1,2],[3,4],[5,6]]
for i in range(0, 3):
        print()
        for j in range(0,2):
                print(matrix[i][j], " ", end="")
print("while, break and continue work  the same")

print("**************************************************************")
print("\nfunctions")
def addNum(fnum, snum):
        sum = fnum + snum
        return sum
#now calling
print("addNum(2,3)=", addNum(2,3))

#reading from console/user
print("whats ur name = ")
name = sys.stdin.readline()
print("hello", name)

#done till 26.57

# self in python == this in Java

