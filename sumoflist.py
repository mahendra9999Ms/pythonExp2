mylist=input("enter a list of numbers seperated by space:")

mylist=list(map(int,mylist.split()))

sum=0
for num in mylist:

    sum+=num

print("the sum of the numbers is :",sum)

output:
enter a list of numbers seperated by space:20 44 55 66 33 11

the sum of the numbers is : 229