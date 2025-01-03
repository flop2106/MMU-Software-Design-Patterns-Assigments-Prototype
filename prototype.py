import copy

class HealthInsurancePrototype:
    def __init__(self, base_coverage = None, base_premium=0.0):
        self.base_coverage = base_coverage or []
        self.base_premium = base_premium
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Coverage: {self.base_coverage}, Base Premium: ${self.base_premium:.2f}"

class MaleInsurance(HealthInsurancePrototype):
    def __init__(self):
        super().__init__(["Basic Hospitalization", "Annual Checkup"], 500)

class FemaleInsurance(HealthInsurancePrototype):
    def __init__(self):
        super().__init__(["Basic Hospitalization", "Annual Checkup", "Maternity"], 600)
