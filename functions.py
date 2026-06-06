def attribute():
    users_name=input("what is your name? ")
    age=input("what is your age? ")
    height=float(input("How tall are you? "))
    weight=float(input("what is your weight? "))
    question=input("Should i calculate your BMI?")
    if question=="yes":
        BMI=weight/(height**2)
        BMI=round(BMI,2)
        print("Your BMI is:",BMI)
    else:
        print("ok")
attribute()