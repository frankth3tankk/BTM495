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
    def __init__(self, emp_id, emp_position, project, proposal, quote, contract):
        self.emp_id = emp_id
        self.emp_position = emp_position
        project(Project)
        proposal(Proposal)
        quote[Quote]
        contract[Contract]
      
    #Methods  
    def sign_contract(employee_signature):
        Contract.append(employee_signature)
        
class Client:
    def __init__(self, id, address, type, project, inquiry, quote, contract):
        self.id = id
        self.address = address
        self.type = type
        project(Project)
        inquiry[Inquiry]
        quote[Quote]
        contract[Contract]
              
    #Methods
    def sign_contract(self):
       self 
       
    def generate_inquiry(self):
       self
            
class Person:
    def __init__(self, firstname, lastname, phone_number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email 
              
class Contract:
    def __init__(self, id, description, release_state, employee_signature, client_signature, project, quote):
        self.id = id
        self.description = description
        self.release_state = release_state
        employee_signature(Employee)
        client_signature(Client)
        project(Project)
        quote(Quote)
        
    #Methods
    def send_contract(self):
        self
        
    def add_stage_date(self):
       self 
       
    def add_quote(self):
       self

class Quote:
    def __init__(self, id, issue_date, cost, project, employee, send_quote, add_project):
        self.id = id
        self.issue_date = issue_date
        self.cost = cost
        project(Project)
        employee(Employee)
        
    #Methods
    def send_quote(self):
       self 
       
    def add_project(self):
       self
        
class Project:       
    def __init__(self, id, design_details, design_sketch, description, status, feasibility, progress, requirements, stage_dates, items, client, proposal, quote, contract, furniture):
        self.id = id
        self.design_details = design_details
        self.design_sketch = design_sketch
        self.description = description
        self.status = status
        self.feasibility = feasibility
        self.progress = progress
        self.requirements = requirements
        self.stage_dates = [stage_dates]
        items[Furniture]
        client(Client)
        proposal(Proposal)
        quote(Quote)
        contract(Contract)
        furniture(Contract)
        
    #Methods
    def change_furniture_reserved(self):
       self
       
    def add_quote(self):
       self
       
    def add_contract(self):
       self
       
    def add_furniture(self):
       self 
         
class Proposal(Project):
    def __init__(self, id, description, floor, number_of_rooms_to_fill, residence_type, dates_available_for_visit, client, inquiry):
        self.id = id
        self.description = description
        self.floor = floor
        self.number_of_rooms_to_fill = number_of_rooms_to_fill
        self.residence_type = residence_type
        self.dates_available_for_visit = dates_available_for_visit
        client(Client)
        inquiry(Inquiry)
    
    #Methods    
    def modify_client_info(self):
        self   
                          
class Inquiry(Project):
    def __init__(self, id, date, description, street_name, house_number, city, province, client):
        self.id = id
        self.date = date
        self.description = description
        self.street_name = street_name
        self.house_number = house_number
        self.city = city
        self.province = province
        client(Client)
  
    #Methods
    def create_profile(self):
        self
     
class Furniture:    
    def __init__(self, id, reserved_date, name, picture, address, project):
        self.id = id
        self.reserved_date = [reserved_date]
        self.name = name
        self.picture = picture
        self.address = address
        project(Project)
         
    
    
    
 
'''
if client.exist()
    fetch client_id()
else
    create_profile.new(Client) and create.client_id() and fetch client_id()
    
with open("furniture.json", "w") as write_file:
    json.dump(furniture, write_file) 
    
client = {
    "furniture1": [{"furniture_reserved", "date" }],
    "furniture2": [{"furniture_reserved", "date" }],
    "furniture3": [{"furniture_reserved", "date" }] 
} 

assign date to furniture() 

available = True

if Furniture.furniture_reserved = Project.stage_dates
    append().furniture_reserved as available = false
else if
    append().furniture_reserved as available
 
if available = true   
    append() project_items[Furniture]

'''