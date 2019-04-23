from pymongo import MongoClient
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import pprint

class Customer:
    def __init__(self):
        Client = MongoClient('localhost:27017')
        Db = Client.FoodManagement
        self.Customer = Db.Customer

    def Create(self, Name, Email, PhoneNumber, Password, Type):
        Now = datetime.datetime.now()
        hash = generate_password_hash(Password)
        customer = {
            'Name': Name,
            'Email': Email,
            'PhoneNumber': PhoneNumber,
            'Password': hash,
            'Type': Type,
            'CreatedDate': Now,
            'LastModifiedDate': Now
        }
        pprint.pprint(customer)
        try:
            Id = self.Customer.insert_one(customer).inserted_id
            if Id:
                print("CREATE: Successful")
                return 1
        except Exception as ex:
            print (ex)
            print ("CREATE: Unsuccessful")
            return 0
