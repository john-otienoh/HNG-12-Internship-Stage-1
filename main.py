"""
    An API that takes a number and returns interesting mathematical properties about it,
    along with a fun fact.
"""
import requests
from pydantic import BaseModel
from fastapi import FastAPI, Query
from functions import digit_sum, is_perfect, is_prime, properties

app = FastAPI()

class BasicInfo(BaseModel):
    """Model for the response"""
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list
    digit_sum: int
    fun_fact: str

number_info = {}

@app.get("/api/classify-number")
async def classify_number(number = Query(..., description="A number.")):
    """
    Returns interesting mathematical properties about a number, along with a fun fact.
    """
    try:
        number = int(number)
        url = f'http://numbersapi.com/{abs(number)}/math'

        number_info["number"] = number
        number_info["is_prime"] = is_prime(number)
        number_info["is_perfect"] = is_perfect(number)
        number_info['properties'] = properties(number)
        number_info['digit_sum'] = digit_sum(number)

        response = requests.get(url)
        if response.status_code == 200:
            number_info["fun_fact"] = response.text

        return number_info

    except ValueError:
        return {
            "number": number,
            "error": True
        }
