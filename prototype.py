import copy

class HealthInsurancePrototype:
    def __init__(self, base_coverage=None, base_premium=0.0):
        self.base_coverage = base_coverage or []
        self.base_premium = base_premium

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        result = f"Dental Care Total Base Premium: ${self.base_premium:.2f},\\n Coverage: {self.base_coverage}"
        return result


class MaleInsurance(HealthInsurancePrototype):
    def __init__(self):
        super().__init__(
            [
                "Brush teeth 3 times a day using fluoride toothpaste",
                "Floss at least once every day",
                "Schedule a dental appointment every 6 months",
                "Avoid smoking to maintain gum health",
            ],
            500.00,
        )


class FemaleInsurance(HealthInsurancePrototype):
    def __init__(self):
        super().__init__(
            [
                "Brush teeth 2-3 times a day using fluoride toothpaste",
                "Floss every day",
                "Schedule a dental appointment every 6 months",
                "Additional dental checkups during pregnancy",
                "Maintain a balanced diet to ensure dental health",
            ],
            550.00,
        )
