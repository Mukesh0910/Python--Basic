def isLeap(a):
    if a%400==0:
        return 1
    if a%100!=0:
        if a%4==0:
            return 1
        return 2
    else:
        return 2
a=input("Enter First Date: ")
b=input("Enter Second Date:")
c=int(a[6:])
d=int(b[6:])
leapyears =""
nonleapyear =""
for i in range(c,d+1):
    s=isLeap(i)
    if s==1:
        leapyears=leapyears+str(i)+","
    else:
        nonleapyear=nonleapyear+str(i)+","
leapyears=leapyears[0:len(leapyears)-1]
print("leap Year")
print(leapyears)
nonleapyear=nonleapyear[0:len(nonleapyear)-1]
print("Non Leap year")
print(nonleapyear)