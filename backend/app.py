from fastapi import FastAPI
from prompt import generate_pet_name
from schemas.pet import Pet

app = FastAPI()

@app.post('/api/pet')
def genenate_name(pet: Pet):
    result = generate_pet_name(pet)
    return result