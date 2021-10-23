

# class Drinkk:
#     def __init__(self,type,gass_or_not,sizee):

#         self.type=type

#         self.gass_or_not=gass_or_not

#         self.sizee=sizee

#     def __init__(self) :
#         print("injoi ur drink")

# gd = Drinkk("ghazy","yes",440)


# print(gd.type)


# create a human class and inharete its attributes with an outher class

class Huomann:
    def __init__(self, finame, laname, age):
        self.finame = finame
        self.laname = laname
        self.age = age

    def printhmninfo(self):
        print("First name",self.finame,"Last name",self.laname, "He is",self.age,"Years old")


class momad(Huomann):
    pass


x = momad("mohammed", "ali", 30)
x.printhmninfo()
