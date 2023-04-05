import random
response = input("Do you want to roll a dice? Type 'y' for yes and 'n' for no :")
def rollDice(response):
    while response == "y":
        no = random.randint(1,6)
        if(no == 1):
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print('[-----]')
        if(no == 2):
            print("[-----]")
            print("[  0  ]")
            print("[     ]")
            print("[  0  ]")
            print('[-----]')
        if(no == 3):
            print("[-----]")
            print("[  0  ]")
            print("[  0  ]")
            print("[  0  ]")
            print('[-----]')
        if(no == 4):
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print('[-----]')
        if(no == 5):
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print('[-----]')
        if(no == 6):
            print("[-----]")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print('[-----]')
rollDice(response)
