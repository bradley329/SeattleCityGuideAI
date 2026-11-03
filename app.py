# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    print("Request for index page received")
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")

    if name:
        print("Request for hello page received")
        return render_template("hello.html", name=name)

    print("Request for hello page received with no name or blank name; redirecting")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
