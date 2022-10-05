def order_function():
    
    orders=[] 
    
    while True:
        
      order=input('**  What would you like to order?   **\n**************************************\n>')
      if order.lower() in menu:
        
        menu[order.lower()]+=1
            
        print(f'\n** {menu[order.lower()]} order of {order.capitalize()} have been added to your meal **\n\n**************************************')
        if order.capitalize() not in orders:
          
          orders.append(order.capitalize())

      elif order.lower()=="quit":
          print("Your final orders are:")
          for i in orders:
            
            print( f"{menu[i.lower()]} of {i}" )
          
          print("""
          Tanks for your order
          ** Good bye **
          """)
          break     
      else:
        print(f"\n** your order '{order}' is not on the menu, please select from our menu\n")

      
      
  

    
if __name__ == "__main__":
    print ("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print ("**************************************")
    print("Appetizers")
    print("----------")
    print("Wings \nCookies \nSpring Rolls")
    print("\nEntrees")
    print("-------")
    print("Salmon\nSteak\nMeat Tornado\nA Literal Garden")
    print("\nDesserts")
    print("--------")
    print("Ice Cream\nCake\nPie")
    print("\nDrinks")
    print("------")
    print("Coffee\nTea\nUnicorn Tears")
    print ("**************************************")
    menu = {
    "wings":0,
    "cookies":0,
    "spring rolls":0,
    "salmon":0,
    "steak":0,
    "seat sornado":0,
    "a literal garden":0,
    "ice cream":0,
    "cake":0,
    "pie":0,
    "coffee":0,
    "tea":0,
    "unicorn tears":0
    }

    order_function()
    