def main():
    print("this is a shipping company selling tea")
    print("the prices are as follows")
    print("bosnia 1.5e per kg + 0 base")
    print("croatia 1.9e per kg + 5 base")
    print("serbia 2.5e per kg + 12 base")
    print("montenegro 2.7e per kg + 14 base")
    print("where do you want your tea shipped?")
    ship_to = int(input("1 is bosnia 2 is crotia 3 is serbia 4 is montenegro>>>>>"))
    kg = int(input("how many kg of tea do you want>>>>"))
    # Bosnia = ship_to == 1 == print(kg * 1.5 ,end= " euro")
    # croatia = ship_to == 2 == print(kg * 1.9 + 5, end=" euro")
    # serbia = ship_to == 3 == print(kg * 2.5 + 12,end=" euro")
    # montenegro = ship_to == 4 == print(kg * 2.7 + 14, end=" euro")

    countries = [[1.5, 0], [1.9,5], [2.5,12], [2.7,14]]
    cost = kg * countries[ship_to-1][0] + countries[ship_to-1][1]
    print(cost)

main()