# Initialize variables
base_price = 10.0
topping_cost = 2.50
toppings_list = []
total_cost = base_price

# Start the loop to get toppings from the user
while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break  # Exit the loop if the user types 'quit'
    else:
        print(f"Adding {topping} to your pizza.")
        toppings_list.append(topping)
        total_cost += topping_cost

# After the loop, print the results
print("\n--- Your Pizza Summary ---")
if toppings_list:
    print("Toppings added:", ", ".join(toppings_list))
else:
    print("No toppings were added.")

print(f"Base price: ${base_price:.2f}")
print(f"Total cost: ${total_cost:.2f}")

