n=int(input("Enter the number"))
str1="A"
str2="B"
print( str1 ,"",str2,end=" ")
for  i in range(1,n):
    next_str=str2+str1
    print(next_str,end=" ")
    str1=str2
    str2=next_str