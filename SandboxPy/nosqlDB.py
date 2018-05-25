# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient("mongodb://dbuser1:dbuser1@ds161162.mlab.com:61162/pysand")
# Connect to the test db 
db=client.pysand

# Use the employee collection
employee = db.custOrders 
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}
result = employee.insert_one(employee_details)
print(result)