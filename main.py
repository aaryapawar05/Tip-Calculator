print("Welcome to the tip calculator!")
a=float(input("What was the total bill?"))
b=int(input("How much tip would you like to give?,10,12 or 15"))
c=int(input("How many people to split the bill?"))
bill_with_tip = b/100*a+a
d=bill_with_tip/c
final_amount= round(d,2)
print(f"each person should pay:${final_amount}")