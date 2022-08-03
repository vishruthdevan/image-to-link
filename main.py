import uuid
from http import HTTPStatus
from mimetypes import guess_extension

import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)

config = cloudinary.config(secure=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/FileUploader", methods=["GET", "POST"])
def FileUploader():
    file = request.get_data()
    # with open(f"file{guess_extension(request.content_type)}", "wb") as blob:
    #     blob.write(file)
    file_name = str(uuid.uuid4())
    cloudinary.uploader.upload(
        file,
        public_id=file_name,
        unique_filename=False,
        overwrite=True,
    )
    src_url = cloudinary.CloudinaryImage(file_name).build_url()
    return src_url


if __name__ == "__main__":
    app.run(debug=True)
