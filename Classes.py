import json
from json import JSONEncoder
import jsonpickle
import datetime
from os import path


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
        project = input("Enter the ID of the desired quote:\n")
        if hasattr(Contract, '_id'):
            Project(contract=project)
        else:
            print('Desired quote does not exist\n')

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
        newQuote = input("Enter the ID of the desired contract:\n")
        if hasattr(Quote, '_id'):
            Contract(quote=newQuote)
        else:
            print('Desired quote does not exist\n')

    def add_project(self):
        newProj = input("Enter the ID of the desired quote:\n")
        if hasattr(Project, '_id'):
            Quote(project=newProj)
        else:
            print('Desired quote does not exist\n')


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
        furniture = []
        with open('furniture.json', 'r+') as file:
            furniture = json.load(file)
            date = input('Enter the dates ID:\n')
            furniture[0]["stage_dates"] = date
            json.dump(furniture, file)
            print(furniture)
        '''for i in furniture:
            print(i)
            i = input('Enter the furniture ID:\n')
            iD = furniture[0]['id']
            if i == iD:
                dates = furniture['dates']
                print(dates)
'''



    def add_quote(self):
        newQuote = input("Enter the ID of the desired Quote:\n")
        if hasattr(Quote, '_id'):
            Project(quote=newQuote)
        else:
            print('Desired quote does not exist\n')

    def add_contract(self):
        newContract = input("Enter the ID of the desired contract:\n")
        if hasattr(Contract, '_id'):
            Project(contract=newContract)
        else:
            print('Desired quote does not exist\n')

    def add_furniture(self):
        furnitures = {}
        newID = input('Enter new id:\n')
        newdd = input('Enter new design_details:\n')
        newds = input('Enter new design_sketch:\n')
        newd = input('Enter new description:\n')
        news = input('Enter new status:\n')
        newf = input('Enter new feasibility:\n')
        newp = input('Enter new progress:\n')
        newr = input('Enter new requirements:\n')
        newsd = input('Enter new stage_dates:\n')
        newi = input('Enter new items:\n')
        newc = input('Enter new client:\n')
        newp = input('Enter new proposal:\n')
        newQuote = input('Enter new quote:\n')
        newContract = input('Enter new contract:\n')
        newfur = input('Enter new furniture:\n')
        for furniture in furnitures:
            furniture['id'] = newID
            furniture['design_details'] = newdd
            furniture['design_sketch'] = newds
            furniture['description'] = newd
            furniture['status'] = news
            furniture['feasibility'] = newf
            furniture['progress'] = newp
            furniture['requirements'] = newr
            furniture['stage_dates'] = newi
            furniture['client'] = newc
            furniture['quote'] = newp
            furniture['contract'] = newQuote
            furniture['inquiry'] = newContract
            furniture['furniture'] = newfur

        furnitures = [{'id': newID,
                       'design_details': newdd,
                       'design_sketch': newds,
                       'description': newd,
                       'status': news,
                       'feasibility': newf,
                       'progress': newp,
                       'requirements': newr,
                       'stage_dates': newi,
                       'client': newc,
                       'quote': newp,
                       'contract': newQuote,
                       'inquiry': newContract,
                       'furniture': newfur}]

        print(furnitures)
        newfurniture = json.dumps(furnitures)
        file = open('furniture.json', 'a')
        file.write('\n' + newfurniture)
        file.close()


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
        # newClient = Client()
        with open('clients.json', 'r+') as file:
            client = json.load(file)
        for x in client:
            print(x)
            i = input('Enter the Client ID:\n')
            iD = client[0]['id']
            if i == iD:
                client = {}
                modify = input(
                    'Enter the number of the variable in need of change:\n-(1)firstname\n-(2)lastname\n-(3)phone_number\n-(4)email\n-(5)id\n-(6)address\n-(7)type\n-(8)contract\n-(9)inquiry\n-(10)quote\n-(11)Project\n')
                match modify:
                    case "1":
                        newFname = input('Enter new firstname:\n')
                        client['firstname'] = newFname
                    case "2":
                        newLname = input('Enter new lastname:\n')
                        client['lastname'] = newLname
                    case "3":
                        newPnum = input('Enter new phone_number:\n')
                        client['phone_number'] = newPnum
                    case "4":
                        newEmail = input('Enter new email:\n')
                        client['email'] = newEmail
                    case "5":
                        newID = input('Enter new id:\n')
                        client['id'] = newID

                    case "6":
                        newAddress = input('Enter new address:\n')
                        client['address'] = newAddress
                    case "7":
                        newtype = input('Enter new type:\n')
                        client['type'] = newtype
                    case "8":
                        newContract = input('Enter new contract:\n')
                        client['contract'] = newContract
                    case "9":
                        newInquiry = input('Enter new inquiry:\n')
                        client['inquiry'] = newInquiry
                    case "10":
                        newQuote = input('Enter new quote:\n')
                        client['quote'] = newQuote
                    case "11":
                        newProject = input('Enter new project:\n')
                        client['project'] = newProject
                    case _:
                        print("Exiting the software. Have a nice day!")

            print(client)
            # json.dump(client, file)

    # f.close()


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
        clients = {}
        newFname = input('Enter new firstname:\n')
        newLname = input('Enter new lastname:\n')
        newPnum = input('Enter new phone_number:\n')
        newEmail = input('Enter new email:\n')
        newID = input('Enter new id:\n')
        newAddress = input('Enter new address:\n')
        newtype = input('Enter new type:\n')
        newContract = input('Enter new contract:\n')
        newInquiry = input('Enter new inquiry:\n')
        newQuote = input('Enter new quote:\n')
        newProject = input('Enter new project:\n')
        for client in clients:
            client['firstname'] = newFname
            client['lastname'] = newLname
            client['phone_number'] = newPnum
            client['email'] = newEmail
            client['id'] = newID
            client['address'] = newAddress
            client['type'] = newtype
            client['contract'] = newContract
            client['inquiry'] = newInquiry
            client['quote'] = newQuote
            client['project'] = newProject

        clients = [{'id': newID,
                    'firstname': newFname,
                    'lastname': newLname,
                    'phone_number': newPnum,
                    'email': newEmail,
                    'address': newAddress,
                    'type': newtype,
                    'contract': newContract,
                    'inquiry': newInquiry,
                    'quote': newQuote,
                    'project': newProject}]

        print(clients)
        newclient = json.dumps(clients)
        file = open('clients.json', 'a')
        file.write('\n' + newclient)
        file.close()


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
                create = Quote()
                create.send_quote()
            case "5":
                # Add Project to Quote
                create = Quote()
                create.add_project()
            case "6":
                # Change Furniture Reserved
                create = Project()
                create.change_furniture_reserved()
            case "7":
                # Add Quote to Project
                create = Project()
                create.add_quote()
            case "8":
                # Add Contract to Project
                create = Project()
                create.add_contract()
            case "9":
                # Add Furniture to the list
                create = Project()
                create.add_furniture()
            case _:
                print("Exiting the software. Have a nice day!")


if __name__ == "__main__":
    main()
