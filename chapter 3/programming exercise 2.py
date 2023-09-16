def main():
    import math
    pizza_price = int(input("how much does your pizza cost?:"))
    pizza_size = int(input("whats the diameter of your pizza?:"))
    pizza_radius = pizza_size / 2
    pizza_area = math.pi * (pizza_radius**2)
    pizza_per_square_centimeter = pizza_price / pizza_area


    print("your pizzas price per square centimeter is",pizza_per_square_centimeter )
main()
