#Hello World!
print("Hello world!")
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


print("Value of a: ",a)
print("Value of b: ",b)
print("Value of d: ",d)
print("Value of e: ",e)
print("Value of f: ",f)
print("Value of g: ",g)
print("Value of h: ",h)
print("Value of i: ",i)
print("Value of k: ",k)

print("\n")

#________________________________________________________________________________________________________

#math operators
print("Math Opertor")

print("SUM of a and b: ",a+b)
print("Product of a and b: ",a*b)
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
a bitwise AND would result in 0011 & 1010 -> 0010
result of a&b is 2
'''
print("a AND b: ",a & b) 

#bitwise or operation
'''
a = 3, in binary form a is 011
b = 10, in binary form b in 1010
a bitwise OR would result in 0011 & 1010 -> 1011
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
print("Right Shift 1: ",a>>1)
print("Right Shift 2: ",a>>2)

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
Variable e is a list [1,2,3]
len() returns Length of the list
Result of len(e) is 8
'''
print("Length of e: ", len(e))

#First element of list
print("First Element of e: ", e[0])

#last element of list
l = len(e)
print("Last Elelment of e: ",e[l-1])

#last element of list (-ve indexing)
print("Last  Element of e with negative index:", e[-1])

#slicing
'''
List in Python can have three params _list[start:end:index_jump]
'''
print("Elements of e from index 0 to until index 4: ", e[0:4])
print("Elements of e from index 0 to until index 8: ", e[0:8])

print("Elements of e from index 0 to until index 2 without start index: ", e[:2])

print("All Elelements from index 0 till end: ", e[0:])
print("All Elements from index 1 till end: ", e[1:])

#jumping
print("Alternative Elements of e from index 0 till end: ", e[::2]) 

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
print("List e after inserting 3232 at index 2: ", e)

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

#________________________________________________________________________________________________________

#Loops
print("Control Loops")
print("\n")
print("Iteration with while loop")
#while loop
iterationVariable = 4
while(iterationVariable != 0):
    print("Iteration on while loop: ",iterationVariable)
    iterationVariable -= 1

print("\n")
print("Iteration with for loop on list f")

lengthE = len(f)
idx = 0
while(idx < lengthE):
    f[idx] += idx
    idx += 1
print("Result of array manipulation with While loop:", f)

print("\n")
print("Iteration with for loop")

#for loop
for i in range(0,4):
    print("Iteration on for loop: ",i)

print("\n")
print("Printing values in f iteratively using for loop")

for i in f:
    print(i, end=' ')

print("\n")


#________________________________________________________________________________________________________

#User Defined Functions
print("User defined functions")

def add(a,b):
    return(a+b)

def diff(a,b):
    c = a-b
    return(c)

def arraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return(sum)

print("Result of add function call:",add(1,2))
print("Result of diff function call:", diff(1123123,123121))
print("Result of arraySum function call:", arraySum([i for i in range(10)]))

print("\n")


#___________________________________________________________________________________________________________
#Misc

print("Miscellaneous")

x = [i for i in range(0,10)]
print("Value of x on list comprehension:",x)

y = [i for i in range(5,10)]
print("Value of y on list comprehension:",y)

z = [i for i in range(0,20,3)]
print("Value of z on list comprehension:",z)

w = [i for i in range(20,0,-1)]
print("Value of w on list comprehension:",w)

print("\n")