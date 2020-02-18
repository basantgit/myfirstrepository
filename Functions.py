#Define function
def my_function(fname):
  print(fname + "Basant")

my_function("Emil")
my_function("EmployeID")
my_function("Place")

#Passing a List as an Argument

def my_function(Basant):
  for x in Basant:
    print(x)

fruits = ["apple", "banana", "cherry"]
animal = ["cow", "horse", "cat"]
birds = ["duck", "peacock", "swan"]
games = ["cricket", "football", "volyball"]

my_function(fruits)
my_function(animal)
my_function(birds)
my_function(games)

#Return Values
def my_function(x):
  return 10 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement
def myfunction():
  pass
#