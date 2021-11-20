n=int(input("enter number to check:-"))
i=n
count=0
while i>0:
    count=count+1
    i=i//10
sum=0
i=n
while i>0:
    digit=i%10
    x=1
    pro=1
    while x<=count:
        pro=pro*digit
        x=x+1
    sum=sum+pro
    i=i//10
if sum==n:
    print("armstrong number")
else:
    print("not armstrong number")





# sum=0
# var=int(input("enter the number"))
# temp=var
# while (var):
#     i=1
#     j=1
#     x=var%10
#     while (i<=x):
#         j=j*1
#         i=i+1
#     sum=sum+j
#     var=var//10
# if (var==temp):
#     print("it is a armstrong number")
# else:
#     print("it is a not armstrong number")