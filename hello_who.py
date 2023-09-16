from fastapi import FastAPI, Body, Header

app = FastAPI()

# URL Path
@app.get("/hi_url_path/{who}")
def greet(who):
    return f"Hello {who}"

# Query Parameters
@app.get("/hi_query_params")
def greet(who):
    return f"Hello {who}"

# Body
@app.post("/hi_body")
def greet(who:str = Body(embed=True)):
    return f"Hello {who}"
# 'Body(embed=True)' tell FastAPI to get the value of 'who' from JSON-Formated
# request body.
# The 'embed=True' means that it should loo like { "who": "Mom" } rather than
# just "Mom"

# HTTP Header
@app.post("/hi_header")
def greet(who:str = Header()):
    return f"Hello {who}"

if __name__ == "__main__":
    from uvicorn import run
    run("hello_who:app", reload=True)
    # 'hello' is the file name 'hello.py'
    # 'app' is the FastAPI object 'app = FastAPI()'
    # 'reload=True' tells uvicorn to restart the server if hello.py changes