from first.FirstClass import *
print(FirstClass.staticI)
a = FirstClass(religion="christian",name="obo",age=9)
a.toString()
a.setAttributes("lmao","lol","jk",67.98,True,not True)
a.printAttributes()
a.gh=9
print(a.gh)
print(a.staticI)
