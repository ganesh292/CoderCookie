#My Shopping Cart

items=input("Enter your grocery list:")
my_item_list=[]
while(items!="done"):
    my_item_list.append(items)
    items=input()#keep entering items until I enter done

print("Your cart:")
for i in my_item_list:
    print(i)
