# print("you have five chance guess the number")
# print("you have enter the number 1 to 10")
# i=1
# while i<=5:
#     num=int(input("enter the number"))
#     if num==9:
#         print("exelent you guess correct number")
#         break
#     else:
#         print("you guess is incorrect try again")
#     i=i+1
# else:
#     print("game over")



print("you have five chance guess the number")
print("you have enter the number 1 to 10")
i=1
while i<=5:
    num=int(input("enter the number"))
    if num==7:
        print("wow,exelent you guess correct number")
        break
    elif num<7:
        print("entered your number is small,try one more time")
    elif num>7:
        print("entered your number is greater,try one more time")
# else:
    # print("game voer")

 