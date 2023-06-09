#Hello World!
'''
print method displays the text given in the console
by default an argument end is set to '\n'
Multiple print() statements would display each content in subsequent lines
'''
print("Hello world!")
print("Hello world!")

#We can use \n or \t to add whitespaces in text
print("\n")

#Variables

print("Variables")

a = 3 #integer variable
b = 10 #integer variable
k = True
d = 1.234 #floating point variable
e = [1,2,3,4,5,6,7,8] #list
i = [True, False, 1,2,3,4,5.444234, 'c',[1,2,a],"1231ASD!@#"]
f = [0]*10  #list as [0,0,0,0,0,0,0,0,0,0]
g = ['a']*10 #list as ['a','a','a','a','a','a','a','a','a','a']
h = "Hello World!" #string valiable
dictionary = {"key1":2,3:'c',5:1.123,6:"Jerry"}
tuple_1 = (1,2,3.14,"hello",'c')
set_1 = set([1,1,2,3,4,4,4,5,6])

print("Value of a: ",a)
print("Value of b: ",b)
print("Value of d: ",d)
print("Value of e: ",e)
print("Value of f: ",f)
print("Value of g: ",g)
print("Value of h: ",h)
print("Value of i: ",i)
print("Value of k: ",k)
print("Value of dictionary: ",dictionary)
print("Value of tuple_1: ",tuple_1)
print("Value of set_1: ",set_1)

print("\n")

#________________________________________________________________________________________________________

#math operators
print("Math Opertor")

print("SUM of a and b: ",a+b)
print("Product of a and b: ",a*b)

