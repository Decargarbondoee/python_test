
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

# Be careful when comparing strings
country = 'CANADA'
if country.lower() == 'Canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')