

state_data = [
    ('NC', 'Raleigh', 'Charlotte'),
    ('TX', 'Austin', 'Houston'),
    ('CA', 'Sacramento', 'Los Angeles'),
    ('OH', 'Columbus', 'Columbus'),
    ('NY', 'Albany', 'New York'),
    ('MI', 'Lansing', 'Detroit'),
]

for state in state_data:
    print(state, state[0], state[1], type(state))
print()

for abbreviation, state_name, largest_city in state_data:
    print(f"{abbreviation}/{state_name} ({largest_city})")




