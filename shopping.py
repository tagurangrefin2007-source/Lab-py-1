# Define the Item class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Define the ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.name} added to cart.")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"{item.name} removed from cart.")
                return
        print("Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return
        total = 0
        print("\nYour Cart:")
        for item in self.items:
            print(f"{item.name} - ${item.price}")
            total += item.price
        print("Total:", total)

    def checkout(self):
        total = sum(item.price for item in self.items)
        print("\nCheckout Total:", total)
        print("Thanks for shopping at GamingStore!")

# Predefined store items
store_items = [
    Item("Roblox", 50),
    Item("Minecraft", 20),
    Item("Dota 2", 35),
    Item("Valorant", 40)
]

cart = ShoppingCart()

print("Welcome to GamingStore!")

while True:
    print("\n1. View Store")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Cart")
    print("5. Checkout")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nAvailable Games:")
        for i, item in enumerate(store_items):
            print(f"{i+1}. {item.name} - ${item.price}")

    elif choice == "2":
        num = int(input("Enter item number to add: ")) - 1
        if 0 <= num < len(store_items):
            cart.add_item(store_items[num])
        else:
            print("Invalid item.")

    elif choice == "3":
        name = input("Enter game name to remove: ")
        cart.remove_item(name)

    elif choice == "4":
        cart.view_cart()

    elif choice == "5":
        cart.checkout()
        break

    else:
        print("Invalid choice.")