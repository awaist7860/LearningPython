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

v1 = 200
v2 = 33
v3 = "Hello"
v4 = 15

if v2 > v1:
      print("v2 is greater than v1")
else:
      print("v2 is not greater than v2")

#evaluating using bool()
"""
Most values are evaluated as True if it has some sort of content

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

print(bool("Hello"))
print(bool(15))

#evaluating using varibales
print(bool(v3))
print(bool(v4))

"""
Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(''))

"""
One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
"""

#Operators
"""
Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
Example
print(10 + 5)

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operatorsA


Operator Precedence
Operator precedence describes the order in which operations are performed.

Example
Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

Example
Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:

print(100 + 5 * 3)

Example
Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)

"""
print("Multiplication is highr presedence than addition")
print(100 + 5 * 3)

print("Addiditon and subtraction have the same precedence")
print(5 + 4 - 7 + 3)

#Python collections
"""
***Python Collections (Arrays)***
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
#python lists
"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

example
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

type()
From Python's perspective, lists are defined as objects with the data type 'list':

<class 'list'>

"""

myList = ["apple", "banana", "cherry"]
print(myList)

thisList = ["apple", "banana", "cherry", "apple", "cherry"]
print(thisList)

print(len(thisList))

list1 = ["apple", "banana", "cherry"]   #string list
list2 = [1, 5, 7, 9, 3]                 #int list
list3 = [True, False, False]            #boolean list

list4 = ["abc", 34, True, 40, "male"]   #list with a mix of data types - strings, ints, booleans

print(type(list4))


#making a list using the list() constructor
"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.

Example
Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""

createdList = list(("apple", "banana", "orange"))   #created list with double brakes for more than 1 item
print(createdList)

#access list items
print(thisList[3])

#negative indexing
print(thisList[-4]) #goes backwards adn starts from the last item in the lst

#list[a:b]- a = start of index    b = end of index
#a can be 0
#b can be 0
#returning from a range index
print(thisList[1:4])

print(thisList[:3])
print(thisList[2:])
print(thisList[-5:-1])

#checking if items exist in a list
if "cherry" in thisList:
      print("Cherry exists")


#changing values in a list
thisList[2] = "Mango"
print(thisList)

#chnaging a range of items
thisList[3:5] = ["kiwi", "pear"]
print(thisList)

if "cherry" in thisList:
      print("Cherry exists")
else:
      print("Cherry does not exist")

#Inserting an item to a list
"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
"""

thisList.insert(1, "Watermelon")
print(thisList)

#Adding list items
#using the Append() method
"""
Append Items
To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
"""

thisList.append("Orange")
print(thisList)

#Extending a list
"""
Extend List
To append elements from another list to the current list, use the extend() method.

Example
Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"""

newList  = ["Mango", "Passion Fruit", "Cocunut"]
moreFruits = ["Pineapple", "Pomegranate", "Dragon Fruit"]
print(newList)
newList.extend(moreFruits)
print(newList)

#add any iterable to the list by using extend
thisTuple = ("Kiwi", "Orange", "Apple")
print(thisTuple)
newList.extend(thisTuple)
print(newList)


#Removing items using the remove() method
newList.remove("Apple")
print(newList)

#removing the last item in the list with the pop() method
newList.pop()
print(newList)

#pop(x) removes the specified index
newList.pop(2)

#the del(x) keyword removes the specified index value
del newList[3]
print(newList)

#the del keyword can fully delete a list
#del newList
#print(newList)

#the method clear() is used to empty a list of items
newList.clear()
print(newList)


#Loop lists
loopList = ["item1", "item2", "item3"]

#for loop
for x in loopList:
      print(x)

for i in range(len(loopList)):      #i will be 1 2 and 3
      print(loopList[i])

#while loop
iCount = 0

while iCount < len(loopList):
      print(loopList[iCount])
      iCount = iCount + 1

#uisng list comprehension
[print(xCount) for xCount in loopList]

"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

Example

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


****The Syntax****

newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.

***Condition***

The condition is like a filter that only accepts the items that valuate to True.
Example
Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

*The condition is optional and can be omitted:

Example
With no if statement:

newlist = [x for x in fruits]

***Iterable***
The iterable can be any iterable object, like a list, tuple, set etc.

Example
You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

Same example, but with a condition:

Example
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

***Expression***
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

Example
Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

You can set the outcome to whatever you like:

Example
Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]

The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Example
Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

The expression in the example above says:

"Return the item if it is not banana, if it is banana return orange".

"""

