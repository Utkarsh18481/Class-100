class Games():
    def __init__(self, n, c, s):
        self.name = n
        self.category = c
        self.speciality = s

    def show(self):
        print(self.name)
        print(self.category)
        print(self.speciality)


game1 = Games("Fortinte", "Shooting", "Building") 
game2 = Games("Minecraft", "Creative", "Blocks")

game1.show()

game2.show()
