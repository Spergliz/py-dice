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
    # 1 roll
    if menu == "1":
        print("\n")
        DR = random.randrange(1, 6)
        DR2 = random.randrange(1, 6)
        print(str(DR)+", " + str(DR2))
        print("sum: " + str(DR+DR2))

    #5 roll
    elif menu == "2":
        for I in range(5):
            FR = random.randrange(1,6)
            FR2 = random.randrange(1,6)
            print("")
            print( str(FR)+ ","+ str(FR2))
            print("sum: "+ str(FR+FR2))
    
      #not working
      # X roll
    elif menu == "3":
        num = int(input("choose a number: "))
        for I in range(num):
            XR = random.randrange(1,6)
            XR2 = random.randrange(1,6)
            print("")
            print( str(XR)+ ","+ str(XR2))
            print("sum: "+ str(XR+XR2))
    # SE roll
    elif menu == "4":
        loop = True
        while loop:
            SER = random.randrange(1,6)
            SER2 = random.randrange(1,6)
            print("")
            print( str(SER)+ ","+ str(SER2))
            print("sum: "+ str(SER+SER2))
            if SER+SER2 == 2:
                print ("Snake Eyes")
                loop=False
    # setup before eveything else above, 
    # exit
    if menu == "5":
        Loop = False



