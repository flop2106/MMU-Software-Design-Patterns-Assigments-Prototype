import openai
from prototype import MaleInsurance, FemaleInsurance
openai.api_key = "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"
class InsuranceFacade:
    def __init__(self):
        self.male_insurance = MaleInsurance()
        self.female_insurance = FemaleInsurance()

    def get_insurance_template(self, gender):
        if gender.lower() == "male":
            return self.male_insurance.clone()
        elif gender.lower() == "female":
            return self.female_insurance.clone()
        else:
            raise ValueError("Please select 'Male' or 'Female' only.")
    
    def customize_insurance(self, insurance, user_data):
        # Fetch recommendation via GPT-API
        response = openai.Completion.create(
            engine = "gpt-4o-mini",
            prompt=f"Given the following user details, suggest additional coverage and premium customization: {user_data}",
            max_tokens=100,
        )
        recommendation = response.choices[0].text.strip()

        insurance.base_coverage.append(recommendation)
        insurance.base_premium += 200

        return insurance