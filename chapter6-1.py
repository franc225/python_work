alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(f"The color is now {alien_0['color']}.")
del alien_0['points']
print(alien_0)

point_value = alien_0.get('points','No point value assigned.')
print(point_value)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)

print("...")