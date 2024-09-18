from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="my_api_application",
    version="0.1.0"
)


@app.get(
    "/",
    summary="Стартовая страница",
    tags=["Главная"]
)
def index():
    return {"status": 200, "message": "Привет мир!"}


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        reload=True
    )
