employee_file = open("employees.txt", "r")
print(employee_file.readable()) # readable >>> will return a boolean value. .
# print(employee_file.read()) # entire text
# print(employee_file.readline()) # one by one next line
# print(employee_file.readlines()) # List
# print(employee_file.readlines()[1]) # specific line from list by index
# print(employee_file.readline())

for employee in employee_file.readlines():   # to print all list by using for loop
    print(employee)
employee_file.close()