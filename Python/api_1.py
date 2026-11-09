# courseid 
# coursename
# fees 
# duration
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
course_data = {}

class CourseModel(BaseModel):
    id : int
    coursename : str
    fees : int
    duration : int

@app.get("/")
def home():
    return {"message":"course API running"}

@app.get("/course")
def get_courses():
    return course_data

@app.get("/course/{course_id}")
def get_course(course_id:int):
    if course_id in course_data:
        return course_data[course_id]
    return {"message": "course not found"}
@app.post("/course")
def create_course(course:CourseModel):
    course_data[course.id] = course.dict()
    return {
        "message": "post successfully",
        "data": course_data[course.id]
    }
@app.put("/course/{course_id}")
def update_all(course_id:int,course:CourseModel):
    if course_id in course_data:
        course_data[course_id] = course.dict()
        return {
            "message": "successfull",
            "data":course_data[course_id]
        }
    return {
        "message": "not found"
    }

@app.patch("/course/{course_id}")
def update_particular(course_id:int,updated_1:dict):
    if course_id in course_data:
        course_data[course_id].update(updated_1)
        return {
            "message":"successfully",
            "data":course_data[course_id]
        }
    return {
        "message": "not found"
    }
@app.delete("/course/{course_id}")
def delete_data(course_id:int):
    if course_id in course_data:
        deleted = course_data.pop(course_id)
        return {
            "message": "deleted successfully",
            "data":deleted
        }
    return {
        "message": "not found"
    }