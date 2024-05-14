import random
import time
from datetime import datetime, timedelta

ec_state_dict = {
    1: "Contracting",
    2: "Expanding",
    3: "Stagnating"
}

class UserControl:
    def __init__(self):
        # social variables
        self.population = 0
        self.past_population = self.population
        self.birth_rate = 0
        # instead of using births and deaths
        # birth rate occasionally takes a calculation of current and past population
        # economic variables
        self.economic_grow = ec_state_dict[2]
        self.current_gdp = 0
        self.past_gdp = self.current_gdp
        self.consumer_spending = 0
        self.government_spending = 0
        self.investment = 0
        self.exports = 0
        self.imports = 0
        # political variables
        self.political_typology = "Democratic"
        # political parties/ideologies will come later on
        self.leader = "Gregory Prescov"
        self.political_power = 100
        self.political_exponent = 1.00
        # objectives
        self.objectives = {"Objectives": [
            {"Domestic"},
            {"Foreign"}
        ]}
        # short term memory
        self.national_policy = {"Policy": [
            {"Domestic Policy"},
            {"Foreign Policy"}
        ]}
        # long term memory
        self.long_term_mem = {"Memories": [
            {"Political"},
            {"Social"},
            {"Economic"},
            {"Military"},
            {"International"}
        ]}

    # population/social functions
    # def check_pop_growth()
    def population_growth(self):
        births = random.randrange(0, 15)
        deaths = random.randrange(0, 10)

        self.population += (births - deaths)
        self.birth_rate = births/deaths
    # economic functions
    # def check_economic_growth
    def economic_growth(self):
        self.consumer_spending = round(random.uniform(100, 5000), 2)
        self.government_spending = round(random.uniform(100, 5000), 2)
        self.investment = round(random.uniform(100, 5000), 2)
        self.exports = round(random.uniform(100, 5000), 2)
        self.imports = round(random.uniform(100, 5000), 2)
        if self.economic_grow == "Expanding":
            self.current_gdp -= (self.consumer_spending + self.government_spending + self.investment + (self.exports - self.imports))

        elif self.economic_grow == "Contracting":
            self.current_gdp += (self.consumer_spending + self.government_spending + self.investment + (
                        self.exports - self.imports))

        else:
            pass

    def check_economic_growth(self, globe):
        if globe.date.month() % 6 == 0:
            # checks if month of date has a remainder of 0 if divided by 6
            if self.past_gdp < self.current_gdp:
                # checking if past GDP is lesser than current GDP
                if self.economic_grow != "Expanding":
                    self.economic_grow = ec_state_dict[2]

            elif self.past_gdp == self.current_gdp:
                if self.economic_grow != "Stagnating":
                    self.economic_grow = ec_state_dict[1]
            else:
                if self.economic_grow != "Contracting":
                    self.economic_grow = ec_state_dict[3]

    # political functions
    def political_power_growth(self):
        self.political_power += self.political_exponent