'''
Normal division will result in float class
10/3 becomes 3.333333333335
This is due to runtime class assignmet or we can say python is dynamically typed
'''
print("Division of a by b: ",a/b)
print("Division of b by a: ",b/a)
print("a Integer division by b: ",a//b)
print("b integer Division by a: ",b//a)

c = a - b
print("Value of c: ",c)
print("\n")

#________________________________________________________________________________________________________

#bitwise operators
'''
1. Convert any value into bit in binary.
2. Perform logical operation on individual bits by position
'''
print("Bitwise Opertors")

#bitwise and operation
'''
a = 3, in binary form a is 011
b = 10, in binary form b in 1010
Bitwise AND would result in 0011 & 1010 -> 0010
result of a&b is 2
'''
print("a AND b: ",a & b) 

#bitwise or operation
'''
a = 3, in binary form a is 011
b = 10, in binary form b in 1010
Bitwise OR would result in 0011 | 1010 -> 1011
result of a|b is 11
'''
print ("a OR b: ",a | b)

# bitwise Negate
'''
a = 3 in biinary form is 00000011 (in 8 bit representation)
Negate operation complements each bit
Negate of a is 11111100, which is 2's complement repreesentation
Result of ~a is -4
'''
print("NOT a: ",~a)

#bitwise and operation
'''
a = 3, in binary form a is  0011
b = 10, in binary form b in 1010
a bitwise XOR would result in 0011 & 1010 -> 1001
result of a^b is 9
'''
print("a XOR b: ",a^b)

#shifting
'''
a = 3, in binary form a is  0011
Right shift adds 0 to left most bit and ignore 0001
result of a>>1 is 1 (fundamentally it divides by 2)
'''
print("Right Shift 1: ",a>>1)
print("Right Shift 2: ",a>>2)

'''
b = 10, in binary form a is  1010
Right shift adds 0 to right most bit 10100
result of b<<1 is 20 (fundamentally it multiplies by 2)
'''
print("Left Shift 1: ",b<<1)
print("Left Shift 2: ",b<<2)

print("\n")

#________________________________________________________________________________________________________

#type operator
'''
type opereator return the Class which an object belongs to.
'''
print("Type Opertor")
print("Type of a: ",type(a))
print("Type of d: ",type(d))
print("Type of e: ",type(e))
print("Type of h: ",type(h))
print("Type of k: ",type(k))
print("Type of tuple: ",type(tuple_1))
print("Type of dict: ",type(dictionary))
print("Type of set: ",type(set_1))

print("\n")

#________________________________________________________________________________________________________

#List Operations

#Display the list
'''
Variable e is a list [1,2,3]
print function would display [1,2,3] on console
'''
print(e)

#Length
'''
Variable e is a list [1,2,3,4,5,6,7,8]
len() returns Length of the list
Result of len(e) is 8
'''
print("Length of e: ", len(e))

#maximum valued element in a list
print(max(e))

#minimum valued element in a list
print(min(e))

#sorting a list in ascending order
print(e.sort(reverse=False))

#sorting a list in descending order
print(e.sort(reverse=True))

#First element of list
print("First Element of e: ", e[0])

#last element of list
l = len(e)
print("Last Element of e: ",e[l-1])

#last element of list (-ve indexing)
print("Last  Element of e with negative index:", e[-1])
print("Element of e with negative index 2:", e[-2])
print("Element of e with negative index 3:", e[-3])
print("Element of e with negative index 4:", e[-4])
#print("Error ex_ out of bound:", e[8])

#slicing
'''
List in Python can have three params _list[start:end:index_jump]
'''
print("Elements of e from index 0 to until index 4: ", e[0:4])
print("Elements of e from index 0 to until index 8: ", e[0:8])
print("Elements of e from index 1 to until index 4: ", e[1:4])
print("Elements of e from index 2 to until index 5: ", e[2:5])

print("Elements of e from index 0 to until index 2 without start index: ", e[:2])
print("All Elements from index 0 till end: ", e[0:])
print("All Elements from index 0 till end: ", e[:])
print("All Elements from index 1 till end: ", e[1:])
print("All Elements from negative index 4 till end: ", e[-4:])
print("Last 6 Elements in the list: ", e[-6:])

#jumping
print("Alternative Elements of e from index 0 till end: ", e[::2]) 
print("Alternative Elements of e from index 1 till end: ", e[1::2]) 

#reversing
print("All Elements of e in reverse order", e[::-1])

#Append
'''
Given List e
Append method adds an element to the end of the list
'''
e.append(10)
print("List e after appending 10: ", e)

#Inserting an element in the List
e.insert(2,3232)
print("List e after inserting 3232 at index 2: ", e)

#Extending a list
newList = [111,222,333,444,555]
e.extend(newList)
print("List e after extending e with newList: ", e)

#Remove an element from the list
e.append(8)
e.remove(8)
print("List after remove:",e)

#Pop and element from the list
e.pop(-1)
print("List after pop:",e)

#Clearing a list
e.clear()
print("List e after clearing: ", e)

print("\n")
#________________________________________________________________________________________________________

#String Operations

#Display the string
'''
Variable h is a string "Hello World!"
print function would display "Hello World!" on console
'''
print(h)

#Length
'''
Variable h is a string "Hello World!"
len() returns Length of the list
Result of len(h) is 12
'''
print("Length of h: ", len(h))

#First element of string
print("First Character of h: ", h[0])

#last element of string
l = len(h)
print("Last Character of h: ",h[l-1])

#last element of list (-ve indexing)
print("Last Character of h with negative index:", h[-1])

#slicing
'''
String in Python can have three params _string[start:end:index_jump]
'''
print("Characters of h from index 0 to until index 4: ", h[0:4])
print("Characters of h from index 0 to until index 8: ", h[0:8])

print("Characters of h from index 0 to until index 2 without start index: ", h[:2])

print("All Characters from index 0 till end: ", h[0:])
print("All Characters from index 1 till end: ", h[1:])

#jumping
print("Alternative Characters of h from index 0 till end: ", h[::2]) 

#reversing
print("All Characters of h in reverse order", h[::-1])

str1 = "hi"
str2 = "GCEK"
str3 = str1 + " " + str2
print(str3*3)

print(g)
str4 = ''.join(g)
print(str4)
str4 = '-'.join(g)
print(str4)

print("\n")

#________________________________________________________________________________________________________
#Controll Statements
print("Control Statements")

#IF statement
if(True):
    print("The control is here!")

#if else statement (focus on if block)
if(a<10):
    print("Variable a is lesser than 10")
else:
    print("Variable a is greater than 10")

#if else statement (focus on else block)
if(a>10):
    print("Variable a is greater than 10")
else:
    print("Variable a is lesser than 10")

#if statement with equality check
if(d == 1):
    print("The value of d is satisfying the condition.")

print("\n")

#elif ladder
if(a==1):
    print("a is 1")
elif(a==3):
    print("a is 3")
elif(a==2):
    print("a is 2")
elif(a==4):
    print("a is 4")
else:
    print("a is not satisfying any conditions")


'''
Indentation as above should be consistent across the program file
Indentation is used to identify a code block.

if(condition):
    x = 2      #From this line, 'if' block starts
    print(x)
    x += 1
    return(x)  #At this line 'if' block ends.
x = 10 #this line is out of 'if' block

This same logic applicable for keywords: with, def, if, elif, else, while, for, try, except and so on.
'''

#________________________________________________________________________________________________________

#Loops
print("Control Loops")
print("\n")
print("Iteration with while loop")

#while loop
'''
The loop below is used to iterate from value 4 until 0.
'''
iterationVariable = 4
while(iterationVariable != 0):
    print("Iteration on while loop: ",iterationVariable)
    iterationVariable -= 1

print("\n")
print("Iteration with for loop on list f")

'''
The below code snippet iterates from 0 until length of the list f
It traverses through all index values.
For each index we fetch the element at the index in the list, and update its value.
'''
lengthE = len(f)
idx = 0
while(idx < lengthE):
    f[idx] += idx**2
    idx += 1
print("Result of array manipulation with While loop:", f)

print("\n")
print("Iteration with for loop")

#for loop
'''
The loop below is used to iterate from value 0 until 4.
Details of range method is mentioned later in the tutorial
'''
for i in range(0,4):
    print("Iteration on for loop: ",i)

print("\n")
print("Printing values in f iteratively using for loop")

'''
The below code traverses througheach element of the list.
Unlike while, we can access the elements of the list without using the index explicitly.
'''
for i in f:
    print(i, end=' ')

print("\n")


#________________________________________________________________________________________________________
#User Defined Functions

print("User defined functions")

#simple method for addition, takes two parameters, returns the sum of the two numbers
def add(a,b):
    return(a+b)

#simple method for subtraction, takes two parameters, returns the difference of the two numbers
def diff(a,b):
    c = a-b
    return(c)

'''
Method to determine the sum of elements of the list
Takes a list as argument, returns an integer as sum of list elements
Please observe the nested indentation after the for loop here.
'''
def arraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return(sum)

#Calling the methods
print("Result of add function call:",add(1,2))
print("Result of diff function call:", diff(1123123,123121))
print("Result of arraySum function call:", arraySum(f))

print("\n")

#___________________________________________________________________________________________________________
#Misc

print("range method")

'''
Range is a built-in method that returns a range object
upon unpacking with * prefix, it contains a list of values
Range is a methos with polymorphism implemented.
In simple words range can be used in 3 different ways as follows:
    <0>Range(end)
    <1>Range(start,end)
    <2>Range(start,end,jump)
'''
print("Range with value 10: ",*range(10))
print("Range from 0 to 10: ",*range(0,10))
print("Range from 0 to 10 with jump  2: ",*range(0,10,2))
print("Range from 10 to 0 with jump -1: ",*range(10,0,-1))
print("Range from 10 to 0 with jump -2: ",*range(10,0,-2))

print("List comprehension")
'''
List comprehension is a method of creating a list with a syntax
[ result_variable for result_variable in Iterable]
'''
x = [i for i in range(0,10)]
print("Value of x on list comprehension:",x)

y = [i for i in range(5,10)]
print("Value of y on list comprehension:",y)

z = [i for i in range(0,20,3)]
print("Value of z on list comprehension:",z)

w = [i for i in range(20,0,-1)]
print("Value of w on list comprehension:",w)

print("\n")

#___________________________________________________________________________________________________________

#Problems to use the above learnings

'''
Write a program to print lower triangular matrix of size NxN filled with '*'.
Example 0: N = 1
Output  0: 
*

Example 1: N = 4
Output  1: 
*
**
***
****
'''
n = int(input())
for i in range(1,n+1):
    print(''.join(['*']*i))


'''
Write a program to print minimum value in the list without using built-in methods.
Example 0: N = [3,1,3,5,3,2,5,6,-1,0]
Output  0: -1

Example 1: N = [0, 10, 20, 30, 40, 51, 60, 90]
Output  1: 0
'''
arr = list(map(int,input().rstrip().split(' ')))
minVal = arr[0]
for i in arr:
    if(minVal>i):
        minVal = i
print(minVal)

'''
Write a program to print total count of vowels in a givem string.
Example 0: N = "Hello World!"
Output  0: 3

Example 1: N = "abecidolu"
Output  1: 5
'''
inputStr = input()
count = 0
for i in list(inputStr):
    if (i == 'a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count += 1
print(count)
print("\n")
s = "hello world!"
print(list(s))


