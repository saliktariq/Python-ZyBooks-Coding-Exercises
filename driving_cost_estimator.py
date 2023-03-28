# Driving is expensive. Write a function CostForMilesGas that takes miles driven and returns the cents, assuming 30 miles per gallon and a per gallon price of $4. Write a similar function CostForMilesMaintenance that assumes tires last 20,000 miles and cost $500, and that assumes $300 of service every 10,000 miles. Finally, write a function CostForMiles that takes miles driven, and calls those two functions, returning total cents. Use constants in the functions as appropriate, like MILES_PER_GAL, not hardcoded values in the function's statements. Use only integer arithmetic throughout. If the input is 50, the output should be: 941 cents


def CostForMilesGas(milesDriven):
    MILES_PER_GAL = 30
    CENTS_PER_GAL = 400

    centsGas = (milesDriven * CENTS_PER_GAL) // MILES_PER_GAL
    # Note: Important to do the division last, because integer division ignores fraction.

    return centsGas


def CostForMilesMaintenance(milesDriven):
    # $500 every 20,000 miles for tires
    # $300 every 10,000 miles for service
    TIRES_CENTS = 50000
    TIRES_MILES = 20000
    SERVICE_CENTS = 30000
    SERVICE_MILES = 10000

    centsMaintenance = ((milesDriven * TIRES_CENTS) // TIRES_MILES) + ((milesDriven * SERVICE_CENTS) // SERVICE_MILES)
    # Note: Important to do the division last, because integer division ignores fraction.

    return centsMaintenance


def CostForMiles(milesDriven):
    return CostForMilesGas(milesDriven) + CostForMilesMaintenance(milesDriven)


# Get input from user
milesDriven = int(input())

# Output result
print(CostForMiles(milesDriven), "cents")
