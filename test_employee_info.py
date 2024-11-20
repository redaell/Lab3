import employee_info as ei
from employee_info import employee_data as ed

def test_get_employees_by_age_range():
    upper = 33
    lower = 29
    expected = [ed[0], ed[4]]
    result = ei.get_employees_by_age_range(lower,upper)
    assert(expected==result)

def test_calculate_average_salary():
    expected= 60166.67 # 1. input expected result
    result = ei.calculate_average_salary() # 2. get result by calling and executing the function of average salary
    assert(expected==result) # 3. check if expectations met the results

def test_get_employees_by_dept():
    targetdept = "Sales" # declare target dept. to check as sales
    expected=[ed[0], ed[5]] # for sales, array no. 0 and 5 are from sales
    result = ei.get_employees_by_dept(targetdept) # call function and execute using targetdept value, sales
    assert(expected==result) # check if results matches
