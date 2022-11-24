Rewrite soon

# Contact-Book
A simple contact book that works with the online database of [MongoDB](https://www.mongodb.com/ "MongoDB")

# Features
- Add a contact
- Search a contact
- Modify a contact
- Delete a contact

# Requirements
You can find all required libraries and versions in [Requirements.txt](https://github.com/Snipy7374/Contact-Book/blob/main/requirements.txt "Requirements.txt")

# Example database structure
```
| ContactBookDB     # Actually the real Cluster
| -- ContactBook    # Database name
|   |-- Contact     # Collection
```

# Example of documents
```py
{
  _id: ObjectId("..."),
  "name": "Snipy",
  "surname": "7374",
  "number": "1234567890",
  "email": "test@gmail.com"
}
