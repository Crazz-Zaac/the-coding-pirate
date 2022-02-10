import time

class Car:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0
        self.const_speed = 10
    
    def start(self):
        print("Starting your car...")

    def move(self):
        self.speed += 2
        print("\nCar is moving at a speed of "+str(self.speed)+"kmph although it's max speed is: "+str(self.top_speed))
        print("\n moving...")
        return self.const_speed

    def accelerate(self):
        self.speed += 2
        print(("\n moving..."))
        return self.speed

    def apply_brake(self):
        self.speed = 0
    

def callCar():
    print("Note: Press 'b' to hit brake")
    top_speed = int(input("\nEnter top speed in km/h: "))
    bmw = Car(top_speed)      
    bmw.start()
    
    while True:
        const_speed = bmw.move()
        time.sleep(3)
        
        # option to accelerate
        choice = input("\nDo you want to accelerate? Y/N: ")
        if choice == "Y" or choice=="y":
            speed = bmw.accelerate()
            print("\nAccelerating at a speed of "+str(speed))
        
        # giving a warning if the speed exceeds constant speed
        if speed > const_speed:
            print("\n*****Warning! You're speeding up*****")
        
        # applying brake if the speed tries to exceed top speed 
        if speed > top_speed:
            print("You have exceeded the top speed. Press 'b' to hit brake")
            inp = input()
            if inp == "b":
                print("Applying brake. Car is stopping...")
                time.sleep(2)
                break
        else:
            continue

callCar()

