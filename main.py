# Contact book project
import pymongo
import os

class myDatabase:
  
  def __init__(self, db_name, collection_name) -> None:
    self.username = os.environ['username']
    self.password = os.environ['password']
    self.db_name = db_name
    self.collection_name = collection_name

  def _get_connection(self):
    client = pymongo.MongoClient(f"mongodb+srv://{self.username}:{self.password}@contactbookdb.lckvbig.mongodb.net/?retryWrites=true&w=majority")
    return client

  def _get_db(self):
    return self._get_connection()[f"{self.db_name}"]

  def _get_collection(self):
    return self._get_db()[f"{self.collection_name}"]

  def insert_doc(self, documents):
    return self._get_collection().insert_one(documents)

  def insert_many_doc(self, ls):
    return self._get_collection().insert_many(ls)

  def find(self, query):
    return self._get_collection().find(query)

  def update_doc(self, query, doc):
    return self._get_collection().update_one(query, doc)

  def replace_doc(self, query, doc):
    return self._get_collection().replace_one(query, doc)

  def delete_doc(self, query):
    return self._get_collection().delete_one(query)

  def delete_many_doc(self, query):
    return self._get_collection().delete_many(query)


db = myDatabase("ContactBook", "Contact")


class contactBook:
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
    option = input()
    if option.strip() == '1':
      name = input("Name: ")
      surname = input("Surname: ")
      query = {
        "name": name,
        "surname": surname
      }
    elif option.strip() == '2':
      phone_number = input("Phone number: ")
      query = {"number": phone_number}
    elif option.strip() == '3':
      email = input("Email: ")
      query = {"email": email}

    try:
      db.delete_doc(query)
      print(query, "was removed")
    except:
      print("This contact is not present in the database")
    

  def search_contact(self):
    print("\nSearching a contact by\n1- Name\n2- Surname\n3- Name & Surname\n4- Phone number")
    option = input()
    if option.strip() == '1':
      name = input("Name: ")
      query = {"name": name}
    elif option.strip() == '2':
      surname = input("Surname: ")
      query = {"surname": surname}
    elif option.strip() == '3':
      name = input("Name: ")
      surname = input("Surname: ")
      query = {
        "name": name,
        "surname": surname
      }
    elif option.strip() == '4':
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

while True:
  men = contactBook().menu()
  if men == '1':
    contactBook().search_contact()
  elif men == '2':
    contactBook().add_contact()
  elif men == '3':
    contactBook().modify_contact()
  elif men == '4':
    contactBook().remove_contact()
  elif men == '5':
    print("Exiting the program")
    break
