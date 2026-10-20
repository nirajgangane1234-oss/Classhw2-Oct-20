class Laptop:
 
    def __init__(self,c,r,b):
        self.color = c
        self.RAM = r
        self.brand = b

Laptop1 = Laptop("Black",64,"Lenovo")
Laptop2 = Laptop("White",24,"Asus")
Laptop3 = Laptop("Blue",128,"DELL")
Laptop4 = Laptop("Navy Blue",64,"Apple")
Laptop5 = Laptop("Grey",128,"Acer")



Laptop_list = []
Laptop_list.append(Laptop1)
Laptop_list.append(Laptop2)
Laptop_list.append(Laptop3)
Laptop_list.append(Laptop4)
Laptop_list.append(Laptop5)
Laptop_list.append(Laptop1)

for laptop in Laptop_list:
    if laptop.RAM > 64:
        print(f" Laptop color : {laptop.color} , Laptop RAM : {laptop.RAM}, Laptop Brand: {laptop.brand}")
        
