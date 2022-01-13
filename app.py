# this is a comment
# TODO built this function

def add(num, num2):
    '''
    this is suppose to add 2 numbers
    '''


name = "Johnny"

nothing = None

is_working = True
car_off = False

if nothing:
    print('This is true') 
    num = 7 
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')
else:
    print('This is not true...')

# this is another conditional
if is_working:
    print('This is working also')

# conditional -> this first item that represents 
# True, it runs that indented [block]

print(15 / 6)
print(15 // 6)

print("ace of spades".split(" "))
# => ["ace", "of", "spades"]

print("ace-of-spades".split("-"))
# => ["ace", "of", "spades"]

print("ace.of.spades".split("."))
# => ["ace", "of", "spades"]

my_scare = "boo"
my_scare.upper()

print("eggs" in "green eggs and ham")

food = "eggs"
print(food in "green eggs and ham")
print(len(food)) # => 4

statement = "my code rules"[3:9]
print(statement)

if 7 == 7:
    print('This is 7')
else:
    print('This is the second condition')

if 7 != 6:
    print('We are not the same')
else:
    print('This is the second condition')

if not 7:
    print('This is 7')
else:
    print('This is the second condition')


arr = [1, "two", 3, "four", True, False, "hello"]
print(arr[1])
print(arr[-1])

one_through_ten = list(range(10))
print(one_through_ten)

three_through_ten = list(range(3, 10))
print(one_through_ten)


a = [1, 23, 12, 99, 82]
a.sort()
print(a)

a.append(88)
print('After adding 88', a)

a.insert(1, 77)
print('After inserting 77 at index 1 ...', a)

a.pop()
print('popping....', a)

if 33 in a:
    print('This Michael Jordan number!')
else:
    print('Not in there...')

print('Is 7 a digit???', '7'.isdigit())

cat = {
  "name": 'Hamlet',
  "breed": 'American Shorthair',
  "fav_food": 'Prosciutto'
}

cat["name"] = "Garfield"
# 'Hamlet'

print('Do not feed to cat...' ,cat["fav_food"])
# 'Prosciutto'

print('this is my cat breed', cat.get("breed"))
print(cat.get("name"))
cat["age"] = 3
print(cat.get('age'))
# help(dict)

print('ITEMS', cat.items())
print('KEYS', cat.keys())

cat_keys = list(cat.keys())
print(cat_keys)


# String Interpolation
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)

# 2
location = "California"
number = 6
my_second_message = f"{location} is the {number}th largest economy in the world."
print(my_second_message)

# 3
topic = 'Inflation'
num = 7
y = 1982
my_third_message = "{} is at {} percent. Highest since {}".format(topic, num, y)
print(my_third_message)

# Loops

# n = 0
# while n < 1000:
#   n += 1
#   if n % 2 == 0:
#       print(f'{n} is even...')

n = True # setting a boolean
num = 1 # setting a number that will incremented
while n: # if n get to False -> the loop stops
    if num % 2 == 0: # check to see if number is even
        print(f'{num} is even...')

        if num == 750: # check to see if num is 750
            n = False # set the boolean to False
            print('End program')
    num += 1 # adding one to num

# for loop
for i in range(1, 751): 
    if i % 2 == 0:
        print(f"{i} is even...", '**')

        if i == 750:
            print('End program')

nums = [1,2,3,55,66,44,33,22,11,33,750, 44, 66, 33,33,22]
for i in range(len(nums)):
    element = nums[i]
    if element % 2 == 0:
        print(f"{element} is even...", 'NUMS')

        if element == 750:
            print('Hi I am 750')

students = [
    { 
        "name": "Kimmie",
        "city": "Atlanta"
    },
    { 
        "name": "Chris",
        "city": "Salt Lake City"
    },
    { 
        "name": "Zack",
        "city": "Los Angeles"
    }
]

for i in range(len(students)):
    student = students[i]
    print(student.get("name"))

    if student.get("city") == 'Los Angeles':
        print(f'{student.get("name")} wins an iPad for {student.get("city")}', 1)
        print(f"{student.get('name')} wins an iPad for {student.get('city')}", 2)

for i in range(len(students)):
    student = students[i]
    print(student.get("city"))

# Iterating through list of students
for student in students:
    print(student)

# Iterating through dict
for key in students[0]: # key to key
    print(key) # string of the key
    print('value', students[0].get(key))

# Iterating through dict PART 2
for key in students[1]: # key to key
    print(key, 'PART 2') # string of the key
    print('value', students[1][key])

# Iterating through dict PART 3
for anything in students[2]: # key to key
    print(anything, 'PART 3') # string of the key
    print('value', students[2][anything])

# Iterating through dict PART 4
for key, value in students[0].items(): # key to key
    print(key, '->', value)

def say_hello(friend="Tim"): # if we don't put a parameter, it will default to Tim
  print("Hello, {}!".format(friend))

say_hello("Tom")

def move(name, city="Seattle", state="Washington"):
  msg = "{} is moving to {}, {}"
  msg = msg.format(name, city, state)
  print(msg)

move("Charlie", "Los Angeles", "California")
move(city="San Francisco", name="Mark", state="California")
move("John", state="New York", city="New York")

def add(num1=0, num2=0):
    return num1 + num2

print(add(4, 5))


numbers = [1, 2, 3, 4]
def addition(num):
    return num + num

result = map(addition, numbers)
# print(result)

result2 = map(lambda x: x + x, numbers)
# print(list(result2))

result3 = map(lambda y: y * y, numbers)
# print(list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result4))


# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]