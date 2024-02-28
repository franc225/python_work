for value in range (1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = [value**2 for value in range(1,11)]
#for value in range(1,11):
#    squares.append(value**2) 

print(squares) 
print(min(squares))
print(max(squares))

for value in range(1,21):
    print(value)

millions = list(range(1,1000001))
print(sum(millions))

multiples = list(range(3,33,3))
for multiple in multiples:
    print(multiple)