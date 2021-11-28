def find_max(d):
    prices = []
    for dd in d:
        prices.append(dd[1])

    ma = max(prices)
    return prices.index(ma)