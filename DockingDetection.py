from ultralytics import YOLO

# #Load a pretrained YOLOV8m model
model = YOLO('best.pt')

# #Run inference on the source
results = model(source = '3v.mp4', show=True, conf=0.4, save=True) #generator of results
