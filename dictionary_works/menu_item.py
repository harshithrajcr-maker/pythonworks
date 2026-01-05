

menu_item = {
    "dosa set":40,
    "masala dosa":60,
    "idaly set":40,
    "meals":70,"fish curry":120,
    "biriyani":140
    }

# print(menu_item)

# for k in menu_item.keys():

#     print(k)

for k,v in menu_item.items():

    # print(k,v)

    if v<50:

        print(k,v)
 
item_price=menu_item.get("meals",0)

print(item_price)

# if "chikken curry" not in menu_item:

#     menu_item["chikken curry"] =120

#     print(menu_item)

if "meals" in menu_item:
    
    menu_item["meals"]+=15

    print(menu_item)