from fastapi import FastAPI, Depends, params

def check_dep(name: str=params, password: str=params) -> None:
    if not name:
        raise

app = FastAPI()

@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True

if __name__ == "__main__":
    from uvicorn import run
    run(app="dependencies_decorator:app", reload=True)