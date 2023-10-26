class sportmart:
    def __init__(self):
        self.inventory ={}
        self.orders ={}
    def createInventory(self, productid,product,quantity,price):
        temp ={
            "productid":productid,
            "productname":product,
            "quantity":quantity,
            "price":price
        }
        self.inventory[productid]=temp

    def createOrders(self,orderid,productid,quantity,price,total):
        temp ={
            "orderid":orderid,
            "productid":productid,
            "quantity":quantity,
            "price":price,
            "total":total
        }
        self.orders[orderid]=temp
    def printOrders(self):
        print(self.orders)
    def printInventory(self):
        print(self.inventory)

trinity = sportmart()
orders = open("orders.csv","r")
o_header = orders.readline()
o_data = orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createOrders(tmp[0],tmp[1],tmp[2],tmp[3],tmp[4])
trinity.printOrders()
inventory = open("inventory.csv","r")
i_header = inventory.readline()
i_data = inventory.readlines()
for data in i_data:
    tmp = data.strip().split(',')
    trinity.createInventory(tmp[0],tmp[1],tmp[2],tmp[3])
trinity.printInventory()
