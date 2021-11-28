def find_min(d):
    prices = []
    for dd in d:
        prices.append(dd[1])

    mi = min(prices)
    return prices.index(mi)