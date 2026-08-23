###
##
## Stamp Coupling is reasonable when:
## - The function needs most of object's data.
## - Splitting the object into many parameters make the code harder to understand.
##
##


def validate(order):
    print(f"Validate the {order}")


def calculate_shipping(order):
    print(f"Calculate Shipping the {order}")


def charge_payment(order):
    print(f"Charge Payment the {order}")


def process_order(order):
    validate(order)
    calculate_shipping(order)
    charge_payment(order)
