def joinOrders(orders):
    parsed = orders.split(',')
    aggregateBuy = float(0)
    aggregateSell = float(0)

    for order in parsed:
        parsedOrder = order.split(' ')
        if(parsedOrder[3] == 'B'):
            aggregateBuy += (float(parsedOrder[1]) * float(parsedOrder[2]))
        elif(parsedOrder[3] == 'S'):
            aggregateSell += (float(parsedOrder[1]) * float(parsedOrder[2]))

    aggregate = 'Buy: ' + str(format(aggregateBuy, '.2f')) + ' Sell: ' + str(format(aggregateSell, '.2f'))
    return aggregate

rawOrders = 'ZNG 1300 2.66 B,CH15.NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B'
joinedOrders = joinOrders(rawOrders)
print(joinedOrders)