# -*- coding: utf-8 -*-
"""01ex_introduction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WOjLUjj1LOc-46D3bYP46CUhOWO2q6iN
"""



"""ex 1"""

for i in range(101):
  if i%15==0:
    print('HelloWorld') 
    continue 
  if i%3==0:
    print('Hello')
    continue
  if i%5==0:
    print('world')
    continue
   
  print(i)

"""ex 2"""

s=input("enter 1")
w=input("enter 2")
print(s,w)
s,w=w,s
print(s,w)

"""ex 3"""

import math
def ptzl():
  listptzl=[]
  x=int(input("first"))
  listptzl.append(x)
  y=int(input("second"))
  listptzl.append(y)
  z=int(input("third"))
  listptzl.append(z)
  v=int(input("fourth"))
  listptzl.append(v)
  print(listptzl)

  print(listptzl[1])
  plz=listptzl[0]-listptzl[2]
  als=listptzl[1]-listptzl[3]
  q=plz**2
  l=als**2
  e=math.sqrt(q+l)
  print(e)

ptzl()

"""ex 4"""

def listcount():
  letter=input("input your letter")
  text=input("input your text")
  u=0
  for p in text:
    if p==letter:
      u=u+1
  print(u)

listcount()

"""ex 7 a"""

m4=[1,2,3,4,5,6,7,8,9,10]
l1=[]
def calculate():
  for p in m4:
    l1.append(p**3)
  print(l1)

calculate()

"""ex 7 b"""

newlist = [x**3 for x in m4 ]
print(newlist)

"""ex 8"""

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

n = [(a,b) for a in range(3) for b in range(4) ]
print(n)

"""ex9

"""

def mm ():
  a=input("inter a")
  b=input("inter b")
  c=input("inter c")

def fisa():
  mylist=[]
  count=0
  term=2
  while count < 100 :
        for n in range(1, term) :
            a = term * term - n * n
            b = 2 * term * n
            count = term * term + n * n
            if count > 100 :
                break
            mylist.append((a,b,count))
        term = term + 1
  return(tuple(mylist))
fisa()



"""ex 10

"""

def normaliaze():
  num=int(input('enter the vector length'))
  i=0
  t=0
  m1=[]
  m2=[]
  m3=[]
  while i<num:
    n=int(input('enter the vextor '))
    m1.append(n)
    i+=1
  print(m1)
  for i in m1:
    m2.append(i**2)
  print(m2)
  for j in m2:
    t=t+j
  print(t)
  for u in m1:
    m3.append(u/t)
  print(tuple(m3))
normaliaze()

"""x10"""

count=0
x, y = 0, 1
while count < 20:
       print(x)
       t = x + y
       x = y
       y = t
       count += 1