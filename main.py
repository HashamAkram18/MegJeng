import numpy as np

def greeting(name):
    print(f"Hello, {name}!")

def age_adder(a,b):
    ans = np.dot(a,b)    
    print(f"your multiplier age is {ans} number of years")

if __name__ == "__main__":
    name = input("Enter your name: ")
    a = int(input("Enter your current age: "))
    b = int(input("Enter your end age: "))
    greeting(name)
    age_adder(a,b)


