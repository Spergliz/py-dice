import random
# loop
Loop = True
while Loop:
    # menu
    print("\nMenu")
    print("1. one roll")
    print("2. roll five times")
    print("3. roll X times")
    print("4. roll til Snake Eyes")
    print("5. Exit")
    menu = input("choose a number from menu: ")
    # 1 dice roll
    if menu == "1":
        print("\n")
        DR = random.randrange(1, 6)
        DR2 = random.randrange(1, 6)
        print(str(DR)+", " + str(DR2))
        print("sum: " + str(DR+DR2))
    elif menu == "2":
        for I in range(5):
            FR = random.randrange(1,6)
            FR2 = random.randrange(1,6)
            print( str(FR)+ ","+ str(FR2))
            pri
             


    # exit
    if menu == "5":
        Loop = False



