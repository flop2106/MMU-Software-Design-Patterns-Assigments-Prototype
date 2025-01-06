import logging
from facade import DentalCareFacade

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DentalState:
    def handle_request(self, context):
        raise NotImplementedError("Handle request must be implemented")

class IdleState(DentalState):
    def handle_request(self, context):
        logging.info("System is idle. Waiting for user input...")
        if not context.user_data:
            logging.error("No user data provided. Transition to ProcessingState skipped.")
            return
        context.transition_to(ProcessingState())

class ProcessingState(DentalState):
    def handle_request(self, context):
        try:
            logging.info("Processing user input and customizing insurance plan...")
            user_data = context.user_data

            # Validate user data
            if not user_data or "gender" not in user_data:
                logging.error("Invalid user data. Transition aborted.")
                context.transition_to(IdleState())
                return

            # Generate and customize dental care plan
            dental_care = context.facade.get_dental_template(user_data["gender"])
            customized_plan = context.facade.customize_dental_care(dental_care, user_data)
            context.result = customized_plan

            logging.info("Dental Care plan successfully customized.")
            context.transition_to(CompletedState())
        except Exception as e:
            logging.error(f"Error during processing: {e}")
            context.transition_to(IdleState())

class CompletedState(DentalState):
    def handle_request(self, context):
        if context.result:
            logging.info("Processing complete. Delivering the Dental Care plan...")
            logging.info(f"Result: {context.result}")
        else:
            logging.warning("No result found. Transitioning to IdleState.")
        context.transition_to(IdleState())

class DentalContext:
    def __init__(self):
        self.state = IdleState()
        self.user_data = None
        self.result = None
        self.facade = DentalCareFacade()

    def set_user_data(self, data):
        self.user_data = data
        # Start processing after setting user data
        self.request()

    def request(self):
        self.state.handle_request(self)

    def transition_to(self, new_state):
        logging.info(f"Transitioning from {self.state.__class__.__name__} to {new_state.__class__.__name__}")
        self.state = new_state

