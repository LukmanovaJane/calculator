from fastapi import FastAPI, Body, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel, conint, ValidationError

app = FastAPI()


class PostBodyIn(BaseModel):
    # validation as strict positive (greater than zero) integer
    number1: conint(strict=True, gt=0)
    # validation as strict not negative (zero or positive) integer
    number2: conint(strict=True, ge=0)


class PostBodyOut(BaseModel):
    # validation as strict positive (greater than zero) integer
    result: conint(strict=True, gt=0)


@app.post("/calc", response_model=PostBodyOut)
def make_calculation(body: PostBodyIn = Body(...)):
    result = __sum(body.number1, body.number2)
    return {'result': result}


def __sum(number1: int, number2: int):
    """ Returns sum of two received numbers """
    return number1 + number2
