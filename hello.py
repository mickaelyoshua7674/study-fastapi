from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Home"

@app.get("/hi")
def greet():
    return "Hello? World?"

if __name__ == "__main__":
    from uvicorn import run
    run("hello:app", reload=True)
    # 'hello' is the file name 'hello.py'
    # 'app' is the FastAPI object 'app = FastAPI()'
    # 'reload=True' tells uvicorn to restart the server if hello.py changes
