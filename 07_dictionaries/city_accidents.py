cities = {}

for i in range(5):

    city_id = int(input("Enter the city ID: "))
    vehicles = int(input("Enter the number of vehicles in the city: "))
    accidents = int(input("Enter the number of accidents in the city: "))

    cities[city_id] = (vehicles, accidents)


most_accidents = max(cities.items(), key=lambda x: x[1][1])

fewest_accidents = min(cities.items(), key=lambda x: x[1][1])


average_vehicles = sum(
    vehicles for vehicles, _ in cities.values()
) / len(cities)


cities_under_2000 = [
    accidents
    for vehicles, accidents in cities.values()
    if vehicles < 2000
]


if cities_under_2000:
    average_accidents_under_2000 = (
        sum(cities_under_2000) / len(cities_under_2000)
    )
else:
    average_accidents_under_2000 = 0


print(
    f"\nCity with the most accidents: "
    f"ID {most_accidents[0]} with {most_accidents[1][1]} accidents"
)

print(
    f"City with the fewest accidents: "
    f"ID {fewest_accidents[0]} with {fewest_accidents[1][1]} accidents"
)

print(f"Average number of vehicles: {average_vehicles:.2f}")

print(
    f"Average number of accidents in cities "
    f"with fewer than 2,000 vehicles: "
    f"{average_accidents_under_2000:.2f}"
)
