import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def fuel_recursion(fuel):
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_recursion(calculate_fuel(fuel))



if __name__ == '__main__':
    input_file = "input_files/1.txt"
    with open(input_file, "r") as in_file:
        lines = in_file.readlines()
        sum = 0
        for line in lines:
            mass = int(line)
            print(mass)
            fuel = calculate_fuel(mass)
            recursive_fuel = fuel_recursion(fuel)
            sum += recursive_fuel
        print("The fuel for all of the parts is: " + str(sum))


