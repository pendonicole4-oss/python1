from datatypes import first_name


class Employee:
    def __init__(self,first_name,last_name,department,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.department=department
        self.salary=salary
    #this returns a readable string when you print object
    def __str__(self):
        return f'Name :{self.first_name} {self.last_name}, Department: {self.department}, Salary: {self.salary} '
    #returns annual salary
    def annual_salary(self):
        return f'{self.salary*12}'
    #returns weekly pay
    def weekly_pay(self):
        return f"{self.salary/4}"



employee1=Employee("Rebecca","Gichuru","Adminstration",150000)
employee2=Employee("Tatiana","Wanjira","Finance",190000)
employee3=Employee("Cecilia","Mutheu","Clerk",56000)
print(employee1)
print(employee2)
print(employee3)
#accessing the attribute value
print(employee1.first_name)
print(employee2.department)
#printing object
print(f"{employee1.first_name}'s annual salary is {employee1.annual_salary()}")
print(f"{employee2.last_name}'s annual salary is {employee2.annual_salary()}")
print(f"{employee1.first_name} {employee1.last_name}'s weekly pay is {employee1.weekly_pay()}")
print(f"{employee2.first_name} {employee2.last_name}'s weekly pay is {employee2.weekly_pay()}")
