from facade import InsuranceFacade

class InsuranceState:
    def handle_request(self, context):
        raise NotImplementedError("Handle request must be implemented")

class IdleState(InsuranceState):
    def handle_request(self, context):
        print("System is idle. Waiting for user input....")
        context.state = ProcessingState()

class ProcessingState(InsuranceState):
    def handle_request(self, context):
        print("Processing user input and customizing insurance plan...")
        user_data = context.user_data
        insurance = context.facade.get_insurance_template(user_data["gender"])
        customized_plan = context.facade.customize_insurance(insurance, user_data)
        context.result = customized_plan
        context.state = CompletedState()
    
class CompletedState(InsuranceState):
    def handle_request(self, context):
        print("Processing Complete. Delivering the insurance plan...")
        print(context.result)
        context.state = IdleState()

class InsuranceContext:
    def __init__(self):
        self.state = IdleState()
        self.user_data = None
        self.result = None
        self.facade = InsuranceFacade()
    
    def set_user_data(self, data):
        self.user_data = data
    
    def request(self):
        self.state.handle_request(self)