#Q1
class person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"The name is: {self.name}")
class employee(person):
    def __init__(self, name, salary):
        person.__init__(self, name)
        self.salary = salary

    def display(self):
        print(f"Name is: {self.name},And salary is: {self.salary}")
name = input("Enter the name: ")
salary = int(input("Enter the salary"))
per = employee(name, salary)
per.display()



#Q2
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Hello there,{self.name}")

name = input("Enter the name: ")
person = Person(name)
person.greeting()


#Q3
class animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def animalVoice(self):
        print("(Any animal voice)")


class Dog(animal):
    def animalVoice(self):
        print("Woof")

    def display_info(self):
        print(f"Age is: {self.age},And the color is: {self.color}")


class Sheep(animal):
    def animalVoice(self):
        print("Meeeeeee333")

    def display_info(self):
        print(f"age is: {self.age},And the color is: {self.color}")

age = int(input("Enter dog age: "))
color = input("Enter dog color: ")
dog = Dog(age, color)
sheep = Sheep(6, "Black")
dog.display_info()
dog.animalVoice()
sheep.display_info()
sheep.animalVoice()




#Q4
class bankaccount:
    def __init__(self, customer_name, account_no, balance):
        self.customer_name = customer_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"The deposite is: {amount},and the balance is: {self.balance}")

    def withdraw(self, amount):
            self.balance -= amount
            print(f"Withdraw{amount},The balance: {self.balance}")

    def balance_b(self):
        print(f"Full balance: {self.balance}")

customer_name = input("Enter the customer name: ")
account_no = input("Enter the account number: ")
balance = float(input("Enter the account balance: "))
p=bankaccount(customer_name, account_no, balance)
p.deposit(500)
p.withdraw(100)
p.balance_b()



#Q5
def add_element(my_list, element):
    my_list.append(element)
    print(f"Added: {element}")
def delete_element(my_list, element):
        for element in my_list:
            my_list.remove(element)
            print(f"Deleted:  {element}")
my_list = ["Csharp","Html","C"]
print(add_element(my_list, "Html"))
print(delete_element(my_list, "Csharp"))
print(f"list={my_list}")


#Q6
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return "The number is not prime"
        else:
            return "The number is prime"
def check_number(n):
    if n > 0:
        return "The number is positive"
    elif n < 0:
        return "The number is negative"
    else:
        return "The number is zero"
n = int(input("Enter the factorial: "))
print(factorial(n))
pri = int(input("Enter the number to check wither prime or not: "))
print(check_prime(pri))
num = int(input("Enter the number: "))
print(check_number(num))



#Q7
def inverse_string(s):
    return s[::-1]
def string_length(s):
    return len(s)
def delete_spaces(s):
    return s.replace(" ", "")
def check_empty(s):
    if len(s) == 0:
        return "The string is empty"
    else:
        return "The string is not empty"
s= input("Enter the string: ")
print("The inverse is: ",inverse_string(s))
print("The length is: ", string_length(s))
print("The string without spaces: ", delete_spaces(s))
print("Empty or not: ", check_empty(s))



#Q8
import sorting
data_input = input("Enter the numbers to sort: ")
numbers = [int(x) for x in data_input.split()]
choice = input("Enter your choice: 1 = Bubble Sort, 2 = Merge Sort, 3 = Quick Sort: ")
if choice == '1':
    result = sorting.bubble_sort(numbers)
    print(f"The result by Bubble Sort: {result}")
elif choice == '2':
    result = sorting.merge_sort(numbers)
    print(f"The result by Merge Sort: {result}")
elif choice == '3':
    result = sorting.quick_sort(numbers)
    print(f"The result by Quick Sort: {result}")
else:
    print("You didn't choose a valid choice")




#Q9
class Shape:
    def __init__(self, colour):
        self.colour = colour
    def howManySides(self):
        print("Shape")
class rectangle(Shape):
    def __init__(self, colour):
        super().__init__(colour)
    def howManySides(self):
        print(f"The Rectangle color: {self.colour}")
class circle(Shape):
    def __init__(self, colour):
      Shape.__init__(self, colour)

    def howManySides(self):
        print(f"The circle color: {self.colour}")
c1=input("Enter the rectangle color: ")
rect = rectangle(c1)
rect.howManySides()
c2=input("Enter the circle color: ")
circ = circle(c2)
circ.howManySides()



#Q10
def area(r):
    return 3.14 * r * r
def per(r):
    return 2 * 3.14* r
def area1(s):
    return s * s
def per1(s):
    return 4 * s
r=int(input("Enter the radius: "))
print(f"Area is: {area(r)}")
print(f"Perimeter is: {per(r)}")
s=int(input("Enter the square side long: "))
print(f"Area of the square is: {area1(s)}")
print(f"Perimeter of the square is: {per1(s)}")