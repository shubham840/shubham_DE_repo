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

    #check is student_id is present or not
    if student_id not in students:
        return {"error": "Student not found"} # return error message if student not found

    # fetch student data from dictonary using student_id as key
    student=students[student_id]

    #check if student exists
    if not student:
        return {"error": "Student not found"} # return error message if student not found

    #return student report card as JSON response
    return {
        "name": student["name"],
        "maths": student["maths"],
        "science": student["science"],
        "english": student["english"]
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

    #check if student exists or not
    if student.id in students:
        return {"error": "Student with this id already exists"}
    
    #add student into dictonary
    students[student.id]={
        "name": student.name,
        "maths": student.maths,
        "science": student.science,
        "english": student.english
    }
    return {"message": f"student {student.name} added successfully!"}

#Now generating student report
@app.get("/students/{student_id}/report")
def get_student_report(student_id:int):

    #check is student_id is present or not
    if student_id not in students:
        return {"error": "Student not found"} # return error message if student not found

    # fetch student data from dictonary using student_id as key
    student=students[student_id]

    #find total marks, percentage and grade
    total_marks=(student["maths"]+student["science"]+student["english"])
    percentage=total_marks/3

    if percentage>90:
        grade="A"
    elif percentage>75:
        grade="B"
    elif percentage>50:
        grade="C"
    else:
        grade="Fail"

    return {
        "name": student["name"],
        "total_marks": total_marks,
        "percentage": percentage,
        "grade": grade
        }

#Now updating student record
@app.put("/student/{student_id}")
def update_student_record(student_id:int, student:Student):
    #check the id which we want to update is present or not
    if student_id not in students:
        return {"error": "Student not found"} # return error message if student not found
    
    #update student record
    students[student_id]={
        "name": student.name,
        "maths": student.maths,
        "science": student.science, 
        "english": student.english
    }
    return {"message": f"student {student_id} updated successfully!"}

#delete student record use delete api
@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    # check if student exist or not
    if student_id not in students:
        return {"error": "Student not found"} # return error message if student not found
    #delete student record
    del students[student_id]
    return {"message": f"student {student_id} deleted successfully!"}