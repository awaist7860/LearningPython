#importing libraries
import random


print("Hello World")

if 5 > 2:
    print("5 is greater than 2")
    print("This is a 1 indent")
if 10 > 5:
        print("10 is big")
        print("This is a 2 indent")

x = 20  #This is 20
y = "Hello World"   #this is hello world string

if x > 5:   #compares x to 5
      #this will be called is x is bigger than 5
      print("X = 20 and is bigger than 5")  
      print(y)


#Variables
#Variables are case sensative
#A and a are 2 different variables
#A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.
#declaring
a = 5
b = "Awais"
print(a)
print(b)


c = 4   #c is of type int
print(c)
c = "Tasleem"   #d is of type string
print(c)

#type casting

t = str(3)      #t will be '3'
h = int(3)      #h will be 3
q = float(3)    #q will be 3.0

print(t)
print(type(t))  #getting variable type
print(h)
print(type(h))  #getting variable type
print(q)
print(type(q))  #getting variable type

#single and double quotes "" or ''
#They both can be used

name1 = "Awais"
name2 = 'Tasleem'

print(name1 + ' ' + name2)

#Assigning multiple values to mutliple variables
w,e,r = "Oranges", "Banana", "Apple"

print(w)
print(e)
print(r)

#assigning 1 value to multiple variables
u = i = o = "Cherry"

print(u)
print(i)
print(o)

#unpacking a collection
fruit = ["Audi", "Volvo", "BMW"]

m,n,v = fruit

print(m)
print(n)
print(v)

#functions
#Globals variables

#p = "Global varibale Function/Method"

def myFunc():
      #print("This is a function and this is p is a varible from outside the function " + p)
      global p
      p = "Global variable"
      print(p)

myFunc()

print(p)


#Data types
"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

l = 1       #int
k = 2.8     #float
f = 1j      #complex
g = -87.7e10  #Scientific Notation
print(g)
print(f)

print(type(l))
print(type(k))
print(type(f))
print(type(g))



#Type conversion
#You can convert from one type to another with the int(), float(), and complex() methods

int1 = 1
float1 = 2.8
complex1 = 1j

#convert to float from int
conF = float(int1)
print(conF)
print(type(conF))

#convert int from float
conInt = int(float1)
print(conInt)
print(type(conInt))

#convert complex from int
conComplex = complex(int1)
print(conComplex)
print(type(conComplex))



#random numbers using random library
print(random.randrange(1, 100))


#type casting
"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

example

Integer
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

"""

#Python Strings
#Strings can be surronded by "" and ''

myFirstName = "Awais"
mySurname = 'Tasleem'

print("Double Quotes")
print('Single Quotes')
print("Double Quote Name - " + myFirstName + " Single Quote Name - " + mySurname)

#multiline strings
#you can use """ """ or ''' '''
multiLineString = """This is a multi line string 
It will be over 3 lines,
And it will be outputted into
the terminal"""

print(multiLineString)


#Strings are array of Chars
#getting a specific indexes data
#python is a 0 index language where arrays start at 0 instead of 1

indexString = "This is an string"

print(indexString[6])

##looping through a string
for x in 'Banana':
      print(x)

##getting the lenght of a string
print(len(multiLineString))

#checking if a string contains a value that you want
#returns a bool (true or false)

txt = "This is a check string to see if it can be searched"
print("see" in txt) #should return true

#using an if statments to check
if "see" in txt:
      print("the word see is in the text")

#checking if not

print("uidfi" not in txt)

if "osdigfhsaoi" not in txt:
      print("osdigfhsaoi is not in the text")

#slicing strings

"""
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
#txt[a:b]   - a = start of index    b = end of index
print(txt[3:24])    #slice from 3 to 24
print(txt[:24])     #slice from 0 to 24
print(txt[11:])     #slice from 11 to end
print(txt[-10:-3])     #Slice from backwards/opposite of forward slicing

#modifying strings
#Lower case
print(txt.lower())
#upper case
print(txt.upper())
#remove white spaces
print(txt.strip())  #gets rid of white spaces in front and behind of the string
#replace string
print(txt.replace("c" , "z"))
#split string
print(txt.split(","))


#Format string
"""
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

Example
Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
"""

age = 23
height = 5.8
info = "My name is awais and I am {} years old and i am {} feet tall"
print(info.format(age, height))

"""
You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

"""

#escape characters
"""
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."

To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."

"""

escapeTXT = "This is meant to be a \"escape\" clause"
print(escapeTXT)

#String methods
"""
Method	        Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

#Booleans
"""
Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

Example
print(10 > 9)
print(10 == 9)
print(10 < 9)
"""