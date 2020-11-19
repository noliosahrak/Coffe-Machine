def machine_state():
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(available_cups, "of disposable cups")
    print(money, "of money")


def check_resources(number):
    global water, milk, beans, available_cups, money
    if number == 1:
        if water < 250:
            print("Sorry, not enough water")
        elif beans < 16:
            print("Sorry, not enough beans")
        elif available_cups < 1:
            print("Sorry, not enough cups")
        else:
            water -= 250
            beans -= 16
            money += 4
            available_cups -= 1
            print("I have enough resources, making you a coffee!")
    elif number == 2:
        if water < 350:
            print("Sorry, not enough water")
        elif milk < 75:
            print("Sorry, not enough milk")
        elif beans < 20:
            print("Sorry, not enough beans")
        elif available_cups < 1:
            print("Sorry, not enough cups")
        else:
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            available_cups -= 1
            print("I have enough resources, making you a coffee!")
    elif number == 3:
        if water < 200:
            print("Sorry, not enough water")
        elif milk < 100:
            print("Sorry, not enough milk")
        elif beans < 12:
            print("Sorry, not enough beans")
        elif available_cups < 1:
            print("Sorry, not enough cups")
        else:
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            available_cups -= 1
            print("I have enough resources, making you a coffee!")
    print()


water = 400
milk = 540
beans = 120
available_cups = 9
money = 550
while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        caffe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if caffe == "back":
            print()
            continue
        else:
            caffe = int(caffe)
            check_resources(caffe)
        print()
    elif action == "fill":
        water += int(input("Write how many ml of water do you want to add: "))
        milk += int(input("Write how many ml of milk do you want to add: "))
        beans += int(input("Write how many grams of coffee beans do you want to add: "))
        available_cups += int(input("Write how many disposable cups of coffee do you want to add: "))
        print()
    elif action == "take":
        print("I gave you ${}".format(money))
        print()
        money = 0
    elif action == "remaining":
        print()
        machine_state()
        print()
    elif action == "exit":
        break
