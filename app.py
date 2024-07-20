from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import numpy as np
import pandas as pd
import uvicorn
from mlproject.pipeline.prediction import PredictionPipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/train')
def training():
    os.system("python main.py")
    return "Training Successful!!!.."

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...)
):
    try:
        data = np.array([
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
            pH, sulphates, alcohol
        ]).reshape(1, -1)

        obj = PredictionPipeline()
        predict = obj.predict(data)

        return templates.TemplateResponse("results.html", {"request": request, "prediction": str(predict)})

    except Exception as e:
        print('The Exception message is:', e)
        return HTMLResponse(content="Something went wrong", status_code=500)
# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="index.html", context={"id": id}
    # ) 



if __name__ == "__main__":
    uvicorn.run(app, port = 8000)