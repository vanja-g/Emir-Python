def main():
    print("konditorei coffee is 10.50 a pound")
    amountofcoffe = int(input("how many pounds of coffe do you want?:"))
    coffeevalue = 10.50 * amountofcoffe
    x= amountofcoffe * .86
    coffeeaftertax= x + coffeevalue


    print("your total after tax is", coffeeaftertax + 1.50)

main()