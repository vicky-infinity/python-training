
import fastapi

app = fastapi.FastAPI()

data = {"Name" : ["Stud 1", "Stud 2", "Stud 3", "Stud 4"],
        "Roll" : [1,2,3,4],
        "Marks" : [89,34,12,35]}

@app.get("/")
async def home():
    return {"Message": "Hey this is the first endpoint",
            "Data": "This is the data present on this endpoint"}

@app.get("/home2")
async def home2():
    return {"MSG" : "This is the Second home page"}

@app.get("/home3")
async def home2():
    return "This is just the string not Dict"

@app.get("/all_students")
async def all_students():
    return data

# Path parameter
@app.get("/student/{roll_no}")
async def student_record(roll_no: int):
    for name, roll, marks in zip(data["Name"], data["Roll"], data["Marks"]):
        if roll_no == roll:
            return {
                "Name" : name,
                "Roll" : roll,
                "Marks" : marks
            }
    return {"Result" : "Student not found"}
    
