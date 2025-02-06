import pymongo
print("1")

myclient = pymongo.MongoClient("mongodb+srv://hiteshjethava:Hitesh1593@cluster0.jspdn.mongodb.net/")
mydb = myclient["assignmenttry"]

coll = mydb["assignmenttry"]
x=coll.find_one()
print(x)
for i in coll.find():
    print(i)