from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    """
    A simple FastAPI endpoint that returns a 'OK' message.

    Returns:
        A dictionary with a 'message' key and 'OK' as the value.
    """
    return {"message": "OK"}
