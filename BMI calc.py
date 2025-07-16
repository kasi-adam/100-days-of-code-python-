print("Hello, and welcome to my BMI calculator!")
weight=int(input("Your weight in kg:"))
height=float(input("Your height in m:"))
BMI=weight/height**2
print("Your BMI is:",round(BMI,2))