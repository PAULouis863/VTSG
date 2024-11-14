import json
import time
import cv2
import os
from PIL import Image
import numpy as np

ui_page=Image.open("data/input/0.png")

with open('data/input/0.json') as json_file:
    data = json.load(json_file)

arry_img=np.asarray(ui_page)
h=data['img_shape'][0]
w=data['img_shape'][1]
print(h,w)
res_img = ui_page.resize((w,h))
i=1
foldname=str(i)
os.mkdir(f'D:/papers/paddle4ui/data/output/{foldname}')
for compo in data['compos']:
    # Extract bounding box coordinates
    left = compo['position']['column_min']
    top = compo['position']['row_min']
    right = compo['position']['column_max']
    bottom = compo['position']['row_max']
    # Crop the component from the UI page image
    component = res_img.crop((left, top, right, bottom))
    # Save the cropped component with a unique name based on the component id and current timestamp
    unique_id = compo['id']
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    component.save(f"D:/papers/paddle4ui/data/output/{foldname}\\{unique_id}.png",isText=True)