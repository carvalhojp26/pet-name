import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from schemas.pet import Pet

load_dotenv()

creds = Credentials(
    api_key=os.environ["IBM_WX_API_KEY"],
    url=os.environ["IBM_WX_URL"]
)

MODEL_ID = "ibm/granite-3-8b-instruct"

params = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.2
}

model = ModelInference(
    model_id=MODEL_ID,
    credentials=creds,
    project_id=os.environ["IBM_WX_PROJECT_ID"],
    params=params
)

def build_prompt(pet: Pet) -> str:
    description = ", ".join(pet.descriptors) if pet.descriptors else ""
    return f"""
You are a pet name generator.

Task:
- Create a creative name for a {pet.sex} {pet.animal}.
- The name should reflect this description: "{description}".

Output:
- Provide 1 suggested name.
- Explain in 2-3 sentences why this name was chosen.
- Format:
  Name: <name>
  Reason: <short reason>
"""

def generate_pet_name(pet: Pet) -> dict:
    prompt = build_prompt(pet)
    response = model.generate_text(prompt=prompt)
    return response

# resp = model.generate_text(prompt=prompt)
# print(resp)
