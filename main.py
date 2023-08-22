#  a = 10

# b = 5
# c = 2.5
# d = 5
# is_success = True
# is_late = False
# name = "김기환" # 문자열, string

# 문자열, 정수, 소수, boolean (참/거짓을 뜻할 수 있는 데이터 타입)
# print(name)
# print(b == d)

# import math
# print(math.ceil(5.1))
# print(math.ceil (c + d))

# print(divmod(100,8))

# print("*"*10)

# a = "hello world"
# print(a)
# print(a[-1:6])

# print("-".join(a))

# a = "python!"
# print(a.find("!"))

# a = "dog is love"
# print(a.replace("dog","cat"))
# print(a[5:])

# a = [1,2,3,["a,b,c"]]
# print(a[3])
# print(a[0]+a[2])

# a = {"name":"jawon","age":20,"phone":"010-1111-2222"}
# b = {1:"hi"}
# c = {"x":[1,2,3]}
# d = {}

# print(a,b,c,d)

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])


# print(s1|s2)

# my_list = set([1,2,3,4,4,4,9,11,11,11,14])

# # my_list = list(set(my_list))

# print(my_list)


# score = int(input("Enter score: "))
# if 90 <= score <= 100:
#     print("A")

# score = int(input("enter score"))

# if 90 <= score <= 100:
#     print("A")

# elif 80<= score <= 90:
#     print("B")
    
# else:
#     print("C")"

# my_list = ["a","b","c","d","e"]
# for i in range(len(my_list)):
#     print(my_list[i])

# score = int(input("Enter score: "))
# if score % 2 == 0:
#     print("짝수")

# else:
#     print("홀수")

# score = int(input("Enter score: "))
# if score >= 90:
#     print("합격!!")

# else:
#     print("불합격ㅠ")

# def coffee_vending_machine():
    # dictionary를 써서 메뉴를 만들어놓고
    # 거기에 대한 입력을 받게 하고
    # 메뉴가 있는지 체크해야 하고
    # 돈을 받는다.
    # 금액이 모자란지 체크를 하고, 거스름돈을 준다.
#     coffee_options = {
#         '1': {'name': 'Americano ice', 'price': 2000},
#         '2': {'name': 'Americano hot', 'price': 1500},
#         '3': {'name': 'Vanilla Latte ice', 'price': 3000}
#     }

#     print('Welcome! here\'s the menu')
#     for key, value in coffee_options.items():
#         print(key, ':', value)

#     choice = input("Please select menu : ")
#     # if choice not in coffee_options:
#     #     print('invalid menu')
#     #     return
#     while choice not in coffee_options:
#         print('invalid menu, choose again')
#         choice = input("Please select menu : ")

#     amount_paid = input("액수를 입력하세요 : ")
#     price = coffee_options[choice].get('price')

#     if amount_paid == price:
#        print("thx! enjoy your {coffee_options[choice]["name"]}")
             
#     elif amount_paid > price:
#         change = amount_paid - price
#         print('thx! change : ', change)
#     else:
#         print('Insufficient amount')

# coffee_vending_machine()

def get_body_mass_index():
    weight = float(input('enter weight : '))
    height = float(input('enter height in cm : ')) / 100

    body_mass_index = weight / (height ** 2)
    body_mass_index = round(body_mass_index, 2)
    print(f'BMI: {body_mass_index}')
