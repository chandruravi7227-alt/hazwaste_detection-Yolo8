# Hazwaste detection using YOLOv8

## Project Overview
This project detects hazardous waste objects using the YOLOv8 object detection model. 
It helps to identify hazardous materials from images and can be used in waste management and environmental safety application.

## Features
-Hazardous waste object detection
-YOLOv8 deep learning model
-FastAPI backend for prediction
-Image upload support
-Real-time detection result

## Technologies used
-python
-YOLOv8
-FastAPI
-openCV
-pillow

## Project structure
app.py
best.pt
uploads/
.gitignore
README.md

# How to run
1. Clone the repository
2. Installl the required packages
3. Run:
   '''bash
   uvicorn app:app --reload

4.open the API in your browser and upload an image for prediction.

# Model Performance
- Precision: 0.7850154221303896
- Recall: 0.875
- mAP50: 0.8433120773561951
- mAP50-95: 0.7171188463316968

## Future Improvements
- Support video detection
- Deploy on the cloud
- Improve model accuracy with more training data

## Author
**Chandru Ravi**
Aspiring Data Scientist
   
