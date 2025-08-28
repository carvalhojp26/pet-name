import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

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

def build_prompt(animal: str, sex: str, description: str) -> str:
    return f"""
You are a pet name generator.

Task:
- Create a creative name for a {sex} {animal}.
- The name should reflect this description: "{description}".

Output:
- Provide 1 suggested name.
- Explain in 2-3 sentences why this name was chosen.
"""

prompt = build_prompt(
    animal="cat",
    sex="female",
    description="She is very elegant and mysterious, with green eyes.",
)

resp = model.generate_text(prompt=prompt)
print(resp)
