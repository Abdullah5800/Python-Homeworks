number = int(input("Enter your number to get thefactorial: "))
fact = 1
for i in range(1, number + 1):
    fact *= i
print(f"The factorial: {fact}")






n=int(input("Enter the length of the list:"))
numbers=[]
for i in range(1,n+1):
    x=int(input("Enter the list numbers:"))
    numbers.append(x)
print(numbers)