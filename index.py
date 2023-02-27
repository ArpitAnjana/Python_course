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

def calculateFoodTotal2(foodTotal, tipAmount):
    total = int((foodTotal*(tipAmount/100))+foodTotal)
    print(f'the total is: ${total}')

calculateFoodTotal2(100,20)