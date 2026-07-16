from fastapi import FastAPI,File,UploadFile
from ultralytics  import YOLO
import io
import json
from PIL import Image

app=FastAPI()

model=YOLO("best (2).pt")

@app.get("/")
def home():
    return {"message": "API is running!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents= await file.read()
        image=Image.open(io.BytesIO(contents)).convert("RGB")
        results= model.predict(image)

        json_results=json.loads(results[0].to_json())
        return {"status": "success", "detections": json_results}
    except Exception as e:
        return {"status": "error", "message": str(e)}


