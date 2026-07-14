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





