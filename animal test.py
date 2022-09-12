import random


class Animal():
    health_value = 100.00
    def __init__(self,health_value=100.00):
        self.health_value=Animal.health_value
        Animal.health_value+=1.00
        
    def feed_animal(self):
        Animal.health_value = Animal.health_value + (self.health_value / 100)
        random_feed=random.randint(10, 25)
        Animal.health_value +=random_feed
        return Animal.health_value
    def iteration(self):
        Animal.health_value=Animal.health_value-(Animal.health_value/100)
        random_feed = random.randint(10, 20)
        Animal.health_value=Animal.health_value -random_feed
        return Animal.health_value
    def health_check(self):
             for Monkey in Animal.health_value:
              if Animal.health_value<30.00:
                 return "Pronounced dead Straight away"
              else:
                 return "Its Alright"
class Elephant(Animal):
   def __init__(self):
    super(Animal,self).__init__()
   def check_health(self):
          if Animal.health_value>70.00:
             return "It Alright"
          if Animal.heath_value<70.00:
             return "It can not Walk"
          elif Animal.health_value<70.00 and (self.time_passing>self.time_passing) :
              return " Its pronounced dead"
    

    
class Giraffe(Animal):
   def __init__(self):
     super(Animal,self).__init__()
   def check_health(self):
             if Animal.health_value < 50.00:
                 return "Pronounced dead Straight away"
             else:
                 return "Its Alright"

class Monkey(Animal):
  def __init__(self):
    super(Animal,self).__init__()
  def check_health(self):
            if Animal.health_value<30.00:
                return "Pronounced dead Straight away"
            else:
               return "Its Alright"
  def __repr__(self):
      return ""



A1=Animal()
A1=Animal()
A1=Animal()
A1=Animal()
A1=Animal()

E1=Elephant
E2=Elephant
E3=Elephant
E4=Elephant
E5=Elephant


G1=Giraffe
G2=Giraffe
G3=Giraffe
G4=Giraffe
G5=Giraffe

M1=Monkey()
M2=Monkey()
M3=Monkey()
M4=Monkey()
M5=Monkey()


M3=()
#print(A1.health_value)

#print(A1.feed_animal())
#print(A1.iteration())
#print(M2.iteration())
#print(M2)
print(M2.feed_animal())
print(M2.check_health())
print(E1.check_health(3))
print(G5.check_health(2))
#print(M3)
#print(A1)
print(hasattr(M2,"check_health"))
    