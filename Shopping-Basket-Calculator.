item = []
price = []

print("Welcome to iShop Calculator")
ask = int(input("How many items are there in your basket today? "))
print("Let us continue with them...")

for i in range(0, ask):
    item_user = input(f"Please tell me the name of item number {i + 1}:\n")
    item.append(item_user)
    price_user = int(input(f"What is the price of {item_user}?\n"))
    price.append(price_user)
    print("******")

option = input("Would you like to see your entire basket items? ")
if option.lower() == "yes":
    print(item)
else:
    input("Press Enter to exit.")

cost = input("Would you like to see how much it will cost? ")
if cost.lower() == "yes":
    print("Buying this costs:")
    print(sum(price))
else:
    input("Press Enter to exit.")
