district_name = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
population = [150300, 247100, 333300, 266800, 420900, 318000]
area = [11743, 9.244, 43.35, 12.04, 9.96, 10.09]
density = [x / y for x, y in zip(population, area)]
average = sum(density)/len(district_name)
print(average)