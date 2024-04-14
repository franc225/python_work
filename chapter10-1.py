from pathlib import Path

path = Path('pi-digits.txt')
try:
    contents = path.read_text()
    lines = contents.splitlines()
    pi_string = ''
    for line in lines:
        pi_string += line.lstrip()

    print(f"{pi_string[:52]}...")
    print(len(pi_string))
except:
    print("File not found") 

contents = 'I love programming.\n'
contents += 'I love playing games.\n'
contents += 'I also love working with data.\n'

path = Path('programming.txt')
path.write_text(contents)

contents = path.read_text()
lines = contents.splitlines()
programming = ''
for line in lines:
    programming += line.lstrip()

print(programming)
