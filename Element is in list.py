a=[1,7,4,9,7,9]
n=int(input("Enter the number to be checked:"))
flag=0
for i in a:
    if(int(i)==n):
        flag=1
if(flag==1):
    print("Yes! Element is in the list")
else:
    print("No!Element is not in list")
        
