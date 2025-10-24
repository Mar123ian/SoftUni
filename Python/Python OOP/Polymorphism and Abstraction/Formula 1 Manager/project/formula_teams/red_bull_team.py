from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    oracle = {1: 1500000, 2: 800000}
    honda = {3: 20000, 4: 20000, 5: 20000, 6: 20000, 7: 20000, 8: 20000, 9: 10000, 10: 10000}
    expenses_per_race = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        if race_pos > 10:
            pass
        elif race_pos in self.oracle:
            revenue += self.oracle[race_pos]
            revenue += self.honda[min(self.honda.keys())]
        else:
            revenue = self.honda[race_pos]
        revenue -= self.expenses_per_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
