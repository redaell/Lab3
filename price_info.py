
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def print_fruit_price_and_quantity(whatfruit):
    fruitprice = price_list[whatfruit]
    fruitquantity = quantity_list[whatfruit]
    print("Price of "+whatfruit+ " is", fruitprice)
    print("Quantity to buy is ", fruitquantity)

def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys(): 
        if key in quantity_list:
<<<<<<< HEAD
            total_cost += (price_list[key] * quantity_list[key])
    print("total cost = ", total_cost)
    return total_cost
=======
            # complete the implementation below:
            total_cost += (price_list[key] * quantity_list[key])
    print("total cost = ", total_cost)
    return total_cost

>>>>>>> 3060b4e0071bfdcfbe9868dc7f0f6f429dc49629

def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
<<<<<<< HEAD
        return cost

=======
            break
>>>>>>> 3060b4e0071bfdcfbe9868dc7f0f6f429dc49629
    print("cost of ", quantity, fruit, "=", cost)
    return cost




def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()
    print_fruit_price_and_quantity("apple")


if __name__ == "__main__":
    main()