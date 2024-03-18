from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees=Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    employee_name= input("Find Name:")
    name=Employee.find_by_name(employee_name)
    print(name) if name else print (f'No {name} in our database')
    


def find_employee_by_id():
    employee_id= input("Find ID:")
    id=Employee.find_by_id(employee_id)
    print(id) if id else print (f'No {id} in our database')


def create_employee():
    name=input('Employee Name is:')
    job_title=input('Job Title is:')
    department=input('Department is:')
    try:
        employee= Department.create(name, job_title, department)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating department: ", exc)
    


def update_employee():
    id_=input('Employee id')
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employees's new name: ")
            employee.name = name
            job_title = input("Enter the employees's jon: ")
            employee.job_title= job_title
            department=input("Enter the new department:")
            employee.department=department

            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')



def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    department=input('Department Id:')
    employees= Employee.find_by_id(department)
    if employees:
        department_employees=Employee.department_id(employees, department)
        if department_employees:
            for employee in department_employees:
                print(employee)