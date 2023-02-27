# print("hello")
# =======tip calculator:====
# food_amount = int(input("enter your payment: "))
# tip_amount = int(input("enter the tip percetage: "))

# total = int((food_amount*(tip_amount/100))+food_amount)

# print(f'Food Amount: ${food_amount}')
# print(f'Tip Amount: ${tip_amount}\n')
# print(f'total: 😀${total}')


# weather app
# weather = input("how's the weather? ")
# if weather == 'rain':
#     print("⛱️")

# else:
#     print("😎")

# comarison operator

# score = int(input("enter your score: "))


# if score > 90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("fail")



#functions

# from unicodedata import name


# def my_name_is():
#     name = input("what is your name? ") 
    
#     print(f"your name is: {name}" )

# # 1>arguement
# my_name_is()

# def my_name(name):
#     print(f'Hey!👋🏻  {name}')
# my_name('Arpit')


# # 2> multiarguement
# # it will take more than > 1 arguement in function 

# def greeting(greet, name):
#     print(f'{greet} 👋🏻 {name}')
# greeting('Hey', 'Arpit')

# # 3> default arguement
# def greetings(name, greet= 'hello'):
#     print(f'{greet}! {name}')

# greetings('Arpit')

# # 4> named arguemtnt
# def greetingss(name, greet):
#     print(f'{greet}! {name}')

# greetingss(name= 'Arpit', greet='Heyyaa')


# sum funtion: 

# def sum(a,b):
#     return a + b
# print(sum(1, 2))


# tip calculator with functions:

# def calculateFoodTotal():
#     food_amount = int(input("enter your payment: "))
#     tip_amount = int(input("enter the tip percetage: "))

#     total = int((food_amount*(tip_amount/100))+food_amount)

#     print(f'Food Amount: ${food_amount}')
#     print(f'Tip Amount: ${tip_amount}\n')
#     print(f'total: 😀${total}')

# calculateFoodTotal()

# def calculateFoodTotal2(foodTotal, tipAmount):
#     total = int((foodTotal*(tipAmount/100))+foodTotal)
#     print(f'the total is: ${total}')

# calculateFoodTotal2(tipAmount=20,foodTotal=100)

# =============================================
# pro level2 food total:-
from re import A


# def calculateFoodTotal(food: float, tip_percentage: int) -> float:

#     total = (food*(tip_percentage/100))+food
#     print('------------------------')
#     print(f'Food Amount: ${food}')
#     print(f'Tip Amount: ${tip_percentage}\n')
#     print(f'total: 😀${total}')
#     print('------------------------')
#     return total

# print(calculateFoodTotal(tip_percentage=20, food=100))

# =======weather function prolevel==========
#  =============TYPEHINTING===========

# def weather_to_emoji(weather:str) -> None:
#     if weather == 'rain':
#         print("⛱️")
#     else:
#         print("😎")

# weather_to_emoji('rain')
# ===========================================

# def sum(a:int ,b:int) -> int:
#     return a+b

# print(sum(1,2))

# ==============problem solved==============
# def bigger_guy(a: float,b: float)->float:
#     if a>b:
#         return a
#     else:
#         return b

# print(bigger_guy(a=2,b=4))


# ===============lambda function================
# anonymous function

# def sum(a,b):
#     return a + b

# sum2 = lambda a,b : a + b
# print(sum2(5,4))

# # =================================================

sum3 = lambda a,b : a+b
print(sum3(1,2))
assert sum3(1,2) == 3


