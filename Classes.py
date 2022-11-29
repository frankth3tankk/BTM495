import json
import datetime
import uuid

randomID = uuid.uuid4()
#Classes and Methods
class Person:
    def __init__(self, firstname, lastname, phone_number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email 
        
class Employee(Person):
    def __init__(self, emp_id, emp_position, project, proposal, quote, contract, firstname, lastname, phone_number, email):
        Person.__init__(self, firstname, lastname, phone_number, email) 
        self.emp_id = emp_id
        self.emp_position = emp_position
        self.project = project
        self.proposal = proposal
        self.quote = quote
        self.contract = contract
      
    #Methods  
    def sign_contract(employee_signature):
        empSign = input("Please sign this contract:\n")
        print(f'You have signed this contract with this signature: {empSign}')
        empSign = Contract.employee_signature
        
class Client(Person):
    def __init__(self, id, address, type, project, inquiry, quote, contract, firstname, lastname, phone_number, email):
        Person.__init__(self, firstname, lastname, phone_number, email)
        self.id = id
        self.address = address
        self.type = type
        self.project = project
        self.inquiry = inquiry
        self.quote = quote
        self.contract = contract
              
    #Methods
    def sign_contract():
        clientSign = input("Please sign this contract:\n")
        print(f'You have signed this contract with this signature: {clientSign}')
        clientSign = Contract.client_signature 
       
    def generate_inquiry():
        newInquiry = Inquiry() 
        newInquiry.id = uuid.uuid4()
        print("ID: " + uuid.uuid4())
                    
class Contract:
    def __init__(self, id, description, release_state, employee_signature, client_signature, project, quote):
        self.id = id
        self.description = description
        self.release_state = release_state
        self.employee_signature = employee_signature
        self.client_signature = client_signature
        self.project = project
        self.quote = quote
        
    #Methods
    def send_contract(self):
        contractID = input("Enter the desired contract to be sent to the client:\n")
        Client.contract = input("Enter the desired Client ID\n")
        print(f'This contract {contractID} will be sent to the client {Client.contract}')
        if hasattr(Client, "_contract"):
            contractID = self.id = Client.contract
        else:
            Client.contract = Client()
        
    def add_stage_date(self):
       dates = input("Enter desired stage_dates:\n")
       print(f'These dates {dates} will be added to the Project')
       dates.append(Project.stage_dates)
              
    def add_quote(self):
       self.quote = Quote()

class Quote:
    def __init__(self, id, issue_date, cost, project, employee):
        self.id = id
        self.issue_date = issue_date
        self.cost = cost
        self.project = project
        self.employee = employee
        
    #Methods
    def send_quote(self):
        quoteId = input("Enter the quote ID to send to the contract:\n")
        Contract.quote = input("Enter the desired Contract ID\n")
        print(f'This quote {quoteId} will be sent to the contract {Contract.quote}')
        if hasattr(Contract, "_quote"):
            quoteId = self.id = Contract.quote 
        else:
            Contract.quote = Contract()
       
    def add_project(self):
       addproject = input("Enter desired project ID to add to this quote:\n")
       print(f'This project has been added to this quote: {addproject}')
       if hasattr(Project, '_id'):
           addproject = self.project = Project.id 
       else:
           addproject = Project(addproject)
               
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
        self.items = items
        self.client = client
        self.proposal = proposal
        self.quote = quote
        self.contract = contract
        self.furniture = furniture
        
    #Methods
    def change_furniture_reserved():
       date = input("Enter reserved date if the furniture:\n")
       print(f'The reserved date of this furniture is: {date}')
       date.append(Furniture.reserved_date)
       
    def add_quote(self):
       newQuote = input("Enter the ID of the desired Quote:\n")
       print(f'The ID of the desired Quote is: {newQuote}')
       if hasattr(Quote, '_id'):
           newQuote = Quote.id = self.quote
       else:
           newQuote = Quote(newQuote)
       
       #if hasattr(Quote, "_id"):
       #    return Quote._id
           
    def add_contract(self):
       newContract = input("Enter the ID of the desired Contract:\n")
       print(f'The ID of the desired Contract is: {newContract}')
       if hasattr(Contract, '_id'):
           newContract = Contract.id = self.contract
       else:
           newContract = Contract(newContract)
       
    def add_furniture():
       Furniture.id = input("Enter the ID of the desired Furniture:\n")
       print(f'The ID of the desired Furniture is: {Furniture.id}')
       Project.items.append(Furniture.id)
         
class Proposal(Project):
    def __init__(self, id, description, floor, number_of_rooms_to_fill, residence_type, dates_available_for_visit,  client, inquiry):
        self.id = id
        self.description = description
        self.floor = floor
        self.number_of_rooms_to_fill = number_of_rooms_to_fill
        self.residence_type = residence_type
        self.dates_available_for_visit = dates_available_for_visit
        self.client = client
        self.inquiry = inquiry
    
    #Methods    
    def modify_client_info(self):
        modInfo = input("Enter the revised Client information (Id, Adress, Type, Contract, Inquiry, Quote, Project): \n")
        print(f'The revised Client information is: {modInfo}')
        self.client = modInfo = Client()   
                          
class Inquiry(Project):
    def __init__(self, id, date, description, street_name, house_number, city, province, client):
        self.id = id
        self.date = date
        self.description = description
        self.street_name = street_name
        self.house_number = house_number
        self.city = city
        self.province = province
        self.client = client
  
    #Methods
    def create_profile(self):
        newClient = input("Enter the new Client information (Id, Adress, Type, Contract, Inquiry, Quote, Project): \n")
        print(f'The new Client information is: {newClient}')
        self.client = newClient = Client()
     
class Furniture:    
    def __init__(self, id, reserved_date, name, picture, address, project):
        self.id = id
        self.reserved_date = [reserved_date]
        self.name = name
        self.picture = picture
        self.address = address
        self.project = project
 
         
#Main function
def main():
    print("Welcome to Unique Home Solution!")
    role = input("Please enter your role below (Client or Employee):\n")
      
    if (role == "Client"):
        clientAction = input("To generate an inquiry type 'generate' or to sign a contract, please type 'sign':\n")
        print(f'You have chosen to {clientAction}')
        
        match clientAction:
            case "generate":
                Client.generate_inquiry()
                print("You have generated a new inquiry.")
                
            case "sign":
                Client.sign_contract()
                
            case _:
                print("Thank you for using our services! Have a nice day!")    
                   
        
    elif (input == "Employee"):
        employee = input({employee})
        
        
            

if __name__ == "__main__":
    main()

   
    
    
 
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