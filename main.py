from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_data():
    return {"message": "hello world"}


@app.post("/post")
async def post_data(input_str: str):
    return {"message": input_str}


@app.delete("/delete")
async def delete_data(delete_data: str):
    return delete_data
