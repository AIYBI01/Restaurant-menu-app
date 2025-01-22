class RestaurantMenu:
  def init(self):
    self.menu_items = {}
    x
  def add_item(self, name, price):
    self.menu_items[name] = price

  def get_price(self, name):
    return self.menu_items.get(name, None)
    
  def remove_item(self, name):
        if name in self.menu_items:
            return True
        return False


  def main():

  def display_menu(self):
       print("Menu Items:")
       for item, price in self.menu_items.items():
          print (f"{item}: ${price:.2f}")  

def main():

  menu = RestaurantMenu()
  # Add initial menu items
  menu.add_item("Burger", 10.99)
  menu.add_item("Fries", 4.99)

if name == "main":
  main()
