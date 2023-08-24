province = input("what province do you live in?")
tax = 0

#if province == 'Alberta':
    #tax = 0.05
#elif province == 'Nunavut':
    #tax = 0.10
#if province == 'Nunavut':
    #tax = 0.10
#elif province == 'Ontario':
    #tax = 0.08
#if province == 'Ontario':
    #tax = 0.08
#else:
    #tax = ('Not available')
    #tax = 0.15
#if province == 'Not available':
    #tax = 0.15
#print(tax)

# Expressing it using OR:
if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05 
elif province == 'Ontario':
    tax = 0.08
else:
    tax = 0.15
print(tax)

# Expression using IN
if province in('Alberta','Nunavut','Yukon'):
    tax = 0.05 
elif province == 'Ontario':
    tax = 0.08
else:
    tax = 0.15
print(tax)

