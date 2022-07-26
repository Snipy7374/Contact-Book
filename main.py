# Contact book project
from .my_database import MyDatabase

db = MyDatabase("ContactBook", "Contact")

class ContactBook:
  def __init__(self):
    pass
  
  def menu(self):
    print("Contact Book simple application\n\n1- Search a contact\n2- Add a contact\n3- Modify a contact\n4- Delete a contact\n5- Exit the program")
    user_in = input()
    return user_in.strip()

  def add_contact(self):
    print("\nAdding a new contact")
    name = input("Name: ")
    surname = input("Surname: ")
    number = input("Phone Number: ")
    email = input("Email: ")

    data = {
      "name": name,
      "surname": surname,
      "number": number,
      "email": email
    }
    db.insert_doc(data)

  def remove_contact(self):
    print("\nRemoving a contact by\n1- Name & Surname\n2- Phone number\n3- Email")
    option = input().strip()
    if option == '1':
      name = input("Name: ")
      surname = input("Surname: ")
      query = {
        "name": name,
        "surname": surname
      }
    elif option == '2':
      phone_number = input("Phone number: ")
      query = {"number": phone_number}
    elif option == '3':
      email = input("Email: ")
      query = {"email": email}

    try:
      db.delete_doc(query)
      print(query, "was removed")
    except:
      print("This contact is not present in the database")
    

  def search_contact(self):
    print("\nSearching a contact by\n1- Name\n2- Surname\n3- Name & Surname\n4- Phone number")
    option = input().strip()
    if option == '1':
      name = input("Name: ")
      query = {"name": name}
    elif option == '2':
      surname = input("Surname: ")
      query = {"surname": surname}
    elif option == '3':
      name = input("Name: ")
      surname = input("Surname: ")
      query = {
        "name": name,
        "surname": surname
      }
    elif option == '4':
      phone_number = input("Phone number: ")
      query = {"number": phone_number}

    try:
      data = db.find(query)
      out = [i for i in data]
      print(f"Result: {len(out)}")
      for i in range(len(out)):
        print(f"\n[{i}]\nName: {out[i]['name']}\nSurname: {out[i]['surname']}\nPhone number: {out[i]['number']}\nEmail: {out[i]['email']}\n")
      return out

    except:
      print("This contact cannot be found in our database")

  def modify_contact(self):
    print("To modify your contact first we need to search it")
    results = self.search_contact()

    choose = input("Select your contact writing the number: ")
    try:
      choose = int(choose)
    except:
      print("Invalid input, you need to write a number to pick a contact")
    
    picked_contact = results[choose]

    print(f"This contact will be modified\nName: {picked_contact['name']}\nSurname: {picked_contact['surname']}\nPhone number: {picked_contact['number']}\nEmail: {picked_contact['email']}")
    print("\nGetting the new information")
    name = input("Name: ")
    surname = input("Surname: ")
    phone_number = input("Phone number: ")
    email = input("Email: ")

    new_doc = {
      "name": name,
      "surname": surname,
      "number": phone_number,
      "email": email
    }
    query = {
      "name": picked_contact['name'],
      "surname": picked_contact['surname'],
      "number": picked_contact['number'],
      "email": picked_contact['email']
    }

    try:
      db.replace_doc(query, new_doc)

    except:
      print("Something went wrong on modify contact func")

contact = ContactBook()

while True:
  option = contact.menu()
  if option == '1':
    contact.search_contact()
  elif option == '2':
    contact.add_contact()
  elif option == '3':
    contact.modify_contact()
  elif option == '4':
    contact.remove_contact()
  elif option == '5':
    print("Exiting the program")
    break
