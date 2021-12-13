import re

string1 = 'abc1234@rit.edu'
string2 = 'ab1234@rit.edu'
string3 = 'ab1234@g.rit.edu'
string4 = 'ab1234@grit.edu'

def myfunc(string):
    x = re.findall('[a-zA-Z]{2}[a-zA-z]?\d{4}@rit.edu', string)
    print(x)

myfunc(string1)
myfunc(string2)
myfunc(string3)
myfunc(string4)