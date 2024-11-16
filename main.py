from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import pickle

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load your pre-trained model
with open('titanic_model.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
async def predict(
    pclass: int = Form(...),
    sex: str = Form(...),
    age: float = Form(...),
    sibsp: int = Form(...),
    parch: int = Form(...),
    fare: float = Form(...),
    embarked: str = Form(...)
):
    # Prepare the input data for prediction
    data = {
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked]
    }
    input_df = pd.DataFrame(data)

    # Perform the prediction (assumes a pre-trained model pipeline is loaded)
    prediction = model_pipeline.predict(input_df)[0]

    # Send back the prediction result
    survived = "Yes" if prediction == 1 else "No"
    return {"Survival Prediction": survived}
