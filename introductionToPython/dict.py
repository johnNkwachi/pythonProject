capitals = {
    'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin',
         'Colorado': 'Denver'
}

print(capitals["California"])

print('New York' in capitals)
print(f"the capital of California is {capitals['California']}")

for keys in capitals:
    print(keys)

for state in capitals:
    print(f"The capital of {state} is {capitals[state]}")