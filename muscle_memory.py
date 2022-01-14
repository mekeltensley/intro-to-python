# Task 2

#Problem 1 

from cgi import print_form
from xml.etree.ElementTree import iselement


idx = 'abcde'.index('d')

idx = idx + 11

print(idx)

idx * 2 
print(idx)


# Problem 2 

num = 33

is_even = num % 2 == 0
print(is_even)
print(not is_even)

# Problem 3

str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)

str2 = 'bootcamp'
print(str2[num].upper())

char = str2[num].lower()
print(char)

sentence = 'welcome to bootcamp prep'
last_char = sentence[len(sentence) - 1]
print(last_char)
print(sentence.index(last_char))