import time

class Car:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0
    
    def start(self):
        print("Starting your car...")
    
    def move(self):
        self.speed += 2
        print("\nCar is moving at speed of "+str(self.speed)+" kmph although it's max speed is "+str(self.top_speed))
        print("\n moving...")
        return self.speed
    
    def acclerate(self):
        self.speed += 2
        print("\n moving...")
        return self.speed
    
    def apply_brake(self):
        self.speed = 0

class Tesla(Car):
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0
        self.fuel_type = "electricity"
    
    def charge_car(self):
        print("You car is charging...")
        for charge in range(50, 100, 5):
            print(str(charge)+"'%' charged")
            time.sleep(1)

def driveTesla():
    print("Note: Press 'b' to hit the brake")
    top_speed = int(input("Enter the top spped in km/h: "))
    avg_speed = int(input("Enter your average speed: "))
    tsl = Tesla(top_speed)
    opt = input("\nWould you like to recharge your car? y/n: ")
    if opt =='Y' or opt == 'y':
        tsl.charge_car()

    tsl.start()

    while True:
        speed = tsl.move()
        time.sleep(3)

        choice = input("\n Do you want to accelerate? y/n: ")
        if choice == 'Y' or choice=='y':
            speed = tsl.acclerate()
            print("\n Accelerating at a speed of "+str(speed))
        
        if speed > avg_speed:
            print("\n ******Warning!! You're speeding up******")
        
        if speed > top_speed:
            print("You have exceeded the top speed. Press 'b' to hit the brake")
            inp = input()
            if inp == 'b':
                print("Applying brake. The car is stopping...")
                time.sleep(2)
                break
        else:
            continue


if __name__ == '__main__':
    driveTesla()
