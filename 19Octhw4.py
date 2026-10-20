
class Umbrella:
    
    def __init__(self,c,s,p):
        self.color = c
        self.size = s
        self.price = p

umbrella1 = Umbrella("Black","Medium",250)
umbrella2 = Umbrella("Grey","Small",150)
umbrella3 = Umbrella("Sky Blue","Medium",220)
umbrella4 = Umbrella("Red","Large",450)
umbrella5 = Umbrella("Brown","Small",190)

Umbrella_list = []

Umbrella_list.append(umbrella1)
Umbrella_list.append(umbrella2)
Umbrella_list.append(umbrella3)
Umbrella_list.append(umbrella4)
Umbrella_list.append(umbrella5)

for umbrella in Umbrella_list:
    if umbrella.size == "Large":
        print(f"Umbrella color is : {umbrella.color}, Umbrella Size is : {umbrella.size}, Umbrella Price is : {umbrella.price}")