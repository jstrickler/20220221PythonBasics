bob_countries = ['Turkey', 'Burkina Faso', 'Chile',
                 'Germany', 'Turkey', 'Portugal',
                 'Japan', 'Laos', 'Turkey']

ellen_countries = ['Ivory Coast', 'Chile', 'Portugal',
                   'China', 'Chile', 'Chile', 'Laos',
                   'Canada']

bob = set(bob_countries)
ellen = set(ellen_countries)
bob.add('Chile')
bob.add('Turkey')
bob.add('Japan')
ellen.add('China')
ellen.add('Mozambique')

print("bob: {}".format(bob))
print("ellen: {}".format(ellen))

print("Common:", bob & ellen)  # intersection
print("Not common:", bob ^ ellen)  # Xor
print("ALL:", bob | ellen)  # union
print("Just Ellen:", ellen - bob)
print("Just Bob:", bob - ellen)

print(len(bob), len(ellen))





