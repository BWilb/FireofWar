import random
import time
from datetime import datetime, timedelta

class UserControl:
    def __init__(self):
        # social variables
        self.population = 0
        self.past_population = self.population
        self.birth_rate = 0
        # instead of using births and deaths
        # birth rate occasionally takes a calculation of current and past population
        # economic variables
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
        self.long_term_mem = []

    # population/social functions

    # economic functions
    # political functions
