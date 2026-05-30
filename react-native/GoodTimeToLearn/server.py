from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
import numexpr as ne
from sympy import sympify, SympifyError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class request_for_evalution(BaseModel):
    user : str
    exp : str

@app.post("/num")
def calculate(data: request_for_evalution):
    try: 
        ans = sophisticated_eval(data.exp)
        print(f"{data.user} is asking to do this math: {data.exp}")
        return {"ans": str(ans)}
    except:
        return {"ans": "syntax error"}
    


def sophisticated_eval(expression: str) -> str:
    expression = expression.strip().lower()
    expression = expression.replace('^', '**')
    allowed_pattern = re.compile(r'^[0-9.+\-*/%() \s]|sin|cos|tan|log10|log]+$')
    if not allowed_pattern.match(expression):
        return "Error: Invalid characters detected"

    try:
        safe_expr = sympify(expression, evaluate=False)
        expr_string = str(safe_expr)
        result = ne.evaluate(expr_string).item()
        if isinstance(result, float):
            result = round(result, 10)
            if result.is_integer():
                result = int(result)
                
        return str(result)

    except (SympifyError, TypeError, ZeroDivisionError, KeyError, SyntaxError) as e:
        return f"Error: Invalid Expression"