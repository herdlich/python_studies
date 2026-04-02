amount = int(input('Enter cost of goods: '))

if amount > 0:  # in this branch we define the range
    if amount > 25000:
        discount = amount * 0.3
    elif amount > 15000:
        discount = amount * 0.2
    elif amount > 5000:
        discount = amount * 0.12
    else:
        discount = amount * 0.05
else:
    print('Sorry, you have to pay $0.')

# The discount and final price are shown
print(f'Discount: {int(discount)}')
print(f'Amount including discount: {int(amount - discount)}')
