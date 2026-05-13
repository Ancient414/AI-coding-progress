class Fighter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_hit(self, damage):
        self.health -= damage
        print(f'{self.name} took {damage} damage')
        if self.health <= 0:
            print(f'{self.name} lost')
    
    def punch(self, target):
        print(f'{self.name} punched {target.name}')
        target.take_hit(10)
    
    def nuclear_bomb(self, target):
        print(f'{self.name} droped a nuclear bomb on {target.name} killing everyone')
        target.take_hit(100)
    
    def status(self):
        print(f'{self.name}s HP = {self.health}')

fighter1 = Fighter('Ancient', 100)
fighter2 = Fighter('Thragg', 100)

fighter1.status()
fighter2.status()

fighter1.punch(fighter2)
fighter2.punch(fighter1)

fighter1.nuclear_bomb(fighter2)
