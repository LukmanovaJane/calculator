import uvicorn
from app.backend import app


def run():
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run()
