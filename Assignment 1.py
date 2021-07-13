planets = {"earth", "mars", "jupiter"}

planets.add("saturn")

print(planets)

planets = {"earth", "mars", "jupiter"}

planets.clear()

print(planets)

planets = {"earth","mars","jupiter"}
x = planets.copy()

print(x)

x = {"earth", "mars", "jupiter"}
y = {"mars", "neptune", "plutp"}

z = x.difference(y)

print(z)


x = {"earth", "mars", "jupiter"}
y = {"mars", "mercury", "venus"}

x.difference_update(y)

print(x)

planets = {"earth", "mars", "jupiter"}
planets.discard("mars")

print(planets)

x = {"earth", "mars", "jupiter"}
y = {"jupiter", "neptune", "uranus"}

z = x.intersection(y)

print(z)

x = {"earth", "mars", "jupiter"}
y = {"uranus", "pluto", "earth"}

x.intersection_update(y)

print(x)

x = {"earth", "mars", "jupiter"}
y = {"burger", "pizza", "nuglets"}

z = x.isdisjoint(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

planets = {"mars", "mercury", "venus"}

planets.pop()

print(planets)

planets = {"earth", "mars", "mercury"}
planets.remove("mars")

print(planets)

x = {"earth", "mars", "jupiter"}
y = {"mars", "neptune", "venus"}

z = x.symmetric_difference(y)

print(z)

x = {"earth", "mars", "jupiter"}
y = {"venus", "neptune", "earth"}

x.symmetric_difference_update(y)

print(x)

x = {"earth", "mars", "jupiter"}
y = {"mercury", "pluto", "mars"}

z = x.union(y)

print(z)

x = {"earth", "mars", "jupiter"}
y = {"venus", "mercury", "earth"}

x.update(y)

print(x)


# tuple methods

thistuple = (3,6,8,7,4,3,7,5)

x = thistuple.count(5)

print(x)

thistuple = (3,6,8,7,4,3,7,5)

x = thistuple.index(8)

print(x)

# dictionary methods

list1 = {
  "mat": "100",
  "eng": "95",
  "tam": "98"
}

list1.clear()

print(list1)

list1 = {
  "mat": "100",
  "eng": "95",
  "tam": "98"
}

x = list1.copy()

print(x)

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

list2 = {
  "mat": "100",
  "eng": "90",
  "sci": "97"
}

x = list2.get("mat")

print(x)

list3 = {
  "tam": "99",
  "mat": "95",
  "evs": "98"
}

x = list3.items()

print(x)

list4 = {
  "tam": "90",
  "eng": "97",
  "mat": "65"
}

x = list4.keys()

print(x)

list5 = {
  "a": "1",
  "b": "4",
  "g": "9"
}

list5.pop("g")

print(list5)

list6 = {
  "A": "23",
  "B": "79",
  "U": "98"
}

list6.popitem()

print(list6)

list7 = {
  "a": "1",
  "l": "10",
  "m": "98"
}

x = list7.setdefault("l", "m")

print(x)

list8= {
  "b": "boy",
  "g": "girl",
  "c": "common"
}

list8.update({"gender": "M/F"})

print(list8)

list9 = {
  "b": "1",
  "m": "2",
  "y": "8"
}

x = list9.values()

print(x)

#list methods

list1 = ['1', '3', '5']
list1.append("9")

print(list1)

list1= ['1', '3', '5', '9']

list1.clear()

print(list1)

list1= ['1', '3', '5', '9']

x = list1.copy()

print(list1)

list1= ['1', '25', '39']

x = list1.count("25")

print(list1)

list2= ['a', 'b', 'c']

list3 = ['F', 'B', 'V']

list2.extend(list3)

print(list2)


list1 = ['a', 'b', 'c']

x = list1.index("a")
print(x)

list1 = ['a', 'b', 'c']

list1.insert(1, "r")
print(list1)

list1 = ['a', 'b', 'c']

list1.pop(1)
print (list1)   
                                           
list1 = ['a', 'b', 'c']

list1.remove("b")
print(list1)

list1 = ['a', 'b', 'c']

list1.reverse()
print(list1)

list2 = ['F', 'B', 'W']

list2.sort()
print(list2)

# string methods

txt = "hello, world"

x = txt.capitalize()

print (x)


txt = "Hello, world"

x = txt.casefold()

print(x)

txt = "apple"

x = txt.center(20)

print(x)


txt = "I am good in math,math is easy to learn"

x = txt.count("math")

print(x)


txt = "My name is Mini"

x = txt.encode()

print(x)

txt = "Hello, world"

x = txt.endswith(".")

print(x)

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

txt = "Hello, my dear."

x = txt.find("dear")

print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 55))

txt = "Hello, welcome ."

x = txt.index("welcome")

print(x)

txt = "Company12"

x = txt.isalnum()

print(x)

txt = "NewhomeS"

x = txt.isalpha()

print(x)

txt = "\u0044" #unicode for 4

x = txt.isdecimal()

print(x)

txt = "69000"

x = txt.isdigit()

print(x)


txt = "MAN1"

x = txt.isidentifier()

print(x)


txt = "hello world!"

x = txt.islower()

print(x)

txt = "76345876312969"

x = txt.isnumeric()

print(x)

txt = "HOW ARE YOU?"

x = txt.isprintable()

print(x)


txt = "   "

x = txt.isspace()

print(x)


txt = "Hello World"


x = txt.istitle()

print(x)

txt = "SMILE ALWAYS"

x = txt.isupper()

print(x)

myTuple = ("1", "11", "111")

x = "#".join(myTuple)

print(x)

txt = "Chennai"

x = txt.ljust(20)

print(x, "is my favorite place.")


txt = "Hello EVERYONE"

x = txt.lower()

print(x)


txt = "     chennai     "

x = txt.lstrip()

print("of all places", x, "is my favorite")


txt = "Hello Ram!"
mytable = txt.maketrans("R", "P")
print(txt.translate(mytable))


txt = "I could do workouts all day"

x = txt.partition("workouts")

print(x)

txt = "I like icecream"

x = txt.replace("icecream", "fruits")

print(x)


txt = "My name is singham."

x = txt.rfind("singham")

print(x)


txt = "I like idly."

x = txt.rindex("idly")

print(x)


txt = "strawberry"

x = txt.rjust(20)

print(x, "is my favorite milkshake.")


txt = "I could do workouts all day, workouts are good for health"

x = txt.rpartition("workouts")

print(x)


txt = "a, b, c"

x = txt.rsplit(", ")

print(x)


txt = "     chennai     "

x = txt.rstrip()

print("of all places", x, "is my favorite")


txt = "welcome home"

x = txt.split()

print(x)


txt = "If you work hard \nd you will reap success"

x = txt.splitlines()

print(x)

txt = "Hello, world."

x = txt.startswith("Hello")

print(x)

txt = "     pizza     "

x = txt.strip()

print("of all fastfoods", x, "is my favorite")


txt = "Hello I Am DEEPAK"

x = txt.swapcase()

print(x)

txt = "Welcome everyone"

x = txt.title()

print(x)

#use a dictionary with ascii codes to replace 83 (s) with 80 (p):
mydict = {83:  80}
txt = "Hello pavi!"
print(txt.translate(mydict))

txt = "Hello world"

x = txt.upper()

print(x)

txt = "60"

x = txt.zfill(10)

print(x)


# calculator


# Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
    # Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
  
        




































































