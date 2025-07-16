print("WELCOME TO TIP CALCULATOR!")
total_bill=float(input("what was the total bill?"))
tip=int(input("what percentage tip would you like to give?: 10, 12, 15?"))
people=int(input("How many people are splitting the bill?"))
percent_tip=tip/100
current_bill=total_bill*percent_tip
new_bill=current_bill+total_bill
each_person=round(new_bill/people,2)
print(f"each person is gonna pay {each_person} $")
