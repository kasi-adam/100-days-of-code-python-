print("Hello, and welcome to my BMI calculator!")
weight=int(input("Your weight in kg:"))
height=float(input("Your height in m:"))
BMI=round(weight/height**2)
if BMI < 18.5:
    print(f"your bmi is {BMI} you are underweight")
elif BMI <25:
    print(f"your bmi is {BMI} you are normal weight")
elif BMI < 30:
    print(f"your bmi is {BMI} you are overweight")
elif BMI < 35:
    print(f"your bmi is {BMI} you are slightly overweight")
else:
    print(f"your bmi is {BMI} you are clinically obese")

