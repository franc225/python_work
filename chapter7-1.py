message = input("Tell me something and I will repeat it back to you ! :")
print(message)

age = input("Tell me a numeric value and I will be able to print it if you are an adult ! :")
age = int(age)

if (age >= 18):
    print(age)
else:
    print("Not allowed")

prompt = "Please enter quit to terminate the program :"
message = input(prompt)
while message != 'quit':
    message = input(prompt)
    print(message)