class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"Type {self.__class__.__name__}, Health: {self.health}, Attack:{self.attack}"  
    
    def __add__(self, other):
        if isinstance (other, (int, float)):
            self.health += other
            self.attack += other
        return self

    def __mul__(self, other):
        if isinstance (other, (int, float)):
            self.health *= other
        return self
class Elf (Warrior):
    def __init__(self, health=50, attack=5,agility=4):
        super().__init__(health, attack) 
        self.agility = agility 

    def __str__(self):
        return f"{super().__str__()}, Agility: {self.agility}"
class Orc (Warrior):
    def __init__(self, health=50, attack=5, fury=6):
        super().__init__(health, attack)
        self.fury=fury
    def __str__(self):
        return f"{super().__str__()},Fury:{self.fury}"  

def fight (unit_1, unit_2):
    print ("----------Битва начинается----------")

    while unit_1.is_alive and unit_2.is_alive:
        # Первый боец бьет второго
        unit_2.health -= unit_1.attack
        print(f"{unit_1.__class__.__name__} бьет {unit_2.__class__.__name__}! У жертвы осталось {unit_2.health} HP.")
        
        # Если второй боец погиб от удара — сразу выходим из цикла
        if not unit_2.is_alive:
            break
            
        #Второй боец бьет первого (ответный удар)
        unit_1.health -= unit_2.attack
        print(f"{unit_2.__class__.__name__} бьет {unit_1.__class__.__name__}! У жертвы осталось {unit_1.health} HP.")
        print("-" * 25)  # Разделитель раундов

     # Этот код пишется ВНЕ цикла while, когда кто-то уже погиб
    if unit_1.is_alive:
        print(f" ПОБЕДИТЕЛЬ: {unit_1.__class__.__name__}!")
    else:
        print(f"
               ПОБЕДИТЕЛЬ: {unit_2.__class__.__name__}!")
       

                                                                                   
                                                                                
                                                                                
warrior_1 = Warrior()
print (warrior_1)
warrior_1+10
print (warrior_1)
warrior_1*2
print (warrior_1)  
elf_1=Elf(health=60, attack=8, agility=5)  
print (elf_1)
orc_1=Orc(health=80, attack=12, fury = 10)
print (orc_1)
elf_1 = Elf(health=60, attack=8, agility=5)
orc_1 = Orc(health=80, attack=12, fury=10)
fight(elf_1, orc_1)  
