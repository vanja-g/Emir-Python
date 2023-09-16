def main():
    your_number= int(input("pick a number than can be times by 2>>>>"))
    power_of_2= int(input("how many times will ur number be times by 2>>>>"))
    result=your_number
    for i in range(power_of_2):
        result = result *2
    print(result)

main()