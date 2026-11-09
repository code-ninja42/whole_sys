from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

student_data = {}


class StudentModel(BaseModel):
    id: int
    name: str
    age: int
    course: str


@app.get("/")
def home():
    return {"message": "Student API Running"}


@app.get("/student")
def get_students():
    return student_data


@app.get("/student/{student_id}")
def get_student_by_id(student_id: int):

    if student_id in student_data:
        return student_data[student_id]

    return {"message": "Student not found"}


@app.post("/student")
def create_student(student: StudentModel):

    student_data[student.id] = student.dict()

    return {
        "message": "Student added successfully",
        "data": student_data[student.id]
    }


@app.put("/student/{student_id}")
def update_student(student_id: int, student: StudentModel):

    if student_id in student_data:

        student_data[student_id] = student.dict()

        return {
            "message": "Student updated successfully",
            "data": student_data[student_id]
        }

    return {"message": "Student not found"}


@app.patch("/student/{student_id}")
def partial_update_student(student_id: int, updated_data: dict):

    if student_id in student_data:

        student_data[student_id].update(updated_data)

        return {
            "message": "Student partially updated",
            "data": student_data[student_id]
        }

    return {"message": "Student not found"}


@app.delete("/student/{student_id}")
def delete_student(student_id: int):

    if student_id in student_data:

        deleted_student = student_data.pop(student_id)

        return {
            "message": "Student deleted successfully",
            "data": deleted_student
        }

    return {"message": "Student not found"}


    