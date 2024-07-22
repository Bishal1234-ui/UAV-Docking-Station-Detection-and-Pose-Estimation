
from ultralytics import RTDETR

# Load a COCO-pretrained RT-DETR-l model
model = RTDETR('rtdetrcustom.pt')

# Run inference on an image
results = model(source = '3v.mp4', show=True, conf=0.4, save=True) #generator of results
