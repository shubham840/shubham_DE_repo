#import FastAPI class from fastapi module or package
from fastapi import FastAPI

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