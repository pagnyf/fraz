class Country:
    def __init__(self, name, capital, population):
        self.name = name
        self.capital = capital
        self.population = population

    def describe(self):
        return f"{self.name} has its capital in {self.capital} and has a population of {self.population}."


# Main
if __name__ == "__main__":
    usa = Country("United States", "Washington, D.C.", 331000000)
    print(usa.describe())
