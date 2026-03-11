"""
Below each country varaible will hold their current run quotient prior to the Italy v Mexico matchup
"""

class Country:
    def __init__(self, country:str, ra:int, o:int) -> None:
        self.country = country
        self.ra      = ra
        self.o       = o

    @property
    def rq(self) -> float:
        return self.ra / self.o


USA = Country("USA", 11, (27 + 27))
Mexico = Country("Mexico", 5, 24)
Italy = Country("Italy", 6, 27)
countries = [USA, Mexico, Italy]


italy_score  = int(input("How many runns did Italy score?: "))
Mexico.ra   += italy_score
mexico_score = int(input("How many runns did Mexico score?: "))
Italy.ra    +=  mexico_score

if italy_score > mexico_score:
    print("\nUSA WILL ADVANCE")
    print("\n1. Italy 4-0 \n2. USA 3-1 \n3. Mexico 2-2")
    print("\nRun quoefficient irrelevant in this scenario\n")

innings = int(input("How many inniings did the game last?: "))

"""
Multiply innings by three as each team records three outs per inning
-1 inning for italy as they are the away team
Note: In baseball the away team does not pitch the bottom half of the final inning in a game they lose,
if this line of code is reached that implies Italy lost hence one less inning for them
"""
Mexico.o += 3 * innings
Italy.o  += 3 * (innings - 1)


"""
compare the RQs to see who advances
"""
countries_sorted = sorted(countries, key= lambda c: c.rq)

if countries_sorted[0].country == "USA" or countries_sorted[1].country == "USA":
    print("\nUSA WILL ADVANCE")
else:
    print("\nUSA FAIL TO ADVANCE")

print(f"\n1. {countries_sorted[0].country} \n2. {countries_sorted[1].country} \n3. {countries_sorted[2].country}")
print(f"\n1. {countries_sorted[0].country} - {countries_sorted[0].rq} \n2. {countries_sorted[1].country} - {countries_sorted[1].rq} \n3. {countries_sorted[2].country} - {countries_sorted[2].rq}")

