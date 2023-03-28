# Southern California's electric company uses a "three tier" cost structure for household electric bills. As of Jan 2017, for a given month, the first 232 kWh is $0.08291/kWh, the next 696 kWh is $0.16838/kWh, and any additional kWh is $0.23336/kWh. Write a function that takes a household month's kWh, and the cutoffs and prices for the tiers, and returns that month's electric cost.
#
# If the input is:
#
# 1700.0  232  0.08291 696  0.16838  0.23336
# the output is:
#
# $316.58

def calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost):
    remaining_kwh = month_kwh
    month_cost = 0.0
    tier_kwh = 0.0

    if remaining_kwh > (tier2_cutoff + tier1_cutoff):
        # Calculate the tier 3 amount
        tier_kwh = remaining_kwh - (tier2_cutoff + tier1_cutoff)
        month_cost += tier_kwh * tier3_cost  # The difference is the 3333 part above
        remaining_kwh -= tier_kwh  # This gets rid of the 3333 part, leaving the 11111222222222 part

    if remaining_kwh > tier1_cutoff:
        # Calculate the tier 2 amount
        tier_kwh = remaining_kwh - tier1_cutoff
        month_cost += tier_kwh * tier2_cost  # The difference is the 2222222222 part
        remaining_kwh -= tier_kwh  # This gets rid of the 2222222222 part

    month_cost += remaining_kwh * tier1_cost  # The difference is the 11111 part above
    return month_cost


# Driver code
month_kwh = float(input())
tier1_cutoff, tier2_cutoff = map(float, input().split())
tier1_cost, tier2_cost, tier3_cost = map(float, input().split())

month_cost = calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost)
print(f"${month_cost:.2f}")
