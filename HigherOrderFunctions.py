# ======higher order function========

from cgi import print_directory
import numbers
from unittest import result

from numpy import full, number

# easy method pro
def double_number(number:int)->int:
    return number*2

# print(double_number(1))
print(list(map(double_number,[1,2,3,4])))

# difficult method beginner
def double_number2(numbers:int)->int:
    result=[]
    for number in numbers:
        result.append(number*2)
    return result

print(double_number2([1,2,3]))

# more pro level using lambda and map

print(set(map(lambda double: double*2, [1,2,3])))

def even1(numbers):
    result=[]
    for number in numbers:
        if number%2==0:
            result.append(number)
    return result

print(even1([1,2,3,4,5]))

def even2(numbers):
    if numbers%2==0:
        return numbers

print(list(map(even2,[1,2,3,4,5,6,7,8,9])))

print(list(map(lambda even: even%2==0,[1,2,3,4,5,6,7,8,9])))
# map takes 2 things before ',' is function itself and after ',' is the input we give


# filter(list(map(lambda even: even%2==0,[1,2,3,4,5,6,7,8,9])))
numbers=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda even3:even3%2==0, numbers)))
# here lamda is function and after ',' is what the output should be
# filter do is it iterate through list or set anything and then it perfrom the function and then write the desired output whicfh is "TRUE"
# filter only writes 'TRUE' value
 

#  list comprehension
# filer and print only ODD number

print([number for number in numbers if number%3==0])

print([number*2 for number in numbers if number%2==0])