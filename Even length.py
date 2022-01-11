str1=input("Enter the string:")
str2=str1.split(' ')
for i in str2:
    if(len(i)%2==0):
        print(i)
