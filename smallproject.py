# #############################هنا نبني كلاس الدمية ونعطيها خصائص عامة لكي يتم بنأ ابناء منها انهرتنس.. #######################
class Targetpractice:
    def __init__(self, health):
        self.health = health

    def displayhealth(self):
        return self.health


class robot(Targetpractice):
    pass



# ############################# Now we start with the wepons type #######################

class Wepon:
    def __init__(self, name, dmg, recoil, typee,):
        self.name = name
        self.dmg = dmg
        self.recoil = recoil
        self.typee = typee

    def wpninfo(self):
        print(self.name, "damege =", self.dmg, "wpn recoil =",
              self.recoil, "It's a", self.typee, "type")

    def wpndmg(self):
        return self.dmg


class heavywpn(Wepon):
    pass
# ##################################################### the work start's bellow ####################

# p20 = heavywpn("p20",200,"0","heavy")
# هنا تم تعين السلاح و تم اعطاؤه قيم مثل ضررة و ارتداده..
p20dmg = heavywpn("p20", 500, 55, "oo")
# اما هنا اخذنا فنكشن الظرر لكي يتم مقارنته مع صحة او الهلث التابع للدمية
p20dmg.wpndmg()
# print(p20dmg.wpndmg())
Roobot = robot(300)
Roobot.displayhealth()
# print(Roobot.displayhealth())


if p20dmg.wpndmg() > Roobot.displayhealth():
    print("wow the robot is dead")
elif p20dmg.wpndmg() < Roobot.displayhealth():
    print("this wepon is weak, the robot is not dead")
