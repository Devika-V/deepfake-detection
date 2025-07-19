from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn
from PIL import Image
import io
import shutil
import os
import cv2
import numpy as np

# Import model and preprocessing
from classifiers import Meso4
from preprocess import preprocess_input

# Initialize FastAPI app
app = FastAPI()

# Create upload and weights directories if not exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the Meso4 DeepFake model
model = Meso4()
model.model.load_weights("weights/Meso4_DF.h5")

# Root route for testing
@app.get("/")
def root():
    return {"message": "Hello, FastAPI is working!"}

# Function to extract frames from uploaded video
def extract_frames(video_path, max_frames=5):
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while cap.isOpened() and count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        count += 1
    cap.release()
    return frames

# Predict on one frame
def predict_frame(frame):
    img = cv2.resize(frame, (256, 256))
    img = preprocess_input(np.array(img, dtype=np.float32))
    img = np.expand_dims(img, axis=0)
    prediction = model.model.predict(img)[0][0]
    return prediction

# Upload route
@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    try:
        # Save uploaded file
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract frames
        frames = extract_frames(file_location)

        if not frames:
            return JSONResponse(status_code=400, content={"error": "No frames extracted from video."})

        # Run prediction on each frame
        predictions = [predict_frame(frame) for frame in frames]
        avg_score = float(np.mean(predictions))
        label = "Real" if avg_score >= 0.5 else "Fake"

        return JSONResponse(content={
            "filename": file.filename,
            "frames_analyzed": len(frames),
            "average_score": round(avg_score, 4),
            "label": label
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})



