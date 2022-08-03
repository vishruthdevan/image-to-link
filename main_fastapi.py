import uuid

import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

load_dotenv()
config = cloudinary.config(secure=True)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.route("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.route("/FileUploader", methods=["GET", "POST"])
async def FileUploader(request: Request):
    file = await request.body()
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