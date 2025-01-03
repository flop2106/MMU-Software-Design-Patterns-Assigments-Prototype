import os
from dotenv import load_dotenv
import openai
from prototype import MaleInsurance, FemaleInsurance

# Load environment variables from the .env file
load_dotenv()

# Get the API key securely from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

class InsuranceFacade:
    def __init__(self):
        self.male_insurance = MaleInsurance()
        self.female_insurance = FemaleInsurance()

    def get_insurance_template(self, gender):
        """
        Fetches the appropriate insurance template based on the gender.
        """
        gender = gender.lower()
        if gender == "male":
            return self.male_insurance.clone()
        elif gender == "female":
            return self.female_insurance.clone()
        else:
            raise ValueError("Invalid gender. Please select 'Male' or 'Female' only.")

    def customize_insurance(self, insurance, user_data):
        """
        Customizes the insurance template based on user data using GPT API.
        """
        try:
            # Construct user prompt for the GPT model
            user_prompt = (
                f"You are a health insurance adviser. "
                f"Given the following user details, suggest a detailed health coverage plan and premium customization: {user_data}"
            )

            # API call to OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": user_prompt}],
                max_tokens=500,
                temperature=0.7,
            )

            # Extracting and processing recommendations
            recommendation = response["choices"][0]["message"]["content"].strip()
            insurance.base_coverage.append(recommendation)
            insurance.base_premium += 200  # Example of adding a flat fee for customization

            return insurance

        except openai.error.OpenAIError as e:
            raise RuntimeError(f"OpenAI API error: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")
