
#Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At  the end shownthe food items and the total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food product (or type 'exit' to finish): ")
    if food.lower() == 'exit':
        break
    price = input(f"Enter the price for {food}: ")
    
    try:
        price = float(price)
        foods.append(food)
        prices.append(price)
        total += price
    except ValueError:
        print("Please enter a valid price.")

# Display the shopping cart summary
print("\nShopping Cart Summary:")
for i in range(len(foods)):
    print(f"{foods[i]}: R{prices[i]:.2f}")
print(f"Total: R{total:.2f}")