items = []
prices = []
total = 0

while True:
    item = input("Enter the food name(q to quit): ")
    if item.lower() == 'q':
        break
    else:
        price = int(input("Enter the price of the item: "))
        items.append(item)
        prices.append(price)

print("=====YOUR CART=====")

for item in items:
    print(item, end= ", ")

print("\n=====PRICES=====")

for price in prices:
    print(price, end= ", ")
    total += price

print(f"\nTotal price: {total}" )