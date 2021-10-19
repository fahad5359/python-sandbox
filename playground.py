# from HW2 import summ


# print("hey")

# ###########################functions ###########################
# to write a function in python u need to write de name():

# def sum():
#     print("the function is workng")

# meh =sum();
# print(meh)

# def summm(a,b):
#     return a+b
# print(summm(5,5))
  

############################ dictionarys and for loops ############################
 

# cars ={
#     "offroud": "jeep,buggy",
#     "highwua": "labo,camry",
#     "trucks": "marcades, gallab"
#  }
# # to access an endevgule one ,we need to use as the array way...
# print(cars["trucks"])

# def frouts(frotname,color,ss):

#     # dictionary: ["apple": "red", "banana": "yellow" , "orange": "orange" ]
#   ss[frotname]=color
#   return ss

# print(frouts(ss=[]))

# froutscolor ={
#     "apple":"red",
#     "orange":"orange",
#     "banan":"yello",
# }


# def floop():
#  for x in froutscolor.values():
#     print(x)

# print(floop())
    

# def randm():
#     froutscolor ={
#     "apple":"red",
#     "orange":"orange",
#     "banan":"yello",
# }
    

# def fvall():
#      print(froutscolor["apple","orange","banan"])
 

# print(fvall())


  
         ############################ classes , constructors .... #######
         



# class STUDENT:
#     stodentname="fahad"

# p1=STUDENT()
# print(p1.stodentname)

# init function

# class stdnt:
#     def__init__(self, name, age):
#      self.name=name
#      self.age=age

# p1 =stdnt("fahad",50)
# print(p1.name)
# @@@@@@@@@@@@@@@@@
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

class Student:
    def __init__(self, name, id, course, level):
        self.name=name
        self.id=id
        self.course=course
        self.level=level
    def regster(self,id="student with id is registered"):
       return id






stodent=Student("mohammed","3","333cs","6")



print(stodent.name+" "+stodent.id+" "+stodent.course+" "+stodent.level)
print(stodent.regster())




        



  


    

