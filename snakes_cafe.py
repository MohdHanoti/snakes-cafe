def order_function():
    n=1
    previous_order="none_none" 
    
    while True:
        
      order=input('**  What would you like to order?   **\n**************************************\n>')
      if order in menu:
        
        if order==previous_order:
          n+=1
        
        else:
          n=1
            
        print(f'\n** {n} order of {order} have been added to your meal **\n\n**************************************')
              
      elif order.lower()=="quit":

          print("""
          Tanks for your order
          ** Good bye **
          """)
          break     
      else:
        print(f"\n** your order '{order}' is not on the menu, please select from our menu\n")    
      previous_order=order
      
  

    
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
    "Wings",
    "Cookies",
    "Spring Rolls",
    "Salmon",
    "Steak",
    "Meat Tornado",
    "A literal Garden",
    "Ice Cream",
    "Cake",
    "Pie",
    "Coffee",
    "Tea",
    "Unicorn Tears"
    }

    order_function()
    