class PartyAnimal:
    x = 0
    name = " "
    def __init__(self, z):
        self.name = z 
        print(self.name, "construted")

    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party construted")

s = PartyAnimal("Huy")
s.party()

j = PartyAnimal("Duc")
j.party()
s.party()

numbers = [1, 2, 3, 1, 2, 4, 5]
first = set(numbers)
second = {6, 1, 63, 2}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

print(ord('D'))


