from pymongo import MongoClient
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import pprint
from bson.objectid import ObjectId

class Stock:
    def __init__(self):
        Client = MongoClient('localhost:27017')
        Db = Client.FoodManagement
        self.Stock = Db.Stock

    def Create(self, Name, Quantity, Veg, KitchenId):
        Now = datetime.datetime.now()
        stock = {
            'Name': Name,
            'Quantity': Quantity,
            'Veg': Veg,
            'KitchenId': KitchenId,
            'Status': 1,
            'CreatedDate': Now,
            'LastModifiedDate': Now
        }
        pprint.pprint(stock)
        try:
            Id = self.Stock.insert_one(stock).inserted_id
            if Id:
                print("CREATE: Successful")
                return 1
        except Exception as ex:
            print (ex)
            print ("CREATE: Unsuccessful")
            return 0

    def Retrieve(self, Id = None):
        if Id is None:
            Data = self.Stock.find({"Quantity": {"$gt": 0}}).sort('LastModifiedDate', -1)
        else:
            Data = self.Stock.find({"KitchenId": Id, "Quantity": {"$gt": 0}}).sort('LastModifiedDate', -1)
        Result = []
        for I in Data:
            I['_id'] = str(I['_id'])
            Result.append(I)
        return Result
    
    def RetrieveSingle(self, Id):
        Data = self.Stock.find({"_id": ObjectId(Id)}).sort('LastModifiedDate', -1)
        Result = []
        for I in Data:
            I['_id'] = str(I['_id'])
            Result.append(I)
        return Result

    def Update(self, Name, Quantity, Veg, KitchenId):
        Now = datetime.datetime.now()
        stock = {
            'Quantity': Quantity,
            'Veg': Veg,
            'KitchenId': KitchenId,
            'LastModifiedDate': Now
        }
        MyQuery = {"Name": Name}
        print (MyQuery)
        NewValues = {"$set": stock}
        print (NewValues)
        try:
            Result = self.Stock.update_one(MyQuery, NewValues)
            if int(Result.matched_count) == 1:
                print ("UPDATE: Successful")
                return 1
        except Exception as ex:
            print (ex)
            print ("UPDATE: Unsuccessful")
            return 0

# S = Stock()
# Name = 'Biryani'
# Quantity = 2
# Veg = 1
# KitchenId = '5c8d120f5f627d1c78e72f4d'
# Result = S.Create(Name, Quantity, Veg, KitchenId)

# S = Stock()
# Result = S.Retrieve() 
# for I in Result:
#     print (I)       

# S = Stock()
# Name = 'cheese'
# Quantity = 6
# Veg = 0
# KitchenId = '5c8d120f5f627d1c78e72f4d'
# Result = S.Update(Name, Quantity, Veg, KitchenId)
# print (Result)

# S = Stock()
# Id = '5c8d50985f627d5aac2095c0'
# Result = S.RetrieveSingle(Id)
# pprint.pprint(Result)