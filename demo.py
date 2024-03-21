print("hello")

a = 5
print(a)
print(id(a))

Str = "Hello world"
print(Str)

#Rules to declare variable
#1.There should not be space in variable name
#2.Can not be number at the begining of the var name
#3.Python is case sensitive language: name is different variable, Name is different variable
#4.Special characters are not allowed in variable name

var1 = 100
var2 = 100
print("var1 address", id(var1))
print("var2 address", id(var2))
#If 2 variables having same value than there address will be same

p1 = 600
p2 = 200
print("add:", p1+p2)
print("sub:", p1-p2)
print("mul:", p1*p2)
print("div:", p1/p2)
print(p1==p2)  #compare 2 variable
#power operation
print("square of four", 4**2)

#(a+b)*2= a*2+ b*2+ 2ab
a = 40
b = 50
lhs = (a+b)**2
print("lhs:", lhs)

rhs = a**2 + b**2 + 2*a*b
print("rhs:", rhs)


b, c, d = 5, 5.5, "Pyhton"
print("{} {}".format("value is of", d))

print(type(d))

values = [1, 2, "pyhton", 4, 5]
print(values[0])  # 0
print(values[3])  # 3
print(values[-1])  # 5(to get the last value)
print(values[0:3])  # 1,2, python
print(values)  # [1, 2, "pyhton", 4, 5]
values.insert(4, "version")
print(values)

values.append("end")
print(values)

values[2] = "PYTHON"  # updating

del values[0]  # delete
print(values)

# Tuple - Same as list datatype but immutable where updation is not possible
# val = (1, 2, 3, 4.5, "tuple")
# print(val[1])
# val[2] = "tup"
# print(val) #Should get error

# Dictonary

dic = {"a": 2, 4: "bcd", "c": "value"}
print(dic[4])
print(dic["a"])

dict = {}

dict["first value"] = 1
dict["second value"] = "two"
print(dict)
print(dict["second value"])

#----If else
greeting = "Good morning"

if greeting == "Morning":
    print("Condition matches")
    print("second line")
else:
    print("condition does not match")
print("if else code completed")

#----For loop
obj = [2, 3, 5, 9]
for i in obj:
    print(i)
    print(i*2)

#sum of 5 natural numbers 1+2+3+4+5=15
summation = 0
for j in range(1,6): #range(i,j) -> i to j-1
    summation = summation + j
print(summation)

for k in range(1,10,2):
    print(k)

for m in range(10):
    print(m)

#while loop

it = 10
while it>1:
    if it == 9:
        it = it - 1
        continue
    if it ==2:
        break
    print(it)

    it = it - 1
print("while is done!")

#In python, functions is a set of statements that perform a specific task.


def GreetMe(name):
    print("Good morning " + name)
    #Function call


def AddInt(a,b):
    print(a+b)

GreetMe("Samiksh")
AddInt(2,3)


def AddInti(a,b):
    return(a+b)

print(AddInti(3,3))