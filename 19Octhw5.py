
class Light:

    def __init__(self,b,t,p):
        self.brand = b
        self.type = t
        self.price = p

light1 = Light("Philips","LED",140)
light2 = Light("Syska","Smart RGB",420)
light3 = Light("Havells","CFL",290)
light4 = Light("Wipro","Filament",90)
light5 = Light("Crompton","LED",120)

Light_list = []

Light_list.append(light1)
Light_list.append(light2)
Light_list.append(light3)
Light_list.append(light4)
Light_list.append(light5)

for light in Light_list:
    if light.price > 200:
        print(f"Light brand : {light.brand}, Light Type is: {light.type}, Light Price is : {light.price}")