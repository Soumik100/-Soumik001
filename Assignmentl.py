 #1(a)
from pickletools import string1


str='Python is a case sensitive language'
print(len(str))                  #len() function to give the length of string

#1(b)
rev=str[::-1]                    #to reverse the order of string
print(rev)

#1(c)
c=str[10:35]                    #Slicing
print(c)

#1(d)
obj=str.replace('a case sensitive language','object oriented')
print(obj)                      #Replace keyword

#1(e)
idx=str.index('a')              #indexing
print(idx)

#1(f)
spc=str.replace(' ','')         #replacing the strings
print(spc)

#2
str="Hey,{name} Here! My SID is 2110{SID},I am from {dep} department and my CGPA is {CGPA}"
print(str.format(name='Soumik Das',SID='7113',dep='Mechanical engineering',CGPA='8.0'))

#3(a)
a=56
b=10
g=a&b
h=bin(g)
i=h.replace('0b','')
print(i)

#3(b)
a=56
b=10
g=a|b
h=bin(g)
i=h.replace('0b','')
print(i)

#3(c)
a=56
b=10
g=a^b
h=bin(g)
i=h.replace('0b','')
print(i)

#3(d)
a=56
b=10
g=a<<2
h=bin(g)
i=h.replace('0b','')
print(i)

#3(e)
a=56
b=10
g=a>>2
h=bin(g)
j=a>>4
l=bin(j)
i=h.replace('0b','')
k=l.replace('0b','')
print(i,k)

#4
string1=input("Enter the string:")
if str in string1:
  print("Yes")
else:
  print("No")

#5
def check_traingle(a,b,c):
    result = 'Form a traingle'
    sides = [a, b, c]
    for side in sides:
        if side >= sum([sides[i] for i in range(len(sides)) if i != sides.index(side)]):
            result = 'Does not form a triangle'
            break
        return result
a=int(input("First side length :"))
b=int(input("Second side length :"))
c=int(input("Third side length:"))
print(a, b, c, check_traingle(a, b, c))

#6
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
n=a^b
count=0
while n:
 n=n&(n-1)
 count=count+1
count
print("Required number of bits to be flipped:",count)