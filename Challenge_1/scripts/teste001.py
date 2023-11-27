from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.predict(source=r'C:\Users\rozas\Documents\Projects\Vicsion_Challenge\video\video.mp4', show=True)
