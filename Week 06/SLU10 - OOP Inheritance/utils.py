import random
    

def get_random_number(start: int, stop: int):
    return random.randint(start, stop)


class Spell:
    def __init__(self, charm, name):
        self.name = name
        self.charm = charm
        
    def detail(self):
        return "{name} | {charm} | {desc}".format(name=self.name, charm=self.charm, desc=self.get_description())
    
    def execute(self):
        print(self.charm) 
        
    def get_description(self):
        return "No description"
        