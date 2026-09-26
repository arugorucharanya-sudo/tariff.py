def calculate_energy_charge(units):
    """
    Calculate energy charge using slab-wise tariff.

    Example tariff:
    0 - 100 units       : Rs. 3.00/unit
    101 - 200 units     : Rs. 4.50/unit
    201 - 500 units     : Rs. 6.00/unit
    Above 500 units     : Rs. 7.50/unit
    """

    charge = 0

    if units <= 100:
        charge = units * 3.00

    elif units <= 200:
        charge = (100 * 3.00) + ((units - 100) * 4.50)

    elif units <= 500:
        charge = (
            (100 * 3.00)
            + (100 * 4.50)
            + ((units - 200) * 6.00)
        )

    else:
        charge = (
            (100 * 3.00)
            + (100 * 4.50)
            + (300 * 6.00)
            + ((units - 500) * 7.50)
        )

    return charge

