"""
Created a class to hold each country as an object
makes lloking up name with rq easier
"""
class Country:
    def __init__(self, country:str, ra:int, o:int) -> None:
        self.country = country
        self.ra      = ra #Runs Allowed
        self.o       = o #Outs Recorded

    @property #Needed to update the rq automatically for mex and italy later
    def rq(self) -> float:
        return self.ra / self.o
    
USA   = Country("USA", 11, (27 + 27)) #Countries with their stats prior to Italy v Mexico
Mexico = Country("Mexico", 5, 24)
Italy = Country("Italy", 6, 27)
countries = [USA, Mexico, Italy]



def game_score(italy_score=0, mexico_score=0, innings=0):
    italy_score  = int(input("\nHow many runs did Italy score?: "))
    mexico_score = int(input("How many runns did Mexico score?: "))

    winner_check(italy_score, mexico_score)

    Italy.ra    +=  mexico_score
    Mexico.ra   += italy_score

    
def winner_check(italy_score, mexico_score):
    if italy_score > mexico_score: #If Italy wins there is no 3-way tie making rq irrelevant
        print("\nUSA WILL ADVANCE")
        print("\n1. Italy 4-0 \n2. USA 3-1 \n3. Mexico 2-2")
        print("\nRun Quotient irrelevant in this scenario\n")
        exit()
    else:
        return


"""
Multiply innings by three as each team records three outs per inning
-1 inning for italy as they are the away team
Note: In baseball the away team does not pitch the bottom half of the final inning in a game they lose,
if this line of code is reached that implies Italy lost hence one less inning for them
"""

def game_length(innings=0):
    innings = int(input("How many innings did the game last?: "))
    Mexico.o += 3 * innings
    Italy.o  += 3 * (innings - 1)


def main():
    game_score()
    game_length()


    """
    Created a list to have the countries ordered by rq. Did this to mimic standings
    Python's sorted is O(nlogn), ideal for small size as list length will never change
    """
    countries_sorted = sorted(countries, key= lambda c: c.rq)


    if countries_sorted[0].country == "USA" or countries_sorted[1].country == "USA":
        print("\n!-!-! USA WILL ADVANCE !-!-!")
    else:
        print("\n*** USA FAIL TO ADVANCE ***")


    print(f"\nStandings:\n1. {countries_sorted[0].country} \n2. {countries_sorted[1].country} \n3. {countries_sorted[2].country}")
    print(f"\nRun Quotient:\n1. {countries_sorted[0].country}: {countries_sorted[0].rq} \n2. {countries_sorted[1].country}: {countries_sorted[1].rq} \n3. {countries_sorted[2].country}: {countries_sorted[2].rq}")


if __name__ == "__main__":
    main()