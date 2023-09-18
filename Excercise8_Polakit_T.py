User = input("Username : ")
Pass = input("Password: ")

if User == 'admin' and Pass == 'admin':
    print("--------------------Gaming Tech-----------------------")
    print("------------------------List--------------------------")
    print("--------------------1.Notebook------------------------")
    print("--------------------2.Gaming Pc-----------------------")
    print("---------------------3.Macbook------------------------")
    Product = int(input("Choose Product : "))
    if Product == 1:
        print("1.Notebook")
        Unit = int(input("How much : "))
        Price = 25000
        Total = Unit * Price
        print("Total :",Total,"Baht")
    elif Product == 2:
        print("2.Gaming Pc")
        Unit = int(input("How much : "))
        Price = 30000
        Total = Unit * Price
        print("Total :",Total,"Baht")
    elif Product == 3:
        print("3.Macbook")
        Unit = int(input("How much : "))
        Price = 50000
        Total = Unit * Price
        print("Total :",Total,"Baht")

print("------------Thank you------------")
