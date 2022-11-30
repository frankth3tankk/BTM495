import json
from json import JSONEncoder
from json import jsonpickle
import datetime
import uuid


# randomID = uuid.uuid4()
class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


# Classes and Methods
class Person:
    def __init__(self, firstname=None, lastname=None, phone_number=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email


class Employee(Person):
    def __init__(self, emp_id=None, emp_position=None, project=None, proposal=None, quote=None, contract=None,
                 firstname=None, lastname=None, phone_number=None,
                 email=None):
        Person.__init__(self, firstname, lastname, phone_number, email)
        self.emp_id = emp_id
        self.emp_position = emp_position
        self.project = project
        self.proposal = proposal
        self.quote = quote
        self.contract = contract

    # Methods
    def sign_contract(self):
        empSign = input("Please sign this contract:\n")
        print(f'You have signed this contract')
        sign = Contract()
        setattr(sign, 'client_signature', empSign)


class Client(Person):
    def __init__(self, id=None, address=None, type=None, project=None, inquiry=None, quote=None, contract=None,
                 firstname=None, lastname=None, phone_number=None, email=None):
        Person.__init__(self, firstname, lastname, phone_number, email)
        self.id = id
        self.address = address
        self.type = type
        self.project = project
        self.inquiry = inquiry
        self.quote = quote
        self.contract = contract

    # Methods
    def sign_contract(self):
        clientSign = input("Please sign this contract:\n")
        print(f'You have signed this contract')
        sign = Contract()
        setattr(sign, 'client_signature', clientSign)

    def generate_inquiry(self):
        newInquiry = Inquiry(1, 2022122, "This is a description", "Street", 123, "Montreal", "Quebec", self.id)
        print(MyEncoder().encode(newInquiry))
        print(newInquiry)


class Contract(Client):
    def __init__(self, id=None, description="Description", release_state=None, employee_signature=None,
                 client_signature=None, project=None, quote=None):
        self.id = id
        self.description = description
        self.release_state = release_state
        self.employee_signature = employee_signature
        self.client_signature = client_signature
        self.project = project
        self.quote = quote

    # Methods
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
    def __init__(self, id=None, issue_date=datetime, cost=None, project=None, employee=None):
        self.id = id
        self.issue_date = issue_date
        self.cost = cost
        self.project = project
        self.employee = employee

    # Methods
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
    def __init__(self, id=None, design_details="Description", design_sketch=None, description="Description",
                 status=None, feasibility=None, progress=None, requirements=None,
                 stage_dates=[], items=[], client=None, proposal=None, quote=None, contract=None, furniture=None):
        self.id = id
        self.design_details = design_details
        self.design_sketch = design_sketch
        self.description = description
        self.status = status
        self.feasibility = feasibility
        self.progress = progress
        self.requirements = requirements
        self.stage_dates = [stage_dates]
        self.items = [items]
        self.client = client
        self.proposal = proposal
        self.quote = quote
        self.contract = contract
        self.furniture = furniture

    # Methods
    def change_furniture_reserved(self):
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

        # if hasattr(Quote, "_id"):
        #    return Quote._id

    def add_contract(self):
        newContract = input("Enter the ID of the desired Contract:\n")
        print(f'The ID of the desired Contract is: {newContract}')
        if hasattr(Contract, '_id'):
            newContract = Contract.id = self.contract
        else:
            newContract = Contract(newContract)

    def add_furniture(self):
        addFurniture = Project()
        newID = input('Enter new id:\n')
        setattr(self, 'id', newID)
        newdd = input('Enter new design_details:\n')
        setattr(self, 'design_details', newdd)
        newds = input('Enter new design_sketch:\n')
        setattr(self, 'design_sketch', newds)
        newd = input('Enter new description:\n')
        setattr(self, 'description', newd)
        news = input('Enter new status:\n')
        setattr(self, 'status', news)
        newf = input('Enter new feasibility:\n')
        setattr(self, 'feasibility', newf)
        newp = input('Enter new progress:\n')
        setattr(self, 'progress', newp)
        newr = input('Enter new requirements:\n')
        setattr(self, 'requirements', newr)
        newsd = input('Enter new inquiry:\n')
        addFurniture.stage_dates.append(newsd)
        newi = input('Enter new items:\n')
        addFurniture.items.append(newi)
        newc = input('Enter new client:\n')
        setattr(self, 'client', newc)
        newp = input('Enter new proposal:\n')
        setattr(self, 'proposal', newp)
        newQuote = input('Enter new quote:\n')
        setattr(self, 'quote', newQuote)
        newContract = input('Enter new contract:\n')
        setattr(self, 'contract', newContract)
        newfur = input('Enter new furniture:\n')
        setattr(self, 'furniture', newfur)

        #print(MyEncoder().encode(addFurniture))
        with open('furniture.json', 'w') as outfile:
            json.dump(addFurniture, outfile)



        '''
        Furniture.id = input("Enter the ID of the desired Furniture:\n")
        print(f'The ID of the desired Furniture is: {Furniture.id}')
        Project.items.append(Furniture.id)
        '''

class Proposal(Project):
    def __init__(self, id=None, description="Description", floor=None, number_of_rooms_to_fill=None,
                 residence_type=None, dates_available_for_visit=None,
                 client=None, inquiry=None):
        self.id = id
        self.description = description
        self.floor = floor
        self.number_of_rooms_to_fill = number_of_rooms_to_fill
        self.residence_type = residence_type
        self.dates_available_for_visit = dates_available_for_visit
        self.client = client
        self.inquiry = inquiry

    # Methods
    def modify_client_info(self):
        newClient = Client()
        modify = input('Enter the number of the variable in need of change:\n-(1)firstname\n-(2)lastname\n-(3)phone_number\n-(4)email\n-(5)id\n-(6)address\n-(7)type\n-(8)contract\n-(9)inquiry\n-(10)quote\n-(11)Project\n')
        match modify:
            case "1":
                newFname = input('Enter new firstname:\n')
                setattr(newClient, 'firstname', newFname)
            case "2":
                newLname = input('Enter new lastname:\n')
                setattr(newClient, 'lastname', newLname)
            case "3":
                newPnum = input('Enter new phone_number:\n')
                setattr(newClient, 'phone_number', newPnum)
            case "4":
                newEmail = input('Enter new email:\n')
                setattr(newClient, 'email', newEmail)
            case "5":
                newID = input('Enter new id:\n')
                setattr(newClient, 'id', newID)
            case "6":
                newAddress = input('Enter new address:\n')
                setattr(newClient, 'address', newAddress)
            case "7":
                newtype = input('Enter new type:\n')
                setattr(newClient, 'type', newtype)
            case "8":
                newContract = input('Enter new contract:\n')
                setattr(newClient, 'contract', newContract)

            case "9":
                newInquiry = input('Enter new inquiry:\n')
                setattr(newClient, 'inquiry', newInquiry)
            case "10":
                newQuote = input('Enter new quote:\n')
                setattr(newClient, 'quote', newQuote)
            case "11":
                newProject = input('Enter new project:\n')
                setattr(newClient, 'project', newProject)
            case _:
                print("Exiting the software. Have a nice day!")

        print(MyEncoder().encode(newClient))
        print(newClient)


class Inquiry(Project):
    def __init__(self, id=None, date=datetime, description="Description:", street_name=None, house_number=None,
                 city="Montreal", province="Quebec", client=None):
        self.id = id
        self.date = date
        self.description = description
        self.street_name = street_name
        self.house_number = house_number
        self.city = city
        self.province = province
        self.client = client

    # Methods
    def create_profile(self):
        newClient = Client()

        newFname = input('Enter new firstname:\n')
        setattr(newClient, 'firstname', newFname)
        newLname = input('Enter new lastname:\n')
        setattr(newClient, 'lastname', newLname)
        newPnum = input('Enter new phone_number:\n')
        setattr(newClient, 'phone_number', newPnum)
        newEmail = input('Enter new email:\n')
        setattr(newClient, 'email', newEmail)
        newID = input('Enter new id:\n')
        setattr(newClient, 'id', newID)
        newAddress = input('Enter new address:\n')
        setattr(newClient, 'address', newAddress)
        newtype = input('Enter new type:\n')
        setattr(newClient, 'type', newtype)
        newContract = input('Enter new contract:\n')
        setattr(newClient, 'contract', newContract)
        newInquiry = input('Enter new inquiry:\n')
        setattr(newClient, 'inquiry', newInquiry)
        newQuote = input('Enter new quote:\n')
        setattr(newClient, 'quote', newQuote)
        newProject = input('Enter new project:\n')
        setattr(newClient, 'project', newProject)

        print(MyEncoder().encode(newClient))
        print(newClient)


class Furniture:
    def __init__(self, id=None, reserved_date=None, name=None, picture=None, address=None, project=None):
        self.id = id
        self.reserved_date = [reserved_date]
        self.name = name
        self.picture = picture
        self.address = address
        self.project = project


# Main function
def main():
    # obj = Inquiry()
    # obj1 = Client()
    # obj1.generate_inquiry()

    print("Welcome to Unique Home Solution!")
    role = input("Please enter your role below - Client (1) or Employee (2):\n")

    if (role == "1"):
        clientAction = input("To generate an inquiry type (1) or to sign a contract, type (2):\n")
        print('loading...')

        match clientAction:
            case "1":
                generate = Client()
                generate.generate_inquiry()

            case "2":
                sign = Client()
                sign.sign_contract()

            case _:
                print("Exiting the software. Thank you for using our services! Have a nice day!")


    elif (role == "2"):
        empAction = input(
            "Please type the desired option:\n-(1)Sign Contract\n-(2)Create Client Profile\n-(3)Modify Client Info\n-(4)Send Quote to Contract\n-(5)Add Project to Quote\n-(6)Change Furniture Reserved\n-(7)Add Quote to Project\n-(8)Add Contract to Project\n-(9)Add Furniture to the list\n")
        print('loading...')

        match empAction:
            case "1":
                # Sign Contract
                sign = Employee()
                sign.sign_contract()

            case "2":
                # Create Client Profile
                create = Inquiry()
                create.create_profile()

            case "3":
                # Modify Client Info
                create = Proposal()
                create.modify_client_info()
            case "4":
                # Send Quote to Contract
                return
            case "5":
                # Add Project to Quote
                return
            case "6":
                # Change Furniture Reserved
                return
            case "7":
                # Add Quote to Project
                return
            case "8":
                # Add Contract to Project
                return
            case "9":
                # Add Furniture to the list
                create = Project()
                create.add_furniture()
            case _:
                print("Exiting the software. Have a nice day!")


if __name__ == "__main__":
    main()
