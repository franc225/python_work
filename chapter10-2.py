from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

path = Path('numbers.json')
contens = json.dumps(numbers)
path.write_text(contens)

contens = path.read_text()
numbers = json.loads(contens)

print(numbers)