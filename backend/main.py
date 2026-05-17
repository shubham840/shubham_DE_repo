#import FastAPI class from fastapi module or package
from fastapi import FastAPI
from pydantic import BaseModel # pydantic handle datatype chceking, validation and request parsing 

#create object of FastAPI class and assign it to variable app
app = FastAPI()

#students data

students = {
    1: {"name": "Rahul",
        "maths": 85,
        "science": 90,
        "english": 80
        },
    2: {"name": "Priya",
        "maths": 95,
        "science": 88,
        "english": 92
        },
    3: {"name": "abhi",
        "maths": 78,
        "science": 85,
        "english": 82
        }
}
#create decorator for GET request to root endpoint("/") and define function to return response 
@app.get("/")
def home(): # if request comes to "/" endpoint, this function will be executed and return response
    return {"message": "Backend is running!"} # return a JSON response with a message key and value "Backend is working!"

#api to fetch student report card based on student id
@app.get("/students/{student_id}") # define endpoint with path parameter student_id
def get_student(student_id: int):
    # fetch student data from dictonary using student_id as key
    student = students.get(student_id)

    #check if student exists
    if not student:
        return {"error": "Student not found"} # return error message if student not found
    
    #calculate total marks
    total_marks = (
        student["maths"] + student["science"] + student["english"]
    )

    #claculate percentage
    percentage = total_marks / 3

    #return student report card as JSON response
    return {
        "name": student["name"],
        "maths": student["maths"],
        "science": student["science"],
        "english": student["english"],
        "total_marks": total_marks,
        "percentage": percentage
    }


#expected structure of incoming JSON data for creating a new student record
class Student(BaseModel): #BaseModel is a class from pydantic module that we can use to define the expected structure of incoming JSON data for creating a new student record
    id:int
    name:str
    maths:float
    science:float
    english:float


#Creating post API to add new student record
@app.post("/student")
def add_student(student:Student): #receive request body conevrt into student object and validate automatically.
    #add student into dictonary
    students[student.id]={
        "name": student.name,
        "maths": student.maths,
        "science": student.science,
        "english": student.english
    }
    return {"message": f"student {student.name} added successfully!"}