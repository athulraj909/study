from aa import add,display

while True:
    print("1: Add \n"
          "2: Display\n"
          "3: Exit\n")
    y = int(input("Enter your choice: "))
    if y == 3:
        break
    elif y == 1:
        add()
    elif y == 2:
        display()