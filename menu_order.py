# Author: Sourav Das
# Date: 2025-06-12
# Description: This is a simple restaurant ordering system. The program displays a menu with items and prices,
#              allows the user to select one or two items to order, checks if the items are available,
#              and calculates the total cost of the selected items.



#Defining the menu of the restaurant 
menu ={
    "Burger" : 60,
    "Pizza" : 90,
    "Salad" : 70,
    "Pasta" : 120,
    "Coffee" : 40,
    "Water Bottle" : 10,
}

#Greet 
print("Welcome to our restaurant")
print("Burger: $60\nPizza: $90\nSalad: $70\nPasta: $120\nCoffee: $40\nWater Bottle: $10")

total_order = 0
item_1 = input("Enter the name of your item you want to order = ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaaiable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"Item {item_2} has been added to order")

    else:
        print(f"Ordered item {item_2} is not available!!")

print(f"The total amount of item is {total_order}")