# Ask the user for their favorite fruits, separated by spaces, and store them in a list
favorite_fruits_input = ("avocado","mangoes","banana:")
favorite_fruits_list = favorite_fruits_input.split()

# Ask the user to input the name of any fruit
chosen_fruit = input("avocado:")

# Check if the chosen fruit is in their list of favorite fruits and print the appropriate message
if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
