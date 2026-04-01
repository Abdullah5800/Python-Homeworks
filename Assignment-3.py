#Q1
st = input("String: ")
vowels = ['a','e','i','o','u']
counter = 0
for ch in st:
    if ch in vowels:
        counter += 1
print("Vowel letters:", counter)


#Q2
max = 0
for i in range(10):
    num = int(input("Enter your number"))
    if num > max:
        max = num
print(f"The largest number is: {max}")


#Q3
n = int(input("Enter your num"))
for i in range(n + 1):
    print('*' * i)


#Q4
input_list = input("Enter the values separated by commas: ").split(',')
input_list = [int(item) for item in input_list]
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print("The list without duplicates:", unique_list)


#Q5
num = int(input("The num is: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#Q6
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
elements = []
for item1, item2 in zip(list1, list2):
    if item1 == item2:
        elements.append(item1)
print("elements:", elements)


#Q7
password = input("Enter password: ")
if len(password) >= 8 and \
   any(char.islower() for char in password) and \
   any(char.isupper() for char in password) and \
   any(char.isdigit() for char in password):
    print("Valid")
else:
    print("Invalid. make sure it meets the criteria")


#Q8
def printmor():
    print("Good morning")
printmor()


#Q9
def _user():
    name = input("Enter the name:")
    print(f"{name}")


#Q10
def sum():
  x=int(input("Enter first number: "))
  y=int(input("Enter second number: "))
  result=x+y
  print(f"sum:{result}")
sum()


#Q11
def rect(l, w):
    area = l * w
    return area
l = int(input("Long: "))
w = int(input("Width: "))
area = rect(l, w)
print(f"The area of the rectangle is={area}")


#Q12
def find_largest_number():
    numbers_input = input("number_input=")
    numbers = [int(num) for num in numbers_input.split()]
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"The largest number is {largest}")
find_largest_number()


#Q13
def reverse_string(s):
    return s[::-1]
input_string = input("Enter a string:")
reversed_string = reverse_string(input_string)
print(f"The reverse of the string is: {reversed_string}")


#Q14
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number = int(input("Enter num: "))
print(f"The factorial of {number} is: {factorial(number)}")


#Q15
def check_credentials(username, password):
    valid_username = "first user"
    valid_password = "pass2345"
    if username == valid_username and password == valid_password:
        return "Valid credentials"
    else:
        return "Invalid credentials"
def main():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    result = check_credentials(username, password)
    print(result)
main()


#Q16
import random
def generate_random_number():
    return random.randint(1, 100)
def check_guess(guess, number):
    if guess < number:
        return "Too low"
    elif guess > number:
        return "Too high"
    else:
        return "Correct"
def play_game():
    number = generate_random_number()
    guess = None
    while guess != number:
        guess = int(input("Guess: "))
        result = check_guess(guess, number)
        print(result)
play_game()