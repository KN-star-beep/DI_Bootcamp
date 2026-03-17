# Initial list
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove "Banana"
basket.remove("Banana")

# 2. Remove "Blueberries"
basket.remove("Blueberries")

# 3. Add "Kiwi" to the end
basket.append("Kiwi")

# 4. Add "Apples" to the beginning
basket.insert(0, "Apples")

# 5. Count how many times "Apples" appear
apple_count = basket.count("Apples")
print(f"Count of 'Apples': {apple_count}")

# 6. Empty the list
basket.clear()

# 7. Print the final state
print(f"Final list: {basket}")
