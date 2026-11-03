# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pathlib import Path
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.head("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    print("Request for index page received")
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/hello", response_class=HTMLResponse)
def hello(request: Request, name: Annotated[str | None, Form()] = None):
    if name:
        print("Request for hello page received")
        return templates.TemplateResponse(
            request=request, name="hello.html", context={"name": name}
        )

    print("Request for hello page received with no name or blank name; redirecting")
    return RedirectResponse(url=app.url_path_for("index"), status_code=302)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
