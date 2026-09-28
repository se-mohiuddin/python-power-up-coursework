'''
Question: Shopping Cart
1. Create a class named CartItem to represent items in the cart. 
    Include attributes like name, price, quantity, and a method calculate_item_price().
2. Create subclasses for different item types, e.g., ElectronicsItem and ClothingItem etc.
    Override the calculate_item_price() method in each subclass.
3. Establish a class named ShoppingCart to represent the cart. Include an attribute items (a list) to store added items.
    Implement methods add_item(), remove_item(), and show_cart().
4. Inside the ShoppingCart class, implement a method calculate_total_price() to sum the prices of all items in the cart.
5. Instantiate objects of various item subclasses. Add these items to a ShoppingCart instance using add_item().
    Call calculate_total_price() on the cart to show the total price.
6. Create instances of items and the cart. Add items to the cart.
    Calculate and display the total cart price using calculate_total_price().
'''
class Cart_Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_item_price(self):
        return self.price * self.quantity

class Electronics_Item(Cart_Item):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years
        self.markup = 1 + self.warranty_years * 0.25
    def calculate_item_price(self):
        return super().calculate_item_price() * self.markup

class Clothing_Item(Cart_Item):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size
    
    def calculate_item_price(self):
        if self.size == 'S':
            self.markup = 10
        elif self.size == 'M':
            self.markup = 20
        elif self.size == 'L':
            self.markup = 30
        else:
            self.markup = 40
        return super().calculate_item_price()+self.markup

class Shopping_Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def show_cart(self):
        for item in self.items:
            print("\nItem: ", item.name, ", Quantity: ", item.quantity)

            if isinstance(item, Electronics_Item):
                print("Warranty: ", item.warranty_years, "years", ", Markup: ", item.markup)
                print("Price per item :", item.price * item.markup)
            elif isinstance(item, Clothing_Item):
                print("Size :", item.size, ", Markup: ", item.markup)
                print("Price per item :", item.price + item.markup)
            
            print("Total price :", item.calculate_item_price())
    
    def calculate_total_price(self):
        total_price = sum(item.calculate_item_price() for item in self.items)
        return total_price

item1 = Electronics_Item("Laptop", 20000, 2, 3)
item2 = Clothing_Item("T-shirt", 300, 5, "M")

cart = Shopping_Cart()

cart.add_item(item1)
cart.add_item(item2)

total_price = cart.calculate_total_price()
print(f"Total Cart Price: ${total_price:.2f}")

cart.show_cart()