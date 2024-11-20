# Define a list of 6 dictionaries to store 6 employees' information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def sort_employee_data(sortkey): 
    templist = employee_data.copy() #don't sort the original data, may want to keep original as it
    templist.sort(key=lambda x:x[sortkey]) #use sortkey instead of hardcoding it, so we can change to what we need to sort
    return templist

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result

def calculate_average_salary():
    total = 0
    average = 0
    for everyitem in employee_data: #iterate through every item in employee data
        employeesalary = everyitem["salary"] # for every item named salary, store it in employeesalary
        total += employeesalary #for every employee salary value, store it in total

<<<<<<< HEAD
    average = total/len(employee_data) #average is the total divided by the count of the total no. of rows
    average=round(average,2)
    return average #return this value so it can be used elsewhere

def get_employees_by_dept(department):
    result = [] #initialise an empty array to store the selected deptments
    for everyitem in employee_data: #for every item in employee data,
        if everyitem["department"] == department: #check if the department matches
            result.append(everyitem) #if match, add the result from everyitem to result
    return result #return and display 
=======
    for everyDictionary in employee_data:
        employeeSalary = everyDictionary["salary"] #retrieve employee salary from all dictionaries
        total += employeeSalary

    average = total / len(employee_data) #length of the employee_data is equal to no. of employees
    average = round(average, 2) #round average to 2 d.p.
    return average

def get_employees_by_dept(targetdept):
    result = [] # A empty list, to be filled in with selected dictionaries

    for everyDictionary in employee_data: #loop through all data in employee_data
        if everyDictionary["department"] == targetdept:
            result.append(everyDictionary) #if department is same as our target, add to list using append
    return result
>>>>>>> 3060b4e0071bfdcfbe9868dc7f0f6f429dc49629

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")
    print ("5 - Display all records according to age")
    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()

    elif option == '2':
        average_salary = calculate_average_salary()
        print("Average salary = " + str(average_salary))

    elif option == '3':
        age_lower_limit = input("age (Lower Limit) = ")
        age_upper_limit = input("age (Uper Limit) = ")
        employee_info = get_employees_by_age_range(age_lower_limit, age_upper_limit)
        display_records(employee_info)


    elif option == '4':
        department = input("Name of Department = ")
        employee_info = get_employees_by_dept(department)
        display_records(employee_info)

    elif option == '5':
        #ask for key to be usd for sorting
        sortkey = input("Enter key for sorting = ")
        newlist = sort_employee_data(sortkey)
        display_records(newlist)

    elif option == 'Q':
        quit()

def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()