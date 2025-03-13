


def calculatePrice(cost, revenue):
    price = cost/(1- revenue)
    print (price)


#calculatePrice(15000, 0.30)   


def ask_values():
    cost = float(input("Enter the cost of the product: "))
    revenue = float(input("Enter the revenue of the product: "))
    calculatePrice(cost, revenue)

ask_values()    

