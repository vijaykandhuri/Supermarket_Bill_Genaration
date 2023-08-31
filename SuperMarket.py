from datetime import datetime

name=str(input('''Enter your Name:'''))

# Items List
lists='''
rice    rs 50/kg
sugar   rs 30/kg
salt    rs 20/kg
oli     rs 160/liter
dhal    rs 100/kg
peanuts rs 120/kg
soap    rs 30/each
paste   rs 20/each
maggi   rs 30/each
tea     rs 35/each
coffe   rs 40/each
'''
#print(lists)
#Declaration
price=0
total_price=0
final_price=0
pricelist=[]
items_list=[]
quanty_list=[]
pr_list=[]

# rates for items
items={'rice':50,'sugar':30,'salt':20,'oil':160,'dhal':100,'peanuts':120,
       'soap':30, 'paste':20,'maggi':30, 'tea':35, 'coffe':40 }

option=int(input("\n        *Welcome to Vijay Mart* \npress *1* for shows the list of items: "))
if option==1:
    print(lists)
    
    for i in range(len(items)):
        inp1=int(input("for Buy press 1  or Exit press 2 : "))
        while True:
       
            if inp1==1:
                item=input("Enter your item Name:")
                qty=int(input("Enter quanty:"))
                if item in items.keys():
                    price=qty*(items[item])
                    pricelist.append((item,qty,items,price))
                    total_price+=price
                    items_list.append(item)
                    quanty_list.append(qty)
                    pr_list.append(price)
                    GST=(total_price*5)/100
                    finalamount=total_price+GST
                
                else:
                    print("Entered items list not avalilable")

                
                inp=input("can i bill the items press *yes* and *no* for continue or *exit*:")
                if inp=='yes':
                    pass
                    if finalamount!=0:
                        print(30*"=","Vijay Mart",30*"=")
                        print(25*" ","Nizampet,HYB-500090")
                        print("Name:",name,26*" ","Date:",datetime.now())
                        print(72*"=")
                        print("Sno",12*" ","items",14*" ","quanty",14*" ","price")
                        for i in range(len(pricelist)):
                            print(i,14*' ',items_list[i],17*' ',quanty_list[i],18*' ',pr_list[i])
                        print(72*"=")
                        print(48*" ",'TotalAmount:','Rs:',float(total_price))
                        print(50*" ",'GST amount','Rs:', GST)
                        print(72*"=")
                        print(48*" ",'Total amount','Rs:',float(finalamount))
                        print(72*"=")
                        print(25*" ",'Thanks for Visiting')
                        print(72*"=")
                        break
                        
                elif inp=='no':
                    continue
                
                elif inp=='exit':
                   break 
                else:
                    print("Please select an item and confirm yes or no or Exit only")
                
            else:
                inp1==2
                print("Thanks and Buy again")
                break
        break
    
else:
    print("Entered Wrong Number")
    
                