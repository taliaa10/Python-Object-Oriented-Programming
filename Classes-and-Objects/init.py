class Employee:

    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)


employee = Employee('Mark')
employeeTwo = Employee('Matthew')
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()
