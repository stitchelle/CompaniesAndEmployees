class Employee:

    def __init__(self, name, job_title, employment_start_date):
        self.name = name
        self.job_title = job_title
        self.employment_start_date = employment_start_date

class Company:
    def __init__(self, name, address, industry_type):
        self.business_name = name
        self.address = address
        self.industry_type = industry_type
        self.employees = []

first_tennessee = Company("First Tennessee", "Murfreesboro", "Bank")
taco_bell = Company("Taco Bell", "Franklin", "Resturaunt")

mo = Employee("Mo", "Cook", "12-4-2019")
warner = Employee("Warner", "Teller", "7-15-2012")
ken = Employee("Ken", "Cashier", "8-25-2012")
sam = Employee("Sam", "Teller", "4-14-2016")
mary = Employee("Mary", "Receptionist", "7-8-2018")

first_tennessee.employees.append(mo)
first_tennessee.employees.append(warner)
taco_bell.employees.append(ken)
taco_bell.employees.append(sam)
taco_bell.employees.append(mary)

company_list = [first_tennessee, taco_bell]

for list in company_list:
    print(f'{list.business_name} is in the {list.industry_type} and has the following employees')

    for employee in list.employees: 
        print(f'*{employee.name}')
