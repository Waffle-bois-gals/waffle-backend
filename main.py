from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def buongiorno():
    return {"message": "bonjour"}
