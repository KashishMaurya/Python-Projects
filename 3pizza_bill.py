print("Welcome to Python Pizza Deliveries!")

total_bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
else:
    total_bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is: ${total_bill}.")
