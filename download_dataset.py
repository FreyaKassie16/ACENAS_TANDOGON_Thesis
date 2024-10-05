from roboflow import Roboflow
rf = Roboflow(api_key="d84vxl7g4KPneFkzL5GG")
project = rf.workspace("roboflow-universe-projects").project("basketball-players-fy4c2")
version = project.version(16)
dataset = version.download("yolov11")
