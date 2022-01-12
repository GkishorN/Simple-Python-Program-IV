s=input("Enter the string:")
flag=0
for i in s:
    if(i!='0' and i!='1'):
        flag=1
if(flag==1):
    print("String is not binary string")
else:
    print("String is binary string")
