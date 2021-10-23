

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


# this is the perant 
# from _typeshed import Self


# class Huomann:
#     def __init__(self, finame, laname, age):
#         self.finame = finame
#         self.laname = laname
#         self.age = age

#     def printhmninfo(self):
#         print("First name",self.finame,"Last name",self.laname, "He is",self.age,"Years old")

# # This is one of "Huomann"'s shldren....
# class momad(Huomann):
#     pass


# x = momad("mohammed", "ali", 30)
# x.printhmninfo()


# class Targetpractice:
#     def __init__(self,health):
#         self.health=health


class Wepon:
    def __init__(self,name,dmg,recoil,typee,) :
        self.name=name
        self.dmg=dmg
        self.recoil=recoil
        self.typee=typee

    def fast(self):
        print("this  webon is fast")

    def slow(self):
        print("this wepon iz vry slow")

    def wpninfo(self):
        print(self.name,"damege =",self.dmg,"wpn recoil =",self.recoil,"It's a",self.typee,"type")


class g20(Wepon):
    pass

gg20 = g20("g20",200,180,"heavy")
gg20.wpninfo()

