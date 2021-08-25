def calcBills():
    myBills = {'Electric': 120.00, 'Rent': 675.00, 'Car Insurance': 129.00, 'Phone': 90.00, 'Loan': 258, 'Internet': 84.00}
    total = 0
    for i in myBills:
        total += myBills[i]
    owed = 'The total owed for bills this month is: ${}'.format(total)
    return owed
