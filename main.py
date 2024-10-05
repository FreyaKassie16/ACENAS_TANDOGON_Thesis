from ultralytics import YOLO

from roboflow import Roboflow
rf = Roboflow(api_key="d84vxl7g4KPneFkzL5GG")
project = rf.workspace("roboflow-universe-projects").project("basketball-players-fy4c2")
version = project.version(16)
dataset = version.download("yolov11")
                

model = YOLO('yolo11n.pt')

results = model.train(data="dataset/data.yaml", epochs=100, imgsz=640)
