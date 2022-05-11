#----AlluKoodaa----#

## Fibonacci Bunnies

def bunnies(months):
    if months == 0:
        return 1
    couples = 0
    too_young = 1
    total = 0
    print("Adult bunny couples in the population:")
    for i in range(months + 1):
        total = couples + too_young
        print(f"Month #{i+1}: {total} couples")
        too_young = couples
        couples = total
    return total, too_young

def main():
    print("""This program calculates growth of a bunny population
during given time period.""")
    months = int(input("Input number of months: "))
    couples, young = bunnies(months)
    print(f"Bunny population after {months} months: {couples*2 + young*2} bunnies")

main()

#----eof----#
