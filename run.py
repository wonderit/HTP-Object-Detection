from ultralytics import YOLO, checks, hub

checks()
hub.login('4f7cc76449b94b9296b02a5daf899a7da76785a00f')

model = YOLO('https://hub.ultralytics.com/models/8DocExMxz7lIVLRtiLHh')
model.train()