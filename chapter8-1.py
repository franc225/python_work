from pizzeria import make_pizza as mp

def greet_user(username='toto'):
    print(f"Hello, {username}!")

greet_user(username='jesse')
greet_user()

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age=27)
print(musician)

mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')