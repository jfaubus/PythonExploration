import math as m

#starts the BasicMath Operations class
class BasicMathOperations():
    #initializer
    def __init__(self):
        None

    #method for greeting someone with their firt and last name
    def Greet(self, first, last):
        return f"Hello, {first} {last}"
    
    #method to return the sum of two numbers
    def AddNumbers(self, num1, num2):
        return f"{num1} + {num2} = {int(num1) + int(num2)}"
    
    #method to perform the operation of the user's choosing
    def Operations(self, num1, num2, operation):
        if operation == "multiply":
            return f"{num1} * {num2} = {num1 * num2}"
        elif operation == "divide":
            return f"{num1} / {num2} = {num1 / num2}"
        elif operation == "sum":
            return f"{num1} + {num2} = {num1 + num2}"
        elif operation == "subtract":
            return f"{num1} - {num2} = {num1 - num2}"
        else:
            print( "the operation was not valid")
            operation = input("Please enter either multiply, divide, sum, or subtract " )
            return f"When you {operation} {num1} and {num2} you get {BasicMathOperations.Operations(self, num1, num2, operation)}"
    
    #method to return the square of a number
    def square(self, num):
        return f"{num} squared is {int(num)**2}"
    

    #method to return the factorial of a number
    def factorial(self, num):
        factori = 1
        for i in range(1, num + 1):
            factori *= i
        return f"{num}! = {factori}"
    
    #method to count from the specifed first number to the specified second number
    def counting(self, start, end):
        for i in range(start, end + 1):
            print(i)

    #method to calculate the square of a number
    def calculateSquare(self, num):
        return num**2
    
    #used the calculateSquare method to return the hypotenuse of a right triangle
    def calculateHypotenuse(self, Base, Height):
        return f"The hypotenuse of a triangle with Base: {Base} and Height: {Height} is {m.sqrt(BasicMathOperations.calculateSquare(self, Base) + BasicMathOperations.calculateSquare(self, Height))}"
    
    #method to return the area of a rectangle
    def AreaRect(self, width, height):
        return f"The area of your rectangle: {width} * {height} = {width * height }"
    
    #method to return the power of a number
    def PowerOfNumber(self, num, power):
        return f"{num}^{power} = {num**power}"
    
    #method to return the type of argument
    def TypeOfArgument(self, argument):
        return f"The type of argument is {type(argument)}"
    
def main():
    #creates an instance of the BasicMathOperations class
    instance = BasicMathOperations()

    #prints the options
    print("Here are your options: Greet (click 1) \n Addnumbers (click 2) \n Pick an operation (click 3) \n Return the square (click 4) \n Return the factorial (click 5) \n Counting (click 6) \n Calculate the hypotenuse (click 7) \n Compute the area of a rectangle (click 8) \n Return the power of a number (click 9) \n Return the type of argument (click 10)")
    #lets the user choose by number
    choice = int(input(" What option do you pick? "))

    #if the user chooses 1
    if choice == 1:
        #gets the necessary arguments from the user
        name = input("What is your first name? ")
        lastname = input("What is your last name? ")
        #passes teh arguments to the Greet method in the BasicMathOperations class
        print(instance.Greet(name, lastname))
   #if the user chooses 2
    elif choice == 2:
        #loops until the user chooses a valid input
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments
              num1 = int(input("What is the first number you want to add? "))
              num2 = int(input("What is the second number you want to add? "))
              looping = False
              #if successful, calls the Addnumbers() method using the instance
              print(instance.AddNumbers(num1, num2))
          #catches a situation where the user doesnt input a valid data type
          except ValueError:
              print("This is not a number, please try again")
   #if the user choose 3
    elif choice == 3:
        #follows the same structure as the previous elif
        looping = True
        while looping:
          try: 
            #tries to obtain the necessary arguments
              num1 = int(input("What is the first number "))
              num2 = int(input("What is the second number "))
              operation = input("what operation would you like (multiply, sum, divide, subtract) ")
              looping = False
              
          #catches if the user inputs wrong input for the first two options (the method checks that they put in a valid operation)
          except ValueError:
              print("This is not a number, please try again")
    #if the user chooses 4
    elif choice == 4:
        #loops until the user's input is valid
        looping = True
        while looping:
            try:
                #tries to obtain the right values
                num1 = input("What number would you like to square ")
                looping = False
                #prints the output of the BasicMathOperations' square method when num1 is passed to it
                print(instance.square(num1))
            #if the user's input is invalid
            except ValueError:
                print("That is not a number, please try again ")
    #if the user chooses 5
    elif choice == 5:
        looping = True
        while looping:
            try:
                #tries to get the necessary arguments from the user
                num1 = int(input("What number would you like to get the factorial of "))
                looping = False
                print(instance.factorial(num1))
            except ValueError:
                print("That is not a number, please try again ")
    #if the user chooses 6
    elif choice == 6:
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments from the user
              num1 = int(input("What would you like to start the count with "))
              num2 = int(input("What number would you like to end the count with "))
              looping = False
              print(instance.counting(num1, num2))
          except ValueError:
              print("This is not a number, please try again")
    #if the user chooses 7
    elif choice == 7:
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments from the user
              num1 = int(input("What is the length of the base of the right triangle "))
              num2 = int(input("What is the length of the perpendicular of the right triangle "))
              looping = False
              print(instance.calculateHypotenuse(num1, num2))
          except ValueError:
              print("This is not a number, please try again")
    #if the user chooses 8
    elif choice == 8:
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments from the user
              num1 = int(input("What is the width of the rectangle "))
              num2 = int(input("What is the height of the rectangle "))
              looping = False
              print(instance.AreaRect(num1, num2))
          except ValueError:
              print("This is not a number, please try again")

    #if the user chooses 9
    elif choice == 9:
        looping = True
        while looping:
          try: 
              #tries to get the necessary arguments from the user
              num1 = int(input("What is the base number? "))
              num2 = int(input("What is the power number? "))
              looping = False
              print(instance.PowerOfNumber(num1, num2))
          except ValueError:
              print("This is not a number, please try again")
    #if the user chooses 10
    elif choice == 10:
              #doesnt need try/except because it accepts any data type
              arg = input("What is the argument ")
              print(instance.TypeOfArgument(arg))
    else:
        print("That is not one of the options")


main()