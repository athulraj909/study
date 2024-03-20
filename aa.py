a = []
def add():
    b = []
    n = int(input("Enter how many pairs: "))
    for i in range(n):
        name = input("Enter your vehicle name: ")

        if name in b:  # Check if name already exists
            print(f"{name} already exists")
        else:
            price = int(input("Enter your vehicle price: "))
            wheel = int(input("How many wheels: "))
            b = [name, price, wheel]  # Create a new list for each vehicle
            a.append(b)
            print(b)
            print(a)

def display():
    def two():
        for vehicle in a:
            if vehicle[2] == 2:
                print(f"{vehicle[0]} is a two wheel vehicle.price is {vehicle[1]}")

    def three():
        for vehicle in a:
            if vehicle[2] == 3:
                print(f"{vehicle[0]} is a three wheel vehicle")

    def four():
        for vehicle in a:
            if vehicle[2] == 4:
                print(f"{vehicle[0]} is a four wheel vehicle")

    while True:
        print("1: Two-wheel \n"
              "2: Three-wheel\n"
              "3: Four-wheel\n"
              "4: Exit\n")
        y = int(input("Enter your choice: "))
        if y == 4:
            break
        elif y == 1:
            two()
        elif y == 2:
            three()
        elif y == 3:
            four()