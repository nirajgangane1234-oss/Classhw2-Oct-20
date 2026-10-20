
class Table:
    
    def __init__(self,s,t,c):
        self.shape = s
        self.seat = t
        self.color = c

table1 = Table("Square",5,"Brown")
table2 = Table("Circular",6,"Black")
table3 = Table("Rectangular",5,"Grey")
table4 = Table("Sqare",4,"White")
table5 = Table("Square",5,"Blue")

Table_list = []

Table_list.append(table1)
Table_list.append(table2)
Table_list.append(table3)
Table_list.append(table4)
Table_list.append(table5)

for table in Table_list:
    if table.seat == 5:
        print(f"Table shape is : {table.shape}, Table Seats is : {table.seat}, Table Color is : {table.color} ")