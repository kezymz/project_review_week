print("welcome, here are the entrance prices")
items = ['adult £20', 'child £12', 'senior citizen £11', 'wristband £20']
wristband = 20 
for x in items:
    print(x)
order = []
total = 0.00
print("how many adult tickets are required?")
adult_cost = int(input())
order.append(items[0])
multiply = adult_cost * 20
total += multiply
print(total)
print("how many child tickets are required?")
child_cost = int(input())
order.append(items[1])
multiply = child_cost * 12
total += multiply
print(total)
print("how many senior tickets are required?")
senior_cost = int(input())
order.append(items[2])
multiply = senior_cost * 11
total += multiply 
print(total)
print("how many wristbands would you like for the rides?")
wristband = int(input())
order.append(items[3])
multiply = wristband * 20
total += multiply
print("enter leader book surname for tickets:")
input()
parking_pass = "free"
print("do you a require parking pass?:")
option = input().lower()
if option == "yes":
    print("Parking pass")
else:
    print("No parking pass")
print(f"your total is {total}")
print("this machine only accepts £10 and £20 notes")
payment = 0.00
balance = total

while payment < total:
    print("how would you like to pay? 1 for £10 or 2 for £20")
    answer = input()
    if answer == "1":
        payment += 10
        balance -= 10
        print(f"you have {balance} left to pay")
    elif answer == "2":
        payment += 20 
        balance -= 20
        print(f"you have {balance} left to pay")
    else:
        print("not available")
change = payment - total 
print(f"your final balance is {payment}")
print(f"your change is {change}")


 


