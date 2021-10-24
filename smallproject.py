class Targetpractice:
    def __init__(self,health):
        self.health=health

class robot(Targetpractice):
    pass

class Wepon:
    def __init__(self,name,dmg,recoil,typee,) :
        self.name=name
        self.dmg=dmg
        self.recoil=recoil
        self.typee=typee


    def wpninfo(self):
        print(self.name,"damege =",self.dmg,"wpn recoil =",self.recoil,"It's a",self.typee,"type")

    def wpndmg(self):
        return self.dmg



class heavywpn(Wepon):
        pass



# p20 = heavywpn("p20",200,"0","heavy")
p20dmg = heavywpn("p20",200,55,"oo")
p20dmg.wpndmg()
# print(p20dmg.wpndmg())
Roobot = robot(200)
print(Roobot())


# if p20dmg.wpndmg() >Roobot():
#     print("wow the robot is dead")
# elif p20dmg.wpndmg() < Roobot():
#     print("this wepon is weak, the robot is not dead")





