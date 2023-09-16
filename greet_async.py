from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello World!"

if __name__ == "__main__":
    from uvicorn import run
    run("greet_async:app", reload=True)