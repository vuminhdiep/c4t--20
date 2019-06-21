district_name = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
population = [150300, 247100, 333300, 266800, 420900, 318000]
maximum = population.index(max(population))
minimum = population.index(min(population))
print(district_name[maximum], district_name[minimum])