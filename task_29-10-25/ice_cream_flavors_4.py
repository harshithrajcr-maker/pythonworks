print("select a flavor\n1.chocolate\n2.vanila\n3.strawberry\n4.butterscotch")

op = int(input("enter the options number (1-4) ="))

match op:
    case 1:
        print("chocolate")

    case 2:
        print("vanila")

    case 3:
        print("strawberry")

    case 4:
        print("butterscotch")

    case _:
        print("invalid")
"""
 4. Ice Cream Flavors

"""