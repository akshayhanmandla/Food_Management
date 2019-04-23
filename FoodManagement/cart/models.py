from pymongo import MongoClient
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import pprint
from bson.objectid import ObjectId

class Order:
    def __init__(self):
        Client = MongoClient('localhost:27017')
        Db = Client.FoodManagement
        self.Order = Db.Order

    def Create(self, Orders, NGOId):
        Now = datetime.datetime.now()
        order = {
            'Orders': Orders,
            'NGOId': NGOId,
            'CreatedDate': Now,
            'LastModifiedDate': Now
        }
        pprint.pprint(order)
        try:
            Id = self.Order.insert_one(order).inserted_id
            if Id:
                print("CREATE: Successful")
                return 1
        except Exception as ex:
            print (ex)
            print ("CREATE: Unsuccessful")
            return 0

    def Retrieve(self, Id):
        Data = self.Order.find({'NGOId': Id}).sort('LastModifiedDate', -1)
        Result = []
        for I in Data:
            I['_id'] = str(I['_id'])
            Result.append(I)
        return Result

    def RetrieveForKitchen(self, KitchenId):
        Data = self.Order.find({'Orders.KitchenId': KitchenId}).sort('LastModifiedDate', -1)
        Result = []
        for I in Data:
            I['_id'] = str(I['_id'])
            Result.append(I)
        return Result