#List comprehension
compList1 = ["mango", "apple", "banana", "kiwi", "cherry"]
newCompList = [x.upper() for x in compList1 if "a" in x]
numList = [25, 35, 986, 1, 3654, 2578, 2, 10, 458, 20, 98547, 365478214, 12, 1005, 6584]

print(newCompList)

#sorting a list
#alphanumerically
#use sort() method

print(compList1)
compList1.sort()
print(compList1)

print(numList)
numList.sort()
print(numList)

#sorting descending
compList1.sort(reverse=True)
print(compList1)

numList.sort(reverse=True)
print(numList)

#customizing sort function
#method for seeing how close a number is to 500
def myFunc1(n):
      return abs(n - 500)

numList.sort(key=myFunc1)
print(numList)

#Case Insensitive Sort
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

caseList = ["banana", "Orange", "Kiwi", "cherry"]
caseList.sort()   #this will sort uper case first then lower case
print(caseList)

caseList.sort(key=str.lower)  #this will ignore the case
print(caseList)

#reverse the order of a list
#this will just flip the list
caseList.reverse()
print(caseList)

#Copying lists
"""
Copy a List

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
"""
numListNew = [25, 35, 986, 1, 3654, 2578, 2, 10, 458, 20, 98547, 365478214, 12, 1005, 6584]
copyNumListNew = numListNew.copy()  #Using copy method
copyNumListNew2 = list(numListNew)  #using the built in method from the list library

print(copyNumListNew)
print(copyNumListNew2)

#Joining lists
#Using the + operator
joinedList1 = copyNumListNew + copyNumListNew2
print(joinedList1)
joinedList1.sort()
print(joinedList1)

for x in copyNumListNew2:
      joinedList1.append(x)

print(joinedList1)

#useing extend method
joinedList1.extend(copyNumListNew2)
print(joinedList1)

"""
***List Methods***

Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""

#Python Tuples
"""
***Tuple***

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""
#creating a tuple
firstTuple = ("apples", "bananas", "cherrys")
print(firstTuple)

"""
***Tuple Items***
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

***Ordered***
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

***Unchangeable***
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

***Allow Duplicates***
Since tuples are indexed, they can have items with the same value:

Example
Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
"""

#Duplicate values
dupTuple = ("apple", "banana", "cherry", "apple", "cherry" , "banana")
print(dupTuple)

"""
***Create Tuple With One Item***
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

Example
One item tuple, remember the comma:

thistuple = ("apple",)  #remember the comma
print(type(thistuple))

***#NOT a tuple***
thistuple = ("apple")
print(type(thistuple))
"""

singleTuple = ("Apple",)
print(singleTuple)

"""
***The tuple() Constructor***
It is also possible to use the tuple() constructor to make a tuple.

Example
Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
"""

#Access Tuple Items
"""
***Access Tuple Items***
You can access tuple items by referring to the index number, inside square brackets:

ExampleGet 
Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
"""

print(dupTuple[2])

#Tuples and lists have the same way to access

#Python - Update Tuples

#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
#But there are some workarounds.

"""
***Change Tuple Values***
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example
Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

"""

#Creating a tuple
toBeChangedTuple = ("apple", "banana", "cherry")
print(toBeChangedTuple)

#converting the tuple into a list
convertedFromTuple = list(toBeChangedTuple)
convertedFromTuple[1] = "kiwi"
convertedFromTuple.append("orange")

#converting back to tuple
toBeChangedTuple = tuple(convertedFromTuple)
print(toBeChangedTuple)


#Remember to convert to list, then use the list method to modify the tuple, then convert back

#Python - Unpack Tuples

"""
Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Example
Packing a tuple:

fruits = ("apple", "banana", "cherry")

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example
Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
"""
#Auto assigning each calue in the tuple to a varibale name
toBeVar = ("apple", "banana", "cherry")
print(toBeVar)

(green, yellow, red) = toBeVar

print(green)
print(yellow)
print(red)

print("new list after this")

#Now a longer list then variables

toBeVar1 = ("apple", "banana", "cherry", "kiwi", "cherry", "pineapple", "peach", "pear", "apricot")

(orange, blue, white, *pink) = toBeVar1   #the asteris * will convert the items after adn including into a list
print(orange)
print(blue)
print(white)
print(pink)

print("Asterisk * 2")
(orange, *blue, white, pink) = toBeVar1   #the asteris * will convert the items after and including into a list until the remaining mathces the variable left to be assigned in this cae 2

print(orange)
print(blue)
print(white)
print(pink)

#Looping a tuple is same as looping through list
#Joining tuples is same as joining lists

#Multiplying tuples

