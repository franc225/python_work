banned_users = ['andrew','carolina','david']
user = 'marie'

if not user in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

age = 17
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

if age < 4:
    print ("No admissiuon fee")
elif age < 18:
    print("Your admission cost is 25$")
elif age >= 65:
    print("Your admission cost is 30$")
else:
    print("Your admission cost is 40$")