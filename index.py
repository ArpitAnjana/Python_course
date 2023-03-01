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
from unicodedata import name


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

# ==============assert checking=======================
# sum3 = lambda a,b : a-b
# print(sum3(1,2))
# assert sum3(1,2) == 3, 'does not return 3'

# =============================================

# =========LISTS (ARRAYS)===============

# fruit = ['🍎','🍏','🍒','🍌']
# print(fruit)
# fruit.append('🍊')
# print(fruit)

# # ==========indexing=============
# # ===========slicing==============
# print(fruit[3:5])
# print(fruit[-4:-1])
# print(fruit[0:len(fruit)-1])
# # ======slicing string=============
# print('hy my name is arpit'[0:10])
# print(fruit[::-1])


# =============Dictionary===========

# person = {
#     'name': 'arpit',
#     'shirt': 'black'
# }
# print(person['name'],person['shirt'])

# def networth():
#     return person['assets']-person['debt']

# def introducer():
#     person = {
#     'name': 'arpit',
#     'shirt': 'black',
#     'assets' : 100,
#     'debt': 50,
#     'networth': lambda:person['assets'] - person['debt'] #here we use lambda function bcz in a dictionary we cannot use def in a object of dictionary instead we can use lambda function to create a function inside a dictionary 
#     # here networth is a function because of lambda function inside a dictionary (function -> dictionary -> function)
#     # i think we use lambda function for inline function
# }
#     person['assets'] = 1000
#     print(f"\n hi my name is {person['name']} \n i am wearing {person['shirt']} shirt\n my networth is {person['networth']()}") #we are using {person['networth']()} this because it takes the value from person's networth thats a function inside a dict so we have to say {person['wealth']} but it wont work because it a function inside a dict so we have to write it like {person['networth']()}
# introducer()


# ===========sets=============

# list1 = ['ruby', 'java', 'python']
# list2 = ['ruby', 'javascript', 'python', 'c++']

# print(set(list1+list2))
# # it selects the unique elements from set

# print(f"this is new:\n{list(set(list1+list2))}")


# # set function
# def unique():
#     list1 = ['ruby', 'java', 'python']
#     list2 = ['ruby', 'javascript', 'python', 'c++']
#     return f"this is new:\n{list(set(list1+list2))}"
#     # print(f"this is new:\n{list(set(list1+list2))}")

# print(unique())


# def unique2(languages):
#     return list(set(languages))

# print(unique2(["python", "python","java"]))


# unique3 = lambda languages: list(set(languages))
# print(unique3(["python", "python","java"]))



# ==========for loops===============

# def fruits():
#     fruit=['🍒','🍓','🍇']
#     for i in enumerate(fruit):
#         print(f'fruit: {i}')
        

# fruits()

# fruit=['🍒','🍓','🍇']
# for i in range(5):
#     fruit.append('🍎')
    
# print(fruit)

# -===============while loop=============
counter = 0
while counter <10:
    print(counter)
    counter +=1
