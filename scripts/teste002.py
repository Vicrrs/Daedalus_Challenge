from ultralytics import YOLO

model = YOLO('yolov8n.pt')

class_ids = [2] 

results = model.predict(source='video.mp4')
results.display(render=True, classes=class_ids)
