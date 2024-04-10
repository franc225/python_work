user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for value in sorted(set(user_0.values())):
    print(value.title())

users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie' : {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

for username, userinfo in users.items():
    print(f"\nUsername : {username}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']

    print(f"\tFull name : {fullname.title()}")
    print(f"\tLocation : {location.title()}")