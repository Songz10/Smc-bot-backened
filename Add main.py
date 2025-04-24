from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/orderbook")
def get_orderbook():
    # This is a basic response to check if your app is live.
    return JSONResponse(content={"status": "Live from Render!"})
