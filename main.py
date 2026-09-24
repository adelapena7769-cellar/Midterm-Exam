print('========================================')
print('    SALES RECORD MANAGEMENT SYSTEM')
print('========================================')
print('1. Add Sale Record')
print('2. View All Records & Summary Statistics')
print('3. Clear All Sales Dat')
print('4. Exit System')
print('========================================')
option = input('Select an option (1-4): ')

iName = 0
qSold = 0
ppUnit = 0

try:
    if option == '1':
        iName = input('Item Name: ')
        qSold = int(input('Quantity Sold: '))
        ppUnit = float(input('Price Per Unit: '))
    totalAmount = qSold * ppUnit
    print(f'Item Name: {iName}'
          f'\nQuantity Sold: {qSold}'
          f'\nPrice Per Unit: {ppUnit}'
          f'\nTotal Amount: {totalAmount}')
    if option == '4':
        print('Thank you for using the Sales Record Management System.')

except:
    print('Please enter either 1, 2, 3, or 4!')


