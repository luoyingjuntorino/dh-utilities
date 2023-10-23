from fastapi import FastAPI, File, UploadFile, APIRouter, Form
from fastapi.responses import JSONResponse
from datetime import datetime
import pymongo
import os

router = APIRouter()

UPLOAD_FOLDER = "images"  # folder to store
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER) 

@router.post("/upload/image/", tags=["image"])
async def upload_image(image: UploadFile = File(...),
                       description: str = Form(...),):
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d-%H-%M")
    file_name = f"{formatted_time}.hdr"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    # save uploaded image locally(#TODO save it to Docker volumn and image's path save in MongoDB)
    with open(file_path, "wb") as f:
        f.write(image.file.read())
    # save image path to MongoDB
    client = pymongo.MongoClient("localhost", 27017) # connect to Mongo
    db = client["my_database"]  # database name
    images_path_collection = db["images_path"]
    image_doc = {
        "file_name": file_name,
        "path": file_path,
        "description": description
    }
    images_path_collection.insert_one(image_doc)
    #TODO can you update me some image's metadata? single datapoint 
    # can we put image's metadata in the description?
    
    return JSONResponse(content={
        "message": "Image uploaded and saved as {}".format(file_name),
        "description": description,  # metadata of image
        "file_path": file_path
    })