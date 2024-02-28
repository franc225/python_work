players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here is the firtst three players of the team : ")
for player in players[:3]:
    print(player)

print("Here is the middle three players of the team : ")
for player in players[1:4]:
    print(player)

print("Here is the last three players of the team : ")
for player in players[-3:]:
    print(player)

my_foods = ['pizza','falafel','carrot cake']
friends_food = my_foods[:]

my_foods.append('cannoli')
friends_food.append('icecream')

print("My favorite foods are : ")
print(my_foods)

print("\nMy friend's favorites foods are : ")
print(friends_food)