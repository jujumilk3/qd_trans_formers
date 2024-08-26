from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from tqdm import tqdm
import time
from typing import Generator

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


def generate_progress(progress_int: int = 100) -> Generator[bytes, None, None]:
    for i in tqdm(range(progress_int)):
        time.sleep(0.1)
        yield f"{i}/{progress_int}\n".encode()


@app.get("/progress")
async def progress(progress_int: int = 100):
    return StreamingResponse(generate_progress(progress_int), media_type="text/event-stream")
