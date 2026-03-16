#Q1
stdmarks = []
stdnum = 3
i = 1
while i <= stdnum:
    stdmarks.append(input(f"Enter name {i}: "))
    stdmarks.append(float(input(f"Enter degree {i}: ")))
    i += 1
stdmarks.insert(4, input("Enter the new name: "))
stdmarks.insert(5, float(input("Enter the new degree: ")))
stdmarks[6] = input("Enter the replacement name for the 3rd student: ")
print(f"Current List: {stdmarks}")
passedStudents = []
j = 1
while j < len(stdmarks):
    if stdmarks[j] >= 50:
        print(f"{stdmarks[j - 1]} passed with: {stdmarks[j]}")
        passedStudents.append(stdmarks[j-1])
        passedStudents.append(stdmarks[j])
    else:
        print(f"{stdmarks[j - 1]} failed with: {stdmarks[j]}")
    j += 2
print("Passed students:")
k = 0
while k < len(passedStudents):
    print(f"{passedStudents[k]} - {passedStudents[k+1]}")
    k += 2



#Q2
number = input("Enter the to take the sum of its digits: ")
sum = 0
i = 0
while i < len(number):
    sum += int(number[i])
    i += 1
print("The result is: ", sum)



#Q3
number = int(input("Enter a number to get its factorial: "))
factorial = 1
i = 1
while i <= number:
    factorial = factorial * i
    i+=1
print(f"The factorial of {number} is: ", factorial)



#Q4
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if n1>n2 and n1>n3:
    print("The first number is greater than the others: ", n1)
elif n2>n1 and n2>n3:
    print("The second number is greater than the others: ", n2)
else:
    print("The third number is greater than the others: ", n3)




#5
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n + 1):
    sum +=i
print("The sum is: ", sum)



#6
while True:
    number = int(input("Enter a positive number number"))
    if number > 0:
        break
count = 0
for digit in str(number):
    count += 1
print("Number of digits is:", count)



#7
numbers = []
n = int(input("How many numbers you want to enter: "))
for i in range(n):
    num = int(input("Enter the number: "))
    prime = True
    if num <= 1:
        prime = False
    else:
        for j in range(2, num):
            if num % j == 0:
                prime = False
                break
    if prime:
        numbers.append(num)
tuple = tuple(numbers)
print("Prime numbers in tuple: ",tuple)



#8
number = []
num = int(input("Enter the numbers of employee: "))
for i in range(num):
    name = input("Enter employee name: ")
    number.append(name)
number.sort()
print(number)