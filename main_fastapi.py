import uuid

import cloudinary
import cloudinary.api
import cloudinary.uploader
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

load_dotenv()
config = cloudinary.config(secure=True)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/FileUploader")
async def file_upload(request: Request):
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
    return Response(src_url)
