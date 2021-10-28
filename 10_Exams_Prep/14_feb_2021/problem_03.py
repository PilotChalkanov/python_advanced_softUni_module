
def stock_availability(inventory:list, action:str, *args):

    if action == "delivery":
        inventory.extend(args)
    elif action == "sell":
        if args:
            for arg in args:
                if type(arg) is int:
                    inventory=inventory[arg-1:0]
                elif arg in inventory:
                    while inventory.count(arg)>0:
                        inventory.remove(arg)
        else:
            inventory=inventory[1:]
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))