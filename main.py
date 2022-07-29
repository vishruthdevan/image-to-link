from http import HTTPStatus
from mimetypes import guess_extension

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/FileUploader", methods=["GET", "POST"])
def FileUploader():
    file = request.get_data()
    with open(f"file{guess_extension(request.content_type)}", "wb") as blob:
        blob.write(file)

    return "works"


if __name__ == "__main__":
    app.run(debug=True)
