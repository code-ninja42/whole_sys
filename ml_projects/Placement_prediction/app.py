from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI(title="Placement Prediction API")

# Load the trained model
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)


class PlacementInput(BaseModel):
    cgpa: float
    internships: int
    projects: int
    workshops_certifications: int
    aptitude_test_score: float
    soft_skills_rating: float
    ssc_marks: float
    hsc_marks: float
    placement_training: int
    extracurricular_activities: int


@app.get("/")
def home():
    return {
        "message": "Placement Prediction API is Running"
    }


@app.post("/predict")
def predict(data: PlacementInput):

    features = np.array([[
        data.cgpa,
        data.internships,
        data.projects,
        data.workshops_certifications,
        data.aptitude_test_score,
        data.soft_skills_rating,
        data.ssc_marks,
        data.hsc_marks,
        data.placement_training,
        data.extracurricular_activities
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        result = "Placed"
    else:
        result = "Not Placed"

    return {
        "prediction": result
    }
    