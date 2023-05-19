# FastApi Libraries
from fastapi import APIRouter
from fastapi import Path

# schemes 
from backend.schemes.schemes import Function
# service
from backend.services.index import Fourier
from typing import List


fourier_controller = APIRouter(tags=["Fourier Function"])

@fourier_controller.post(
    path="/calculate-fourier",
    response_description="calculated successfully"
)
def tabulate_function(
    functions: List[Function],
    period: str
):
    return Fourier.calculate_fourier_dommies(functions, period)