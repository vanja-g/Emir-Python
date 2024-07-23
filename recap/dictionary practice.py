#send packets through bosnia and they send from sarajevo they send to 5 cities
#sarajevo,tulza,zenicu,mostar,banja luku. tuzla shipping 5km,sarajevo 2km,
# zenica 3km, mostar 5km , banja luka 7km. fees r 1km. for weight of package over 2kg per kilo
# add 30 percent shipping cost to that location. program that will calculate shipping to locations
from math import trunc


def main():
    cities = {"sarajevo":2,"tuzla": 5, "mostar" : 5,"banja luka":7,"zenica": 3}
    location = str(input("Enter city name: ")).lower()
    weight = trunc(float(input("Enter weight: ")))
    delivery_cost = cities[location] + 1
    over_2kg_weight = (cities[location] * 0.3) * (weight - 2)
    if weight > 2:
        delivery_cost = delivery_cost + over_2kg_weight

    print("cost of delivery is: ", delivery_cost)
    print("delivery fee for",location,cities[location])
    print("delivery fee 1km")
    print("over weight fee is",over_2kg_weight)





main()