def calculate_discount(customer):
    if customer["country"] == "US":
        return 10
    return 0


############Better Solution##############


def calculate_discount_in_better_design(country):
    if country == "US":
        return 10
    return 0