"""
***Multiply Tuples***
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

Example
Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
"""
toBeVar2 = ("apple", "banana", "cherry", "kiwi", "cherry", "pineapple", "peach", "pear", "apricot")

multiplyTuple = toBeVar2 * 2

print(multiplyTuple)

#Python Sets
#example
#myset = {"apple", "banana", "cherry"}

"""
***Set***
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

Example
Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

Note: Sets are unordered, so you cannot be sure in which order the items will appear.

***Set Items***
Set items are unordered, unchangeable, and do not allow duplicate values.

***Unordered***
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

***Unchangeable***+
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

***Duplicates Not Allowed***
Sets cannot have two items with the same value.

Example
Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

***Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:***

Example
True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

***Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:***

Example
False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

***Get the Length of a Set***
To determine how many items a set has, use the len() function.

Example
Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

"""

#getting legth with duplicates in the set
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)    #shows items in set

print(len(thisset))     #this shows the items in a set, this shows 3 even though there are 4 items in thisset, but it has duplicates adn is counted as 1


"""
***Set Items - Data Types***
Set items can be of any data type:

Example
String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

A set can contain different data types:

Example
A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}

***type()***
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>
Example
What is the data type of a set?

myset = {"apple", "banana", "cherry"}
print(type(myset))

***The set() Constructor***
It is also possible to use the set() constructor to make a set.

Example
Using the set() constructor to make a set:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""

#Accesiing Set Items
"""
***Access Items***
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

Example
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
"""

#looping through a set using a for loop

for x in thisset:
      print(x)    #loops through the items in thisset

#checing using the in command

print("apple" in thisset)     #returns true

"""
***Change Items***
Once a set is created, you cannot change its items, but you can add new items.
"""

#Add Set Items
"""
***Add Items***
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.

Example
Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

"""

#adding an item to thisset
thisset.add("oranges")
print(thisset)

"""
***Add Sets***
To add items from another set into the current set, use the update() method.

Example
Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
"""

#updating a set with another set

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)      #adding all items from tropical set to thisset

print(thisset)

"""
***Add Any Iterable***
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

Example
Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
"""

thisset.update(thisList)      #adding all items from thisList(List type) to thisset
print(thisset)


#Remvoing an item
"""
emove Item
To remove an item in a set, use the remove(), or the discard() method.

Example
Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

***Note: If the item to remove does not exist, remove() will raise an error.***

Example
Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

***Note: If the item to remove does not exist, discard() will NOT raise an error.***

***pop()*** (Not really recommended)
You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

Example
Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

***Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.***

***clear()***
Example
The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

***del (keyword)***
Example
The del keyword will delete the set completely:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

"""

#loop sets
"""
***Loop Items***
You can loop through the set items by using a for loop:

Example
Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
"""
#looping through a set using a for loop

for x in thisset:
      print(x)    #loops through the items in thisset


#Join Sets
"""
***Join Two Sets***
There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

Example
The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

***Note: Both union() and update() will exclude any duplicate items.***
"""

#Unions() for a new set
#update() to add another set to an already existing one

"""
***Keep ONLY the Duplicates***
The intersection_update() method will keep only the items that are present in both sets.

Example
Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

The intersection() method will return a new set, that only contains the items that are present in both sets.

Example
Return a set that contains the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
"""

#keeping only duplicates
#intersection_update()
setx = {"apple", "banana", "cherry"}
sety = {"google", "microsoft", "apple"}

setx.intersection_update(sety)

print(setx)

#intersection()

setz = setx.intersection(sety)
print(setz)

"""
***Keep All, But NOT the Duplicates***
The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

Example
Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

Example
Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

***Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:***

Example
True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
"""

setx2 = {"apple", "banana", "cherry"}
sety2 = {"google", "microsoft", "apple"}

#Discarding duplicates

#symmetric_difference_update
setx2.symmetric_difference_update(sety2)
print(setx2)

setx3 = {"apple", "banana", "cherry"}
sety3 = {"google", "microsoft", "apple"}

#symmetric_difference
setz3 = setx3.symmetric_difference(sety3)
print(setz3)

"""
***Set Methods***

Set Methods
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""

#Python Dictionaries
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
"""
#Dictionary

"""
***Dictionary***
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

Example

Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

"""
#example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

"""
***Dictionary Items***
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

Example
Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
"""

#exmaple of using a key
print(thisdict["model"])

"""
***Ordered or Unordered?***
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

***Changeable***
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

***Duplicates Not Allowed***
Dictionaries cannot have two items with the same key:

Example
Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


***Dictionary Length***
To determine how many items a dictionary has, use the len() function:

Example
Print the number of items in the dictionary:

print(len(thisdict))

"""

#getting length of dictionary
print(len(thisdict))

"""
***Dictionary Items - Data Types***
The values in dictionary items can be of any data type:

Example
String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

***type()***
From Python's perspective, dictionaries are defined as objects with the data type 'dict':

<class 'dict'>
Example
Print the data type of a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

"""

print(type(thisdict))

"""
***The dict() Constructor***
It is also possible to use the dict() constructor to make a dictionary.

Example
Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

"""

#Accessing Dictionary Items
"""
***Accessing Items***
You can access the items of a dictionary by referring to its key name, inside square brackets:

Example
Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
"""

print(thisdict["brand"])

"""
There is also a method called get() that will give you the same result:

Example
Get the value of the "model" key:

x = thisdict.get("model")
"""

#using the get() method
discX = thisdict.get("year")
print(discX)

#Getting the Keys
#The keys() method will return a list of all the keys in the dictionary.

#Example
keyX = thisdict.keys()
print(keyX)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

"""
Example
Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
"""


#Getting Values
#The values() method will return a list of all the values in the dictionary.

valX = thisdict.values()
print(valX)

"""
***Example 1***
Make a change in the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

***Example 2***
Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
"""

"Get Items"

"""
The items() method will return each item in a dictionary, as tuples in a list.

Example
Get a list of the key:value pairs

x = thisdict.items()

"""
print("Getting items using items()")
print(thisdict.items())

"Checking if a key exist in the dictionary"

if "model" in thisdict:
      print("Yes, the model is in the dictionary")

"""
Python - Change Dictionary Items

Change Values
You can change the value of a specific item by referring to its key name:

Example

Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
"""

thisdict["year"] = 2008

print(thisdict.items())
print(thisdict["year"])

"""

Update Dictionary
The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.

Example
Update the "year" of the car by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

"""

thisdict.update({"model": "GT"})
print(thisdict["model"])


"""
Python - Add Dictionary Items

Adding Items
Adding an item to the dictionary is done by using a new index key and assigning a value to it:

Example

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
"""

thisdict["size"] = "5.0L"
print(thisdict["size"])

"""

Python - Remove Dictionary Items

Removing Items
There are several methods to remove items from a dictionary:

Example 1

The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

Example 2

The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

Example 3

The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

***The del keyword can also delete the dictionary completely:***

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

Example 4

The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

"""

"""
Python - Loop Dictionaries

Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

Example

Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

"""

for x in thisdict:
      print(x)

"""
Example
Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
"""

for x in thisdict:
      print(thisdict[x])


"""
Example
You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
"""
print("thisDict.values()")

for x in thisdict.values():
      print(x)


"""
Example
You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)
"""

print("thisDict.keys()")

for x in thisdict.keys():
      print(x)

"""
Example
Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

"""

print("thisDict.items()")

for x, y in thisdict.items():
      print(x, y)



"""
Python - Copy Dictionaries

Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().

Example

Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
"""


print("Copying dictionaries")
newDict = thisdict.copy()

for x,y in newDict.items():
      print(x, y)


"""
Another way to make a copy is to use the built-in function dict().

Example
Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
"""

print("Copying dictionaries")

newDict2 = dict(thisdict)

for x, y in newDict2.items():
      print(x, y)

"""
Python - Nested Dictionaries

Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

Example

Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

"""


nestDict1 = {
      "nest1" : {
            "name" : "emily",
            "year" : 2004
      },
      "nest2" : {
            "name" : "Toby",
            "year" : 2007
      },
      "nest3" : {
            "name" : "Linus",
            "year" : 2011
      }
}

"""
Or, if you want to add three dictionaries into a new dictionary:

Example
Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

"""

item1 = {
      "name" : "Emil",
      "year" : 2004
}

item2 = {
      "name" : "Toby",
      "year" : 2007
}

item3 = {
      "name" : "linus",
      "year" : 2011
}

bigItem = {
      "item1" : item1,
      "item2" : item2,
      "item3" : item3
}

print("nestDict1")
for x,y in nestDict1.items():
      print(x, y)

print("bigItem")
for x, y in bigItem.items():
      print(x, y)


"""
Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

Example
Print the name of child 2:

print(myfamily["child2"]["name"])
"""
print(nestDict1["nest2"]["name"])
 


"""
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""


"""
Python If ... Else


"""










"""
class myclass():
  def __len__(self):
    return 0
  
  def myFunc():
       return True

myobj = myclass()
print("This is another class")
print(bool(myobj))
print(bool(myFunc))

if myFunc():
     print("myFunc returned True")
else:
     print("myFunc returned False")

"""