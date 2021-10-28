from collections import deque
craft_materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

toy_specss = {
            150 : "Doll",
            250 : "Wooden train",
            300 : "Teddy bear",
            400 : "Bicycle"
}
crafted_toys = {
                "Doll":0,
                "Wooden train":0,
                "Teddy bear":0,
                "Bicycle":0}

while magics and craft_materials:

    current_craft = craft_materials[-1]
    current_magic = magics[0]
    craftung = current_craft*current_magic

    if craftung in toy_specss.keys():
        crafted_toys[toy_specss[craftung]] += 1
        magics.popleft()
        craft_materials.pop()

    elif current_magic < 0 or current_craft < 0:
        craft_materials.pop()
        magics.popleft()
        material = current_magic + current_craft
        craft_materials.append(material)
    elif current_magic == 0:
        magics.popleft()
    elif current_craft == 0:
        craft_materials.pop()
    elif current_magic == 0 and current_craft ==0:
        magics.popleft()
        craft_materials.pop()
    elif craftung not in toy_specss.keys():
        magics.popleft()
        craft_materials[-1] += 15

if crafted_toys["Doll"] >= 1 and crafted_toys["Wooden train"]:
    print("The presents are crafted! Merry Christmas!")
elif crafted_toys["Teddy bear"] >=1 and crafted_toys["Bicycle"] >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if craft_materials:
    craft_materials.reverse()
    print(f"Materials left: {', '.join(str(x) for x in craft_materials)}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")


for k,v in sorted(crafted_toys.items(),key=lambda x:x[0],):
    if v > 0:
        print(f"{k}: {v}")


