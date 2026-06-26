from fastapi import FastAPI

app = FastAPI()

@app.get("/student/{user_id}") #Path Parameter
def get_student(user_id : int):
    return {
        "Id": user_id,
        "Name": "Ghanu",
        "Email": "das11022007@gmail.com",
        "city": "Mpk"
    }