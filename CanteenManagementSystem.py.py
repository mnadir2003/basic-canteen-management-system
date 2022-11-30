# -----------------CANTEEN MANAGEMENT SYSTEM--------------------
name = []
quantity = []
price = []
item_code = []


def refresh(name, quantity, price, item_code):
    import pickle
    try:
        f = open("menu.dat", "rb")
        temp = [""]
        while temp:
            temp = pickle.load(f)
            name.append(temp[0])
            quantity.append(temp[1])
            price.append(temp[2])
            item_code.append(int(temp[3]))
        f.close()
    except EOFError:
        pass
    except FileNotFoundError:
        pass


def view_menu():
    import pickle
    try:
        f = open("menu.dat", "rb")
        count = 1
        l = [""]
        print("S.No.", end="    ")
        print("Item Name", end="")
        for i in range(0, 15 - len("Item Name")):
            print(" ", end="")
        print(" Quantity ", end="     ")
        print("Unit Price", end="     ")
        print("Item Code")
        while l:
            l = pickle.load(f)
            print(count, end="          ")
            print(l[0], end="    ")
            for i in range(0, 22 - len(l[0])):
                print(end=" ")
            print(l[1], end="     ")
            for i in range(0, 14 - len(str(l[1]))):
                print(end=" ")
            print(l[2], end="")
            for i in range(0, 15 - len(str(l[2]))):
                print(end=" ")
            print(l[3])

            count += 1
        if count == 1:
            print("Menu is empty")

    except EOFError:
        print("************************")
    except FileNotFoundError:
        print("NO Menu Exist")


def add_item():
    import pickle
    ch = input("Do you want to use previous data (yes/no) ")
    while True:
        if "Y" in ch.upper():
            try:
                f = open("menu.dat", "ab")
                break
            except FileNotFoundError:
                print("No Previous Data Exists")
        elif "N" in ch.upper() :
            f = open("menu.dat", "wb")
            break
        else:
            print("Invalid input \n Try Again")

    n = input("Enter name: ")
    while True:
        try:
            qty = int(input('Enter Quantity : '))
            break
        except ValueError:
            print('Quantity should only be in digits \n TRY AGAIN')
    while True:
        try:
            p = int(input(' Enter price : '))
            break
        except ValueError:
            print('Quantity should only be in digits \n TRY AGAIN')
    while True:
        try:
            icd = int(input(' Enter item code : '))
            break
        except ValueError:
            print('Quantity should only be in digits \n TRY AGAIN')

    pickle.dump([n, qty, p, icd], f)
    f.close()
    print()
    print("Record Updated")
    print()
    refresh(name, quantity, price, item_code)


#def edit






def sell():
    import pickle
    global name
    global quantity
    global price
    global item_code
    refresh(name, quantity, price, item_code)
    ft = open("temp.dat", "wb")
    while True:
        try:
            f = open("menu.dat", "rb")
        except FileNotFoundError:
            print("First add item for sale")
            break
       
        print("Menu \n")
        view_menu()
        refresh(name, quantity, price, item_code)
        c = int(input("Enter Item Code of item to sell"))
        i = item_code.index(c)
        qty = int(input("Enter Quanntity: "))
        pickle.dump([name[i], qty, price[i]], ft)
        f.close()
        try:
                 f = open("menu.dat", "rb+")
                 m=[""]
                 while m:
                      pos=f.tell()
                      m=pickle.load(f)
                      if m[3]==c:
                          j=m
                          j[1]-=qty
                          f.seek(pos,0)
                          pickle.dump(j,f)

        except EOFError:
                 pass
                 
        print("Do you want to continue ")
        ch = input("Press enter to continue \n 'NO' to End ")
    
        if "N" in ch.upper():
            ft.close()
            ft = open("temp.dat", "rb")
            print("\n \n")
            print("Canteen Bill")
            print("S.No.  Item Name     Quantity   Unit Price    Sub Total", )
            l = [""]
            count = 1
            total = 0
            try:
                while l:
                    l=pickle.load(ft)
                    print(count, "      ", l[0], "               ", l[1], "             ", l[2], "             ", l[1] * l[2])
                    total += l[1] * l[2]
                    count += 1
                    
            except EOFError:
                pass
            except FileNotFoundError:
                pass
            print("\nTotal = ", total)
            print()
            print("THANKS FOR SHOPPING WITH US")
            print("**********************************")
            print()
            f.close()
            ft.close()
            break


while True:
    enter = input('Press enter to continue.')
    print('------------------Welcome to the Canteen------------------')
    print('1.View Menu \n2. Add items for sale \n3.Sell  \n4.Reset \n5.Exit')
    choice = int(input('Enter the number of your choice : '))

    if choice == 1:
        view_menu()
    elif choice == 2:
        add_item()
    elif choice == 3:
        sell()
    elif choice==4:
        import os
        if os.path.isfile("menu.dat"):
             os.remove("menu.dat")
        if os.path.isfile("temp.dat"):
             os.remove("temp.dat")
        print("RESET COMPLETED........")
    elif choice == 5:
         print("Exiting.......")
         break
    else:
        print("Invalid Input")
 
