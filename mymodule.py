class student:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def printStudent(self):
     self.name =input("enter your name:")
     self.regno=input("enter the regno:")
     print("Name:"+self.name,"\nRegno:"+self.regno)
        