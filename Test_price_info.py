import price_info as PI #step 1, import the function u want to test

def test_cost_of_fruit():
    fruitname = "pear"
    quantity = 5
    expected = 4.50
    result = PI.cost_of_fruits(fruitname, quantity) #remember to add "PI" so they know what library to take from
    assert(result == expected)


def test_total_cost():
    PI.quantity_list = quantity_list= {'apple': 5, 'orange':5, 'watermelon': 2, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    expected = 46.75 + 6.50
    result = PI.total_cost_shopping() 
    assert(result == expected)