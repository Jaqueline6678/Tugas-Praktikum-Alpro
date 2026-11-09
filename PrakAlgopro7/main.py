from interest import compound_interest, simple_interest
from display import print_result

principal = 6000000
rate = 0.06
years = 10

ci = compound_interest(principal, rate, years)
si = simple_interest(principal, rate, years)

print_result(principal, rate, years, ci, si)