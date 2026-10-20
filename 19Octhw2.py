
class Bag:

    def __init__(self,c,b,p):
        self.color = c
        self.capacity = b
        self.price = p

bag1 = Bag("Black","1.5L",1200)
bag2 = Bag("Blue","2L",1400)
bag3 = Bag("Grey","2.5L",1500)
bag4 = Bag("Sky Blue","3L",3300)
bag5 = Bag("Brown","1.5L",3200)


Bag_list = []

Bag_list.append(bag1)
Bag_list.append(bag2)
Bag_list.append(bag3)
Bag_list.append(bag4)
Bag_list.append(bag5)

for bag in Bag_list:
    print(f"Bag Color :{bag.color},Bag Capacity :{bag.capacity},Bag Price :{bag.price}")

        