from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

DATABASE_URL = "mysql+pymysql://root:@localhost/company"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class EmployeeTable(Base):

    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    department = Column(String(100))
    salary = Column(Float)


Base.metadata.create_all(bind=engine)


class EmployeeModel(BaseModel):

    id: int
    name: str
    age: int
    department: str
    salary: float


@app.get("/")
def home():

    return {"message": "Employee API Running"}


@app.get("/employees")
def get_employees():

    db = SessionLocal()

    data = db.query(EmployeeTable).all()

    return data


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    db = SessionLocal()

    data = db.query(EmployeeTable).filter(
        EmployeeTable.id == employee_id
    ).first()

    if data:
        return data

    return {"message": "Employee not found"}


@app.post("/employees")
def add_employee(employee: EmployeeModel):

    db = SessionLocal()

    new_employee = EmployeeTable(
        id=employee.id,
        name=employee.name,
        age=employee.age,
        department=employee.department,
        salary=employee.salary
    )

    db.add(new_employee)

    db.commit()

    return {"message": "Employee added successfully"}


@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeModel):

    db = SessionLocal()

    data = db.query(EmployeeTable).filter(
        EmployeeTable.id == employee_id
    ).first()

    if data:

        data.name = employee.name
        data.age = employee.age
        data.department = employee.department
        data.salary = employee.salary

        db.commit()

        return {"message": "Employee updated successfully"}

    return {"message": "Employee not found"}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    db = SessionLocal()

    data = db.query(EmployeeTable).filter(
        EmployeeTable.id == employee_id
    ).first()

    if data:

        db.delete(data)

        db.commit()

        return {"message": "Employee deleted successfully"}

    return {"message": "Employee not found"}   