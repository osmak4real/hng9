from fastapi import FastAPI
app = FastAPI()
@app.get("/aboutme")
def aboutme():
    return {"slackUsername":"osmak", "backend":"true","age":32,"bio":"I am Nigerian and my dream is to become a full stack developer"}

