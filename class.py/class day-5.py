"""class Animal:
    def __init__(self,name,species):
        self.name=name
        self.speices=species

    def __init__(self,name,species,age):
        self.name = name
        self.species =species
        self.age=age
  
    def walk(self):
        print(f"{self.name}is walking")

if __name__=="__main__":
    cat=Animal(name="cat",species="cat family")
    cat.walk()"""

class Car:
 def __init__(self,tyre,door,engine):
  self.tyre=tyre
  self.door=door
  self.engine=engine
    
class Maruti(Car):
     def __init__ (self,tyre,door,engine,speed):
       self.speed=speed
       def travel(self):
         print(f"{self.name}:{self.speed}")
