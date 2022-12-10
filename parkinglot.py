# noOfCars=0
# noOfBikes=0
# totalPayment=0
# noOfCars=int(input("No of Cars"))
# noOfBikes=int(input("No of Bikes"))
# totalPayment=noOfBikes*20+noOfCars*40
# print("total payment would be",totalPayment)

# print()
# noOfCars="Sanjoy"

product1=0
product2=0
product3=0
totalPayment=0
#using input function
product1=int(input("quantity of product1"))
product2=int(input("quantity of product2"))
product3=int(input("quantity of product3"))
# product4=int(input("quantity of product4"))
# product5=int(input("quantity of product5"))
#using list
# l=[product1,product2,product3]
#using for loop
# for i in l:
#     print(i)
#using if else statement
if((product1<=0) or (product2<=0) or (product3<=0)):
    print('please enter a positive number')
else:
    print('product quantity with price:')
    totalPayment=product1*40+product2*50+product3*60
    entries ={product1:40,product2:50,product3:60}
    for i,p in entries.items():
        print(i,p)
    print("the user needs to pay",totalPayment)
    print(totalPayment)







