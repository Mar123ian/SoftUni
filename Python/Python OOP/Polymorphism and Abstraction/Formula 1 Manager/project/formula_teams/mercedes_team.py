from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    petronas = {1: 1000000, 2: 500000, 3: 500000}

    tv = {4: 100000, 5: 100000, 6: 50000, 7: 50000, 8: 0, 9: 0,
          10: 0}
    expenses_per_race = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        if race_pos > 10:
            pass
        elif race_pos in self.petronas:
            revenue += self.petronas[race_pos]
            revenue += self.tv[min(self.tv.keys())]
        else:
            revenue = self.tv[race_pos]
        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
