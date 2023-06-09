# FastApi Libraries
from fastapi import APIRouter
from fastapi import Path, Body

# schemes 
from backend.schemes.schemes import Function
# service
from backend.services.index import FunctionOperations


function_controller = APIRouter(tags=["Controller Functions"])

@function_controller.post(
    path="/tabulate_function",
    response_description="function tabulated successfully"
)
def tabulate_function(
    function: Function
):
    print(function)
    return FunctionOperations.tabulate_function(function)