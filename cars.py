cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)

#cars.sort(reverse=True)
#print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

for car in cars:
    if car == "bmw" or car == "audi":
        print(car.upper())
    else:
        if car == "toyota" and car.upper() == "SUBARU":
            print(car.title())