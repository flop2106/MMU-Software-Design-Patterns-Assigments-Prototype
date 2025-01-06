import copy

class DentalCarePrototype:
    def __init__(self, base_coverage=None, base_premium=0.0):
        self.base_coverage = base_coverage or []
        self.base_premium = base_premium

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        result = f"Coverage: {self.base_coverage}"
        return result


class MaleDentalCare(DentalCarePrototype):
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


class FemaleDentalCare(DentalCarePrototype):
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
