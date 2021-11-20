a=int(input("enter the number"))
i=1
sum=0
while i!=1 and i!=4:
    rem=a%10
    rem=rem+rem*rem
    a=a//1
if i==1:
    print("happy")
else:
    print("not happy" )
    i=i+1
