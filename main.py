from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "SMC/ICT Bot Backend is live on Render"}
