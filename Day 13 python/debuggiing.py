# 1. describe problem

# def my_func():
#     for i in range(1,21):
#         if i == 20:
#             print("You Got It")
# my_func()


#2. reproduce the bug

# from random import randint
# dice_imgs=["1", "2", "3", "4","5", "6"]
# dice_num= randint(0,5)
# print(dice_num)
# print(dice_imgs[dice_num])

#3. Play Computer

# year= int(input("what's Your Year Of birth? "))
# if year> 1980 and year <1994:
#     print ("you are a millenial")
# elif year>=1994:
#     print(" you are an Gen Z ")


#4. Fix The Errors

# age = int(input("How Old Are You ?"))
# if age > 18:
#     print(f"You Can Drive at age {age}")

#5. print is you friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page =int(input("Number of words per page : "))
# total_words = pages * word_per_page
# print ( total_words )

#6. Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1 ,2, 3, 4, 5,8, 13 ])