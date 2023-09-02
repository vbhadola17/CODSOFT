num1=float(input("enter 1st number here:"))
num2=float(input("enter 2nd number here:"))
print("enter 1 for addition\nenter 2 for subtraction\nenter 3 for multiplication \nenter 4 for division")
choice=int(input("enter your choice from 1 to 4:"))
if choice == 1:
    sum=num1+num2                #addition of 2 numbers takes place
    print(sum)
elif choice ==2:
    difference=num1-num2         #difference of 2 numbers take place
    print(difference)
elif choice ==3:
    product=num1*num2            #multiplication of 2 numbers take place
    print(product)
elif choice==4:
    divide=num1/num2             #dividion of 2 numbers take place
    print(divide)
else:
    print("invalid input ")          