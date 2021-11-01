from types import prepare_class


print("COMPUTER BAZAR")
print("1: Dell(Rs 200000)")
print("2: mac(Rs 500000)")
print("3: Toosiba(Rs 300000)")

opt=int(input("Choose your choice"))
qt=int(input("enter your quantity"))
dell_price= 200000
mac_price= 500000
Tosiba_price= 300000

if opt==1:
    print("your price is :",qt*dell_price)
elif opt==2:
    print("your price is :", qt*mac_price)
elif opt==3:
    print("your price is :", qt*Tosiba_price)
else:
    print("No option")

print("do you want to delivery your product")

delivery=int(input("For home enter 1, if pickup enter 2: "))

ho =1000
pc = 0 

if delivery==1:
    hh= ho
    print("1000 has been added")
elif delivery==2:
    pp= pc
    print("its free")
else:
    print("enter wrong number")

packing=int(input("for plastic type pls, for bag type bg, for gift type g, for none type n"))

pls= 500
bg=1000
g=5000
n=0

if packing==pls:
    pg= pls
    print("500 has been added")
elif packing==bg:
    ba=bg
    print("1000 has been added")
elif packing==g:
    gif=g
    print("5000 has been added")
elif packing==n:
    non=n
    print("its free")
else:
    print("enter wrong number")














