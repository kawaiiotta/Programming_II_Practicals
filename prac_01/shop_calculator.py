# Calculate Discounts

total_price = 0
items = int(input("Number of Items: "))
while items < 0:
    print("Wrong input")
    items = int(input("Number of Items: "))

if items == 0:
    print("You have 0 items")
else:
    for i in range(0, items):
        price = float(input("Price of Item: "))
        total_price += price

    print(f"Total price for {items} items is ${total_price:.2f}")
