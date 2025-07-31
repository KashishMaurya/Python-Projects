import random

names = ["Alice", "bob", "Charlie", "David", "Eve", "Frank"]

# way1
randIdx = random.randint(0, 5)
bill_payer = names[randIdx]
print(bill_payer)

# way2
print(random.choice(names))