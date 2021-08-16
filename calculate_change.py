from decimal import Decimal

def calculate_change(list_coins, prod_value: float, received: float) -> list:
    if prod_value > received:
        return []
    result = []
    change = received - prod_value
    for coins in list_coins:
        change = round(change, 2) if change < 1 else change
        calc = int(Decimal(f'{change}') // Decimal(f'{coins}'))
        result.append(calc)
        change -= calc * coins
    return result
