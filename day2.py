print("Welcome to the tip calculator!")
total_bill=float(input("What was your total bill? $"))
number_of_people=int(input("How many people to split the bill? "))
tip=float(input("What is the tip percentage?\n 10\n 12\n 15? "))
tip_calculate=total_bill+(total_bill*tip/100)
each_bill=tip_calculate/number_of_people
each_bill=round(each_bill,2)
print("Each person is paying $",each_bill)
