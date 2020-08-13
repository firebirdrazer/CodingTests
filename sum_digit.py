Num=int(input()) #input
Sum=0
while (Num - Num%10)>0: #if the input has 2 or more digits
    Sum += Num%10       #extract the lowest digit and sum
    Num //= 10          #the rest digits would be processed by the same "while"
else:
    Sum += Num          #if the input has the only 1 digit (or processed to 1 digit)
print(Sum)