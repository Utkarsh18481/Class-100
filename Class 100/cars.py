class Cars():
    def __init__(self, model, colour, company, maxspeed):
        self.model = model
        self.colour = colour
        self.company = company
        self.maxspeed = maxspeed

    def start(self):
        print("Car is getting started")

    def stop(self):
        print("Car has stopped")

    def accelerate(self, value):
        if value < self.maxspeed:
            print("Car is speeding up")
        else: 
            print("Car is at Max Speed")

car1 = Cars("A6", "Red", "Audi", 200)

car1. start()
car1. accelerate(200)
car1. stop()
