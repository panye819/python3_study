# -*- coding:utf-8 -*-
'''
Created on 2017年7月4日

@author: FlyPiG8308
'''
num = 83
guess_flag = False
# if num == guess:
#     print("Bingo!!You are right!")
#     print("You win!!")
# elif guess < num:
#     print("the number you guess is lower than number!")
# else:
#     print("The number you guess is larger than number!")
# print("Done!")


while guess_flag == False:
    guess = int(input("please input a number: "))
    if num == guess:
        print("Bingo!!You are right!")
        print("You win!!")
        guess_flag = True
    elif guess < num:
        print("the number you guess is lower than number!")
    else:
        print("The number you guess is larger than number!")
print("Done!")
    