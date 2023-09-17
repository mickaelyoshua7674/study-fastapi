from fastapi import FastAPI, Depends, params

def user_dep(name: str=params, password: str=params) -> dict:
    return {"name": name, "valid": True}

app = FastAPI()

@app.get("/user")
def get_user(user: dict=Depends(user_dep)) -> dict:
    return user

if __name__ == "__main__":
    from uvicorn import run
    run(app="dependencies_test:app", reload=True)