#List of classes and methods for the Use case

#Example:
""" 
class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)
"""

class Employee:
    def __init__(self, emp_id, emp_f_name, emp_l_name, emp_phone_num, emp_position):
        self.emp_id = emp_id
        self.emp_f_name = emp_f_name
        self.emp_l_name = emp_l_name
        self.emp_phone_num = emp_phone_num
        self.emp_position = emp_position
        
    def enrol(self, sign_contract):
        sign_contract(Contract)
        
    
class Client:
    def __init__(self, id, phone_number, f_name, l_name, address, type):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.phone_number = phone_number
        self.address = address
        self.type = type
              
    def enrol(self, sign_contract, approve_quote, pay_invoice, generate_inquiry):
        sign_contract(Contract)
        approve_quote(Quote)
        pay_invoice(Invoice)
        generate_inquiry(Inquiry)
        
        
class Contract:
    def __init__(self, contract_ID, release_state):
        self.contract_ID = contract_ID
        self.release_state = release_state
        
    def enrol(self, employee_signature, client_signature):
        employee_signature(Employee)
        client_signature(Client)

class Quote:
    def __init__(self, quote_ID, issue_date, cost):
        self.quote_ID = quote_ID
        self.issue_date = issue_date
        self.cost = cost
        
class Invoice:
    def __init__(self, invoice_ID, amount, invoice_type, date_due):
        self.invoice_ID = invoice_ID
        self.amount = amount
        self.invoice_type = invoice_type
        self.date_due = date_due
        
    def enrol(self, charge_full_price, charge_repairs, charge_project):
        charge_full_price(Furniture)
        charge_repairs(Furniture)
        charge_project(Project)

         
class Inquiry:
     def __init__(self):
        self
     
class Proposal:       
    def __init__(self):
        self
     
class Project:
    def __init__(self):
        self
     
class Furniture:    
    def __init__(self):
        self
         